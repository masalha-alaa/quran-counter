import pandas as pd
from yaml import safe_load


class MyDataLoader:
    df = None
    _working_col = None

    def __init__(self):
        if MyDataLoader.df is None:
            config = safe_load(open("config.yml", mode='r'))
            MyDataLoader.df = pd.read_json(config['data']['path'])
            # TODO: save column in df beforehand
            verses_col = config['data']['verses_column']
            MyDataLoader._working_col = f"{verses_col}_split"
            MyDataLoader.df[MyDataLoader._working_col] = MyDataLoader.df[verses_col].str.split('\n')

    @staticmethod
    def get_verse(surah_num, verse_num):
        return MyDataLoader.df.loc[MyDataLoader.df['surah'] == int(surah_num), MyDataLoader._working_col].iloc[0][int(verse_num - 1)]

    @staticmethod
    def get_data():
        return MyDataLoader.df

    @staticmethod
    def get_working_col():
        return MyDataLoader._working_col
