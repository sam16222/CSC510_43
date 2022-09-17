from col import Cols
from main import the
from misc import isfloat, coerce, csv, push
from row import Row

"""Class Data to add a 'Row' to 'data'"""
class Data(object):
    def __init__(self, src):
        """Contructor to initialize cols, rows and add the 'Row' to 'data'"""
        self.cols = None
        self.rows = []
        if isinstance(src, str):
            csv(src, self.add)
        else:
            for _, row in enumerate(src or []):
                self.add(row)

    def add(self, row):
        """Function to update 'cols' with the new values"""
        if not self.cols:
            self.cols = Cols(row)
        else:
            row = push(self.rows, Row(row))
            for _, todo in enumerate([self.cols.x, self.cols.y]):
                for _, col in enumerate(todo):
                    col.add(row.cells[col.at])

    def stats(self, places, show_cols, fun):
        """Function for show_cols (default = ''data.cols.x') in 'data',
            show 'fun' (default = 'mid'), rounding numbers to 'places' (default = 2)"""
        places, show_cols, fun = places or 2, show_cols or self.cols.x, fun or "mid"
        table = {}       
        for _, col in enumerate(show_cols):
            if fun == "mid":
                value = col.mid()
            else:
                value = col.div()
            value = round(value, places)
            table[col.name] = value
        return table