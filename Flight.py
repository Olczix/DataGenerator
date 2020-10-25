class Flight:
    def __init__(self, flight_id, airline, departure, destination, departure_time, destination_time, price):
        self.flight_id = flight_id
        self.airline = airline
        self.departure = departure
        self.departure_time = departure_time
        self.destination = destination
        self.destination_time = destination_time
        self.price = price

    def csv_format(self):
        string = f'{self.flight_id},{self.airline},{self.departure},{self.departure_time},' \
                 f'{self.destination},{self.destination_time},{self.price}'
        return string

    def get_id(self):
        return self.flight_id

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price
