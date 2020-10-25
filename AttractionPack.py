class AttractionPack:
    def __init__(self, attraction_pack_id, name, description, price):
        self.attraction_pack_id = attraction_pack_id
        self.name = name
        self.description = description
        self.price = price

    def csv_format(self):
        string = f'{self.attraction_pack_id},{self.name},{self.description},{self.price}'
        return string

    def get_id(self):
        return self.attraction_pack_id
