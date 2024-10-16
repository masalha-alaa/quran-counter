import pandas as pd
from yaml import safe_load
from json import load as j_load
from my_utils import resource_path
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

    def __init__(self):
        if MyDataLoader.df is None:
            config = safe_load(open(resource_path("config.yml"), mode='r'))
            pages = j_load(open(resource_path('data/surah-num-page-map.json')))
            MyDataLoader.surah_num_to_name_map = j_load(open(resource_path('data/surah-map.json'), encoding='utf-8'))
            MyDataLoader.surah_name_to_num_map = {v:k for k,v in MyDataLoader.surah_num_to_name_map.items()}
            MyDataLoader.df = pd.read_json(resource_path(config['data']['path']))
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
    def get_surah_num(surah_name):
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
        return MyDataLoader.df.loc[MyDataLoader.df['surah'] == int(surah_num), MyDataLoader._working_col].iloc[0][int(verse_num - 1)]

    @staticmethod
    def get_verses(surah_num, verses_nums):
        return [MyDataLoader.df.loc[MyDataLoader.df['surah'] == int(surah_num), MyDataLoader._working_col].iloc[0][v-1] for v in verses_nums]

    @staticmethod
    def get_surah(surah_num):
        return MyDataLoader.df.loc[MyDataLoader.df['surah'] == int(surah_num), MyDataLoader._working_col].iloc[0]

    @staticmethod
    def get_data():
        return MyDataLoader.df

    @staticmethod
    def get_working_col():
        return MyDataLoader._working_col

    @staticmethod
    def get_first_page_of_surah(surah_num):
        return MyDataLoader.df.loc[MyDataLoader.df['surah'] == int(surah_num), 'page'].iloc[0]
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
    # page-surah-verses methods [BEGIN]
