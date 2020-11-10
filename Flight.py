class Flight:
    def __init__(self, flight_id, airline, departure, destination, departure_date, departure_time):
        self.flight_id = flight_id
        self.airline = airline
        self.departure = departure
        self.destination = destination
        self.departure_date = departure_date
        self.departure_time = departure_time

    def csv_format(self):
        string = f'{self.flight_id},{self.airline},{self.departure},{self.destination},{self.departure_date},' \
                 f'{self.departure_time}'
        return string

    def get_id(self):
        return self.flight_id

    def set_time(self, time):
        self.departure_time = time

