import csv


class Worker:
    def __init__(self, person_id, name, surname, age, email, phone_number, work_experience):
        self.person_id = person_id
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.phone_number = phone_number
        self.work_experience = work_experience

    def print(self):
        print('Name: ' + self.name)
        print('Surname: ' + self.surname)
        print('Date of birth: ' + str(self.age))
        print('Email: ' + str(self.email))
        print('Phone number: ' + str(self.phone_number))
        print('Hire date: ' + str(self.work_experience))
        print()

    def csv_format(self):
        string = f'{self.person_id},{self.name},{self.surname},{self.age},{self.email},' \
                 f'{self.phone_number},' f'{self.work_experience}'
        return string

    def get_id(self):
        return self.person_id

    def set_phone(self, phone):
        self.phone_number = phone
