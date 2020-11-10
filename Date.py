class Date:
    def __init__(self, id, date, year, month, day):
        self.id = id
        self.date = date
        self.year = year
        self.month = month
        self.day = day

    def csv_format(self):
        string = f'{self.id},{self.date},{self.year},{self.month},{self.day}'
        return string

    def get_id(self):
        return self.id
