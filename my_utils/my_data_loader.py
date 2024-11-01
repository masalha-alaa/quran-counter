import pandas as pd
from yaml import safe_load
from json import load as j_load
from my_utils.utils import resource_path, AppLang
from difflib import get_close_matches


class PageVerses:
    def __init__(self, surah_num, verses_range, verses, has_next):
        self.surah_num = surah_num
        self.verses_range = verses_range
        self.verses = verses
        self.has_next = has_next


class MyDataLoader:
    df = None
    _working_col = None
    page_surah_verses = None
    surah_num_to_name_map = None
    surah_name_to_num_map = None
    waw_words = None
    FIRST_SURAH = 1
    LAST_SURAH = 114
    MIN_VERSE = 1
    MAX_VERSE = 286

    def __init__(self):
        if MyDataLoader.df is None:
            config = safe_load(open(resource_path("config.yml"), mode='r'))
            pages = j_load(open(resource_path('data/surah-num-page-map.json')))
            MyDataLoader.surah_num_to_name_map = j_load(open(resource_path('data/surah-map.json'), encoding='utf-8'))
            MyDataLoader.surah_name_to_num_map = {v:k for k,v in MyDataLoader.surah_num_to_name_map.items()}
            MyDataLoader.df = pd.read_json(resource_path(config['data']['path']))
            MyDataLoader.df['total_verses'] = MyDataLoader.df['total_verses'].astype(int)
            MyDataLoader.waw_words = set(j_load(open(resource_path('data/waw_words.json'), encoding='utf-8')))
            # TODO: save columns in df beforehand
            verses_col = config['data']['verses_column']
            MyDataLoader._working_col = f"{verses_col}_split"
            MyDataLoader.df[MyDataLoader._working_col] = MyDataLoader.df[verses_col].str.split('\n')
            MyDataLoader.df['page'] = MyDataLoader.df['surah'].apply(lambda s: pages[str(s)])
            MyDataLoader.page_surah_verses = pd.read_json(resource_path("data/page-surah-verses.json"))

    # surah-map methods [BEGIN]
    @staticmethod
    def get_surah_name(surah_num):
        return MyDataLoader.surah_num_to_name_map.get(str(surah_num))

    @staticmethod
    def get_surah_num(surah_name, source_language: AppLang = AppLang.ARABIC):
        if (num := MyDataLoader.surah_name_to_num_map.get(str(surah_name))) is None:
            return MyDataLoader.surah_name_to_num_map.get(MyDataLoader._get_closest_surah_name(surah_name))
        return num

    @staticmethod
    def _get_closest_surah_name(surah_name):
        closest = get_close_matches(surah_name, MyDataLoader.surah_name_to_num_map.keys(), n=1, cutoff=0.80)
        if closest:
            return closest[0]
        return None
    # surah-map [END]

    # df methods [BEGIN]
    @staticmethod
    def get_verse(surah_num, verse_num):
        return MyDataLoader.df.loc[int(surah_num), MyDataLoader._working_col][int(verse_num - 1)]

    @staticmethod
    def get_verses(surah_num, verses_nums):
        return [MyDataLoader.df.loc[int(surah_num), MyDataLoader._working_col][v-1] for v in verses_nums]

    @staticmethod
    def get_number_of_verses(surah_num):
        return MyDataLoader.df.loc[int(surah_num), 'total_verses']

    @staticmethod
    def get_surah(surah_num):
        return MyDataLoader.df.loc[int(surah_num), MyDataLoader._working_col]

    @staticmethod
    def get_data():
        return MyDataLoader.df

    @staticmethod
    def get_working_col():
        return MyDataLoader._working_col

    @staticmethod
    def get_first_page_of_surah(surah_num):
        return MyDataLoader.df.loc[int(surah_num), 'page']

    @staticmethod
    def iterate_over_verses_words(start_surah_num, start_verse_num, start_word_in_verse_num,
                                  end_surah_num=None, end_verse_num=None, end_word_in_verse_num=None):
        if end_word_in_verse_num is None:
            end_word_in_verse_num = MyDataLoader.MAX_VERSE + 1
        if end_surah_num is None:
            end_surah_num = MyDataLoader.LAST_SURAH
            if end_verse_num is None:
                end_verse_num = MyDataLoader.get_num_of_last_verse_in_surah(end_verse_num)
        elif end_verse_num is None:
            end_verse_num = MyDataLoader.get_num_of_last_verse_in_surah(end_verse_num)

        s, v = int(start_surah_num), int(start_verse_num)
        while s <= min(end_surah_num, MyDataLoader.LAST_SURAH):
            is_final_surah = s == min(end_surah_num, MyDataLoader.LAST_SURAH)
            if is_final_surah:
                verses_to_read = min(end_verse_num, MyDataLoader.get_num_of_last_verse_in_surah(s))
            else:
                verses_to_read = MyDataLoader.get_num_of_last_verse_in_surah(s)
            if v <= verses_to_read:
                verse = MyDataLoader.get_verse(s, v)
                start = start_word_in_verse_num if (s == start_surah_num and v == start_verse_num) else 0
                for i in range(start, len((words := verse.split()))):
                    if s == end_surah_num and v == verses_to_read and i > end_word_in_verse_num:
                        break
                    yield words[i]
                v += 1
                if v > verses_to_read:
                    s += 1
                    v = 1
    # df methods [END]

    # page-surah-verses methods [BEGIN]
    @staticmethod
    def get_verses_of_page(page):
        results = []
        for i, row in (data := MyDataLoader.page_surah_verses.loc[MyDataLoader.page_surah_verses['page'] == int(page)]).iterrows():
            _, surah_num, verses_range = row
            # results.append((surah_num, verses_range, MyDataLoader.get_verses(surah_num, range(verses_range[0], verses_range[1]+1))))
            results.append(PageVerses(surah_num,
                                      verses_range,
                                      MyDataLoader.get_verses(surah_num, range(verses_range[0], verses_range[1]+1)),
                                      has_next=i - data.index[0] < data.shape[0] - 1))
        return results

    @staticmethod
    def get_num_of_last_verse_in_surah(surah_num):
        # TODO: if too slow, create a post-processed json surah_num: num_of_verses
        return int(MyDataLoader.page_surah_verses.loc[MyDataLoader.page_surah_verses['surah'] == int(surah_num), 'verses'].iloc[-1][-1])

    @staticmethod
    def get_verses_of_surah_verse_ref(surah_num, verse_num):
        surah_num, verse_num = int(surah_num), int(verse_num)
        surah_pages = MyDataLoader.page_surah_verses.loc[MyDataLoader.page_surah_verses['surah'] == surah_num, ['page', 'verses']]
        for _, (surah_page, verses_range) in surah_pages.iterrows():
            if verses_range[0] <= verse_num <= verses_range[1]:
                return surah_page
        return None
    # page-surah-verses methods [END]

    # waw-words methods [BEGIN]
    @staticmethod
    def is_waw_part_of_word(word):
        return word in MyDataLoader.waw_words
    # waw-words methods [END]

    # OTHER [BEGIN]
    @staticmethod
    def page_to_juzz(page):
        page = int(page)
        if page <= 21:
            return 1
        if page <= 41:
            return 2
        if page <= 61:
            return 3
        if page <= 81:
            return 4
        if page <= 101:
            return 5
        if page <= 120:
            return 6
        if page <= 141:
            return 7
        if page <= 161:
            return 8
        if page <= 181:
            return 9
        if page <= 200:
            return 10
        if page <= 221:
            return 11
        if page <= 241:
            return 12
        if page <= 261:
            return 13
        if page <= 281:
            return 14
        if page <= 301:
            return 15
        if page <= 321:
            return 16
        if page <= 341:
            return 17
        if page <= 361:
            return 18
        if page <= 381:
            return 19
        if page <= 401:
            return 20
        if page <= 421:
            return 21
        if page <= 441:
            return 22
        if page <= 461:
            return 23
        if page <= 481:
            return 24
        if page <= 501:
            return 25
        if page <= 521:
            return 26
        if page <= 541:
            return 27
        if page <= 561:
            return 28
        if page <= 581:
            return 29
        if page <= 604:
            return 30
        # Shouldn't get here
        return 1

    @staticmethod
    def juz_to_page(juz):
        juz = int(juz)
        if juz == 1:
            return 1
        if juz == 7:
            return 121
        if juz == 1:
            return 201
        if juz <= 30:
            return (juz - 1) * 20 + 2
        # Shouldn't get here
        return 1
    # OTHER [END]
