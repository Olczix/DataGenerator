class AttractionPack:
    def __init__(self, attraction_pack_id, name, description):
        self.attraction_pack_id = attraction_pack_id
        self.name = name
        self.description = description

    def csv_format(self):
        string = f'{self.attraction_pack_id},{self.name},{self.description}'
        return string

    def get_id(self):
        return self.attraction_pack_id

    def set_name(self, name):
        self.name = name


