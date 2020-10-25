class Location:
    def __init__(self, location_id, country, city, population):
        self.location_id = location_id
        self.country = country
        self.city = city
        self.population = population

    def csv_format(self):
        string = f'{self.location_id},{self.country},{self.city},{self.population}'
        return string

    def get_location(self):
        return f'{self.country},{self.city}'

    def get_id(self):
        return f'{self.location_id}'
