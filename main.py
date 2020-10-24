from faker import Faker
from Worker import Worker
import json
import os

faker = Faker()
people_personal_data = []
work_efficiency_data = []


def generate_workers_personal_data(file_name, number_of_people):
    #os.remove(file_name)
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, number_of_people+1):
            name = faker.name_male() if i % 3 == 1 else faker.name_female()
            name, surname = name.split(' ', 1)
            birth_date = str(faker.date_of_birth())
            email = faker.email()
            phone = faker.numerify('+48 ### ### ###')
            hire_date = str(faker.date_this_century())

            person = Worker(i, name, surname, birth_date, email, phone, hire_date)
            people_personal_data.append(person)

            json.dump(person.csv_format(), file, ensure_ascii=False)
            file.write('\n')


def generate_work_efficiency_data(file_name):
    print('ok')


if __name__ == '__main__':
    generate_workers_personal_data('workers_data.csv', 10)
    generate_work_efficiency_data('work_efficiency_data.txt')

