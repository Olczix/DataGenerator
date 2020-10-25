class Offer:
    def __init__(self, offer_id, hotel_id, flight_id, attraction_pack_id, max_participants_number,
                 participants, overall_rating, hotel_price, hotel_rating, flight_rating, attraction_pack_rating):
        self.offer_id = offer_id
        self.hotel_id = hotel_id
        self.flight_id = flight_id
        self.attraction_pack_id = attraction_pack_id
        self.max_participants_number = max_participants_number
        self.participants = participants
        self.overall_rating = overall_rating
        self.hotel_price = hotel_price
        self.hotel_rating = hotel_rating
        self.flight_rating = flight_rating
        self.attraction_pack_rating = attraction_pack_rating

    def csv_format(self):
        string = f'{self.offer_id},{self.hotel_id},{self.flight_id},{self.attraction_pack_id},' \
                 f'{self.max_participants_number},{self.participants},{self.overall_rating},' \
                 f'{self.hotel_price},{self.hotel_rating},{self.flight_rating},{self.attraction_pack_rating}'
        return string

    def get_id(self):
        return self.offer_id
