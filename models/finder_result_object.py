class FinderResultObject:
    def __init__(self, spans, total_number_of_matches, number_of_surahs, total_number_of_verses, paths:dict|None=None):
        self.spans = spans
        self.total_number_of_matches = total_number_of_matches
        self.number_of_surahs = number_of_surahs
        self.total_number_of_verses = total_number_of_verses
        self.paths = paths if paths else {}
