from enum import Enum, auto
import re
from arabic_reformer import rub_el_hizb_mark, sujood_mark, waw_khunjariyah
from arabic_reformer import remove_diacritics, normalize_alif, strip_last_diacritic
from my_utils.my_data_loader import MyDataLoader


class DiacriticsRemoval(Enum):
    DO_NOT_REMOVE = auto()
    REMOVE_ALL = auto()
    REMOVE_LAST = auto()


class Preprocessor:
    space_regex = re.compile(rf"[\s{rub_el_hizb_mark}{sujood_mark}]{{2,}}")

    def __init__(self, diac_removal=DiacriticsRemoval.REMOVE_ALL):
        self.diac_removal = diac_removal
        MyDataLoader()

    def normalize_alif(self, text, normalize_khunjariya=False):
        return normalize_alif(text, normalize_khunjariya)

    def normalize_final_yaa(self, text):
        if text.endswith("ي"):
            return f"{text[:-1]}ى"
        return text

    def normalize_final_ta(self, text):
        return text.replace("ة", "ه")

    def normalize_for_root(self, text):
        return self.normalize_final_ta(self.normalize_final_yaa(self.normalize_alif(text)))

    def preprocess_word(self, w, diac_removal=None, remove_waw=True):
        if diac_removal is None:
            diac_removal = self.diac_removal
        if remove_waw and w.startswith("و") and not MyDataLoader.is_waw_part_of_word(w):
            w = w[1:]
        if w.endswith("ي"):
            w = f"{w[:-1]}ى"
        # NOTE: normalize_waw_khunjariya must be before removing diac
        # NOTE: khunjariyah is removed by remove_diacritics
        if w.endswith(waw_khunjariyah):
            w = w[:-1]
        normalized = normalize_alif(MyDataLoader.normalize_waw_khunjariya(w), normalize_khunjariya=True)
        match diac_removal:
            case DiacriticsRemoval.DO_NOT_REMOVE:
                pass
            case DiacriticsRemoval.REMOVE_ALL:
                normalized = remove_diacritics(normalized)
            case DiacriticsRemoval.REMOVE_LAST:
                normalized = strip_last_diacritic(normalized)
        return normalized

    def preprocess_sentence(self, text, diac_removal=None, split_waw=True):
        if diac_removal is None:
            diac_removal = self.diac_removal

        s_processed = []
        for w in text.split():
            if w.endswith(waw_khunjariyah):
                w = w[:-1]
            # NOTE: normalize_waw_khunjariya must be before removing diac
            # NOTE: khunjariyah is removed by remove_diacritics
            w = MyDataLoader.normalize_waw_khunjariya(w)
            if not w.startswith("و") or MyDataLoader.is_waw_part_of_word(w):
                s_processed.append(w)
            else:
                if split_waw:
                    s_processed.append(w[0])
                    s_processed.append(w[1:])
                else:
                    s_processed.append(w)
        for i, w in enumerate(s_processed):
            match diac_removal:
                case DiacriticsRemoval.DO_NOT_REMOVE:
                    pass
                case DiacriticsRemoval.REMOVE_ALL:
                    s_processed[i] = remove_diacritics(w)
                case DiacriticsRemoval.REMOVE_LAST:
                    s_processed[i] = strip_last_diacritic(w)
        s_processed = ' '.join(s_processed)
        s_processed = normalize_alif(MyDataLoader.normalize_waw_khunjariya(s_processed), normalize_khunjariya=True)
        s_processed = Preprocessor.space_regex.sub(" ", s_processed).strip()
        return s_processed

    def replace_laa(self, ser):
        s1 = 'ٱلْـَٔا'
        t1 = 'ٱلْأَ'
        s2 = 'لَـَٔا'
        t2 = 'لَأَ'
        s3 = 'لِـَٔا'
        t3 = 'لِأَ'
        s4 = 'لَّـَٔا'
        t4 = 'لَّأَ'
        s5 = 'لَلْـَٔا'
        t5 = 'لَلْأَ'
        s6 = 'لِّلْـَٔا'
        t6 = 'لِّلْأَ'
        return (ser.str.replace(s1, t1).
                str.replace(s2, t2).
                str.replace(s3, t3).
                str.replace(s4, t4).
                str.replace(s5, t5).
                str.replace(s6, t6))


if __name__ == '__main__':
    # TEST
    # s = "وَأَطِيعُوا۟ ٱللَّهَ وَأَطِيعُوا۟ ٱلرَّسُولَ ۚ فَإِن تَوَلَّيْتُمْ فَإِنَّمَا عَلَىٰ رَسُولِنَا ٱلْبَلَـٰغُ ٱلْمُبِينُ"
    s = "وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَـٰبَ مِنۢ بَعْدِ مَآ أَهْلَكْنَا ٱلْقُرُونَ ٱلْأُولَىٰ بَصَآئِرَ لِلنَّاسِ وَهُدًى وَرَحْمَةً لَّعَلَّهُمْ يَتَذَكَّرُونَُ"
    preprocessor = Preprocessor()
    print(preprocessor.preprocess_sentence(s))
