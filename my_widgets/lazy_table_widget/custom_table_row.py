from .custom_table_widget_item import CustomTableWidgetItem


class CustomTableRow:
    def __init__(self, data:list, metadata=None):
        self.data = data
        self.metadata = metadata

    def __getitem__(self, index):
        return self.data[index]

    # def __lt__(self, other):
    #     pass

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)
