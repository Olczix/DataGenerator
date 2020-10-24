import csv


class Worker:
    def __init__(self, person_id, name, surname, birth_date, email, phone_number, hire_date):
        self.person_id = person_id
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.email = email
        self.phone_number = phone_number
        self.hire_date = hire_date

    def print(self):
        print('Name: ' + self.name)
        print('Surname: ' + self.surname)
        print('Date of birth: ' + str(self.birth_date))
        print('Email: ' + str(self.email))
        print('Phone number: ' + str(self.phone_number))
        print('Hire date: ' + str(self.hire_date))
        print()

    def json_string_format(self):
        data_string = {}
        data_string['person_id'] = str(self.person_id)
        data_string['name'] = self.name
        data_string['surname'] = self.surname
        data_string['birth_date'] = self.birth_date
        data_string['email'] = self.email
        data_string['phone_number'] = self.phone_number
        data_string['hire_date'] = self.hire_date

        print(data_string)
        return data_string

    def csv_format(self):
        string = f'{self.person_id},{self.name},{self.surname},{self.birth_date},{self.email},' \
                 f'{self.phone_number},' f'{self.hire_date}'
        return string
