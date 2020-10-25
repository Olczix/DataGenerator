class Airline:
    def __init__(self, id, name, rating, plane_name, max_passengers_number):
        self.id = id
        self.name = name
        self.rating = rating
        self.plane_name = plane_name
        self.max_passengers_number = max_passengers_number

    def csv_format(self):
        string = f'{self.id},{self.name},{self.rating},{self.plane_name},{self.max_passengers_number}'
        return string

    def get_id(self):
        return self.id

    def set_max_passengers_number(self, number):
        self.max_passengers_number = number
