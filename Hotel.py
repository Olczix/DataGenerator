class Hotel:
    def __init__(self, hotel_id, name, location_id, stars):
        self.hotel_id = hotel_id
        self.name = name
        self.location_id = location_id
        self.stars = stars

    def csv_format(self):
        string = f'{self.hotel_id},{self.name},{self.location_id},{self.stars}'
        return string

    def get_id(self):
        return self.hotel_id
