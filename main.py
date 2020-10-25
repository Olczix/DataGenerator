from faker import Faker
from Airline import Airline
from Worker import Worker
from Location import Location
from Flight import Flight
import random
from datetime import datetime, timedelta

faker = Faker()
airlines = []
flights = []
attraction_packs = []
locations = []
hotels = []
offers = []
workers_personal_data = []
work_efficiency_data = []


def generate_workers_personal_data(file_name, number_of_people):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, number_of_people+1):
            name = faker.name_male() if i % 3 == 1 else faker.name_female()
            name, surname = name.split(' ', 1)
            birth_date = str(faker.date_of_birth())
            email = faker.email()
            phone = faker.numerify('+48 ### ### ###')
            hire_date = str(faker.date_this_century())

            worker = Worker(i, name, surname, birth_date, email, phone, hire_date)
            workers_personal_data.append(worker)

            file.write(worker.csv_format()+'\n')


def generate_work_efficiency_data(file_name):
    print('ok')


def generate_airlines(file_name, number_of_airlines):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_airlines):
            name = faker.last_name() + ' Airline'
            rating = random.randint(100, 500)/100
            plane_name = faker.word() + 'Jet'
            max_passengers_number = faker.random_int(200, 400)

            airline = Airline(name, rating, plane_name, max_passengers_number)
            airlines.append(airline)

            file.write(airline.csv_format()+'\n')


def generate_locations(file_name, number_of_locations):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_locations):
            location_id = i+1
            country = faker.country()
            city = faker.word() + ' City'
            # city = faker.city()
            population = faker.random_int(40000, 98829389)

            location = Location(location_id, country, city, population)
            locations.append(location)

            file.write(location.csv_format() + '\n')


def generate_flights(file_name, number_of_flights):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_flights):
            flight_id = i+1
            airline = random.choice(airlines).get_name()
            departure = random.choice(locations).get_location()
            destination = random.choice(locations).get_location()

            if destination == departure:
                destination = random.choice(locations).get_location()

            departure_time = faker.date_time_this_century()
            destination_time = departure_time + timedelta(hours=random.randint(2, 15))
            price = random.randint(100, 2000)

            flight = Flight(flight_id, airline, departure, departure_time, destination, destination_time, price)
            flights.append(flight)

            file.write(flight.csv_format() + '\n')


if __name__ == '__main__':
    generate_airlines('Data/airlines.csv', 3)
    generate_workers_personal_data('Data/workers_data.csv', 10)
    generate_work_efficiency_data('Data/work_efficiency_data.txt')
    generate_locations('Data/locations.csv', 10)
    generate_flights('Data/flights.csv', 5)
