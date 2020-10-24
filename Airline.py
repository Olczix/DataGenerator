class Airline:
    def __init__(self, name, rating, plane_name, max_passengers_number):
        self.name = name
        self.rating = rating,
        self.plane_name = plane_name
        self.max_passengers_number = max_passengers_number

    def csv_format(self):
        string = f'{self.name},{self.rating},{self.plane_name},{self.max_passengers_number}'
        return string
