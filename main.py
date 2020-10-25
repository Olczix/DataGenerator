from faker import Faker
from Airline import Airline
from Worker import Worker
from Location import Location
from Flight import Flight
from Hotel import Hotel
from AttractionPack import AttractionPack
from Offer import Offer
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


def generate_hotels_data(file_name, number_of_hotels):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_hotels):
            hotel_id = i+1
            name = faker.word().capitalize() + ' Hotel'
            location_id = random.choice(locations).get_id()
            stars = random.randint(1, 5)

            hotel = Hotel(hotel_id, name, location_id, stars)
            hotels.append(hotel)

            file.write(hotel.csv_format() + '\n')


def generate_attraction_packs_data(file_name, number_of_attraction_packs):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_attraction_packs):
            attraction_pack_id = i+1
            name = faker.word().capitalize() + ' Pack'
            description = faker.words(5)
            price = random.randint(100, 1000)

            attraction_pack = AttractionPack(attraction_pack_id, name, description, price)
            attraction_packs.append(attraction_pack)

            file.write(attraction_pack.csv_format() + '\n')


def generate_offers_data(file_name, number_of_offers):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_offers):
            offer_id = i + 1
            hotel_id = random.choice(hotels).get_id()
            flight_id = random.choice(flights).get_id()
            attraction_pack_id = random.choice(attraction_packs).get_id()
            max_participants_number = random.randint(50, 150)
            participants = random.randint(1, max_participants_number)
            hotel_price = random.randint(1000, 5000)
            hotel_rating = round(random.uniform(1.0, 5.0), 2)
            flight_rating = round(random.uniform(1.0, 5.0), 2)
            attraction_pack_rating = round(random.uniform(1.0, 5.0), 2)
            overall_rating = round((hotel_rating+flight_rating+attraction_pack_rating)/3.0, 2)

            offer = Offer(offer_id, hotel_id, flight_id, attraction_pack_id, max_participants_number,
                          participants, overall_rating, hotel_price, hotel_rating, flight_rating, attraction_pack_rating)
            offers.append(offer)

            file.write(offer.csv_format() + '\n')


def generate_work_efficiency_data(file_name):
    print('ok')


if __name__ == '__main__':
    generate_airlines('Data/airlines.csv', 3)
    generate_workers_personal_data('Data/workers_data.csv', 10)
    generate_locations('Data/locations.csv', 10)
    generate_flights('Data/flights.csv', 5)
    generate_hotels_data('Data/hotels_data.csv', 10)
    generate_attraction_packs_data('Data/attraction_packs_data.csv', 5)
    generate_offers_data('Data/offers_data.csv', 50)

    generate_work_efficiency_data('Data/work_efficiency_data.txt')



