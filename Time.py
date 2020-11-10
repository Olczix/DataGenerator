class Time:
    def __init__(self, id, time, hour, minute, seconds):
        self.id = id
        self.time = time
        self.hour = hour
        self.minute = minute
        self.seconds = seconds

    def csv_format(self):
        string = f'{self.id},{self.time},{self.hour},{self.minute},{self.seconds}'
        return string

    def get_id(self):
        return self.id
