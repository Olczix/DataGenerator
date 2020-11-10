from faker import Faker
from Date import Date
from Time import Time
from Airline import Airline
from Worker import Worker
from Location import Location
from Flight import Flight
from Hotel import Hotel
from AttractionPack import AttractionPack
from Offer import Offer
import random
from datetime import datetime, timedelta

number_of_dates = 500
number_of_times = 200
number_of_hotels = 8500
number_of_workers = 5000
number_of_airlines = 100
number_of_locations = 2000
number_of_flights = 20000
number_of_attraction_packs = 20
number_of_offers = 150000

faker = Faker()
airlines = []
flights = []
attraction_packs = []
locations = []
hotels = []
offers = []
workers = []
work_efficiency_data = []
dates = []
times = []

work_experience_categories = ['under 1 year', 'between 1 year and 5 years', 'above 5 years']
age_categories = ['under 20', 'between 21 and 30', 'between 31 and 40', 'between 41 and 50', 'above 50']
max_passenger_number_categories = ['under 100', 'between 101 and 250', 'between 251 and 500', 'above 500']
population_categories = ['under 100 000', 'between 100 000 and 500 000', 'above 500 000']
prices = ['under 100PLN', 'between 100PLN and 250PLN', 'between 250PLN and 500PLN', 'above 500PLN']


def generate_dates(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, number_of_dates):
            date = faker.date_this_century()
            year = str(date)[:4]
            month = str(date)[5:-3]
            day = str(date)[-2:]

            date = Date(i, date, year, month, day)
            dates.append(date)

            file.write(date.csv_format())
            if i != number_of_dates:
                file.write('\n')


def generate_times(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, number_of_times):
            time = faker.time()
            hour = str(time)[:2]
            minute = str(time)[3:-3]
            seconds = str(time)[-2:]

            time = Time(i, time, hour, minute, seconds)
            times.append(time)

            file.write(time.csv_format())
            if i != number_of_times:
                file.write('\n')


def generate_workers_personal_data(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, number_of_workers+1):
            name = faker.name_male() if i % 3 == 0 else faker.name_female()
            name, surname = name.split(' ', 1)
            birth_date = random.choice(age_categories)
            email = faker.email()
            phone = faker.numerify('#########')
            work_experience = random.choice(work_experience_categories)

            worker = Worker(i, name, surname, birth_date, email, phone, work_experience)
            workers.append(worker)

            file.write(worker.csv_format())
            if i != number_of_workers:
                file.write('\n')


def generate_workers_personal_data_t2(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, number_of_workers+1):
            if i % 15 == 0:
                workers[i].set_phone(faker.numerify('#########'))
            file.write(workers[i-1].csv_format()+'\n')

        for i in range(1, int(number_of_workers/10)):
            name = faker.name_male() if i % 3 == 0 else faker.name_female()
            name, surname = name.split(' ', 1)
            age = random.choice(age_categories)
            email = faker.email()
            phone = faker.numerify('#########')
            work_experience = random.choice(work_experience_categories)

            worker = Worker(number_of_workers+i, name, surname, age, email, phone, work_experience)
            workers.append(worker)

            file.write(worker.csv_format())
            if i != int(number_of_workers/10):
                file.write('\n')


def generate_airlines(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_airlines):
            airline_id = i+1
            name = faker.last_name() + ' Airline'
            rating = random.randint(100, 500)/100
            plane_name = faker.word() + 'Jet'
            max_passengers_number = random.choice(max_passenger_number_categories)

            airline = Airline(airline_id, name, rating, plane_name, max_passengers_number)
            airlines.append(airline)

            file.write(airline.csv_format())
            if i != number_of_airlines-1:
                file.write('\n')


def generate_airlines_t2(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_airlines):
            if i % 5 == 0:
                max_passengers_number = random.choice(max_passenger_number_categories)
                airlines[i].set_max_passengers_number(max_passengers_number)
            file.write(airlines[i].csv_format()+'\n')

        for i in range(0, int(number_of_airlines/4)):
            airline_id = number_of_airlines + i + 1
            name = faker.last_name() + ' Airline'
            rating = random.randint(100, 500)/100
            plane_name = faker.word() + 'Jet'
            max_passengers_number = random.choice(max_passenger_number_categories)

            airline = Airline(airline_id, name, rating, plane_name, max_passengers_number)
            airlines.append(airline)

            file.write(airline.csv_format())
            if i != int(number_of_airlines/4)-1:
                file.write('\n')


def generate_locations(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_locations):
            location_id = i+1
            country = faker.country()
            city = faker.word().capitalize() + ' City'
            population = random.choice(population_categories)

            location = Location(location_id, country, city, population)
            locations.append(location)

            file.write(location.csv_format())
            if i != number_of_locations-1:
                file.write('\n')


def generate_locations_t2(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_locations):
            if i % 5 == 0:
                locations[i].set_population(random.choice(population_categories))
            file.write(locations[i].csv_format()+'\n')

        for i in range(0, int(number_of_locations/10)):
            location_id = number_of_locations+i+1
            country = faker.country()
            city = faker.word().capitalize() + ' City'
            # city = faker.city()
            population = faker.random_int(40000, 98829389)

            location = Location(location_id, country, city, population)
            locations.append(location)

            file.write(location.csv_format())
            if i != int(number_of_locations/10)-1:
                file.write('\n')


def generate_flights(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_flights):
            flight_id = i+1
            airline = random.choice(airlines).get_id()
            departure = random.choice(locations).get_id()
            destination = random.choice(locations).get_id()

            if destination == departure:
                destination = random.choice(locations).get_id()

            departure_date = random.choice(dates).get_id()
            departure_time = random.choice(times).get_id()

            flight = Flight(flight_id, airline, departure, destination, departure_date, departure_time)
            flights.append(flight)

            file.write(flight.csv_format())
            if i != number_of_flights-1:
                file.write('\n')


def generate_flights_t2(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_flights):
            if i % 10 == 0:
                flights[i].set_time(random.choice(times).get_id())
            file.write(flights[i].csv_format()+'\n')

        for i in range(0, int(number_of_flights/10)):
            flight_id = number_of_flights+i+1
            airline = random.choice(airlines).get_id()
            departure = random.choice(locations).get_id()
            destination = random.choice(locations).get_id()

            if destination == departure:
                destination = random.choice(locations).get_id()

            departure_date = random.choice(dates).get_id()
            departure_time = random.choice(times).get_id()

            flight = Flight(flight_id, airline, departure, destination, departure_date, departure_time)
            flights.append(flight)

            file.write(flight.csv_format())
            if i != number_of_flights-1:
                file.write('\n')


def generate_hotels_data(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_hotels):
            hotel_id = i+1
            name = faker.word().capitalize() + ' Hotel'
            location_id = random.choice(locations).get_id()
            stars = random.randint(1, 5)

            hotel = Hotel(hotel_id, name, location_id, stars)
            hotels.append(hotel)

            file.write(hotel.csv_format())
            if i != number_of_hotels-1:
                file.write('\n')


def generate_hotels_data_t2(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_hotels):
            if i % 5 == 0:
                hotels[i].set_stars(random.randint(1,5))
            file.write(hotels[i].csv_format()+'\n')

        for i in range(0, int(number_of_hotels/20)):
            hotel_id = number_of_hotels+i+1
            name = faker.word().capitalize() + ' Hotel'
            location_id = random.choice(locations).get_id()
            stars = random.randint(1, 5)

            hotel = Hotel(hotel_id, name, location_id, stars)
            hotels.append(hotel)

            file.write(hotel.csv_format())
            if i != int(number_of_hotels/20)-1:
                file.write('\n')


def generate_attraction_packs_data(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_attraction_packs):
            attraction_pack_id = i+1
            name = faker.word().capitalize() + ' Pack'
            description = ''
            for j in range(0, 5):
                description = description + faker.word()
                if j != 4:
                    description += ' '

            attraction_pack = AttractionPack(attraction_pack_id, name, description)
            attraction_packs.append(attraction_pack)

            file.write(attraction_pack.csv_format())
            if i != number_of_attraction_packs-1:
                file.write('\n')


def generate_attraction_packs_data_t2(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_attraction_packs):
            if i % 5 == 0:
                attraction_packs[i].set_name(faker.word().capitalize() + ' Pack')
            file.write(attraction_packs[i].csv_format()+'\n')

        for i in range(0, int(number_of_attraction_packs/10)):
            attraction_pack_id = number_of_attraction_packs+i+1
            name = faker.word().capitalize() + ' Pack'
            description = ''
            for j in range(0, 5):
                description = description + faker.word()
                if j != 4:
                    description += ' '

            attraction_pack = AttractionPack(attraction_pack_id, name, description)
            attraction_packs.append(attraction_pack)

            file.write(attraction_pack.csv_format())
            if i != int(number_of_attraction_packs/10)-1:
                file.write('\n')


def generate_offers_data(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_offers):
            offer_id = i + 1
            hotel_id = random.choice(hotels).get_id()
            flight_id = random.choice(flights).get_id()
            attraction_pack_id = random.choice(attraction_packs).get_id()
            max_participants_number = random.randint(50, 150)
            participants = random.randint(1, max_participants_number)
            hotel_price = random.choice(prices)
            hotel_rating = round(random.uniform(1.0, 5.0), 2)
            flight_price = random.choice(prices)
            flight_rating = round(random.uniform(1.0, 5.0), 2)
            attraction_pack_price = random.choice(prices)
            attraction_pack_rating = round(random.uniform(1.0, 5.0), 2)
            overall_rating = round((hotel_rating+flight_rating+attraction_pack_rating)/3.0, 2)

            offer = Offer(offer_id, hotel_id, flight_id, attraction_pack_id, max_participants_number,
                          participants, overall_rating, hotel_price, hotel_rating, flight_price, flight_rating,
                          attraction_pack_price, attraction_pack_rating)
            offers.append(offer)

            file.write(offer.csv_format())
            if i != number_of_offers-1:
                file.write('\n')


def generate_offers_data_t2(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_offers):
            if i % 10 == 0:
                offers[i].set_participants(offers[i].get_participants()+random.randint(1, 10))
            file.write(offers[i].csv_format()+'\n')

        for i in range(0, int(number_of_offers/10)):
            offer_id = number_of_offers + i + 1
            hotel_id = random.choice(hotels).get_id()
            flight_id = random.choice(flights).get_id()
            attraction_pack_id = random.choice(attraction_packs).get_id()
            max_participants_number = random.randint(50, 150)
            participants = random.randint(1, max_participants_number)
            hotel_price = random.choice(prices)
            hotel_rating = round(random.uniform(1.0, 5.0), 2)
            flight_price = random.choice(prices)
            flight_rating = round(random.uniform(1.0, 5.0), 2)
            attraction_pack_price = random.choice(prices)
            attraction_pack_rating = round(random.uniform(1.0, 5.0), 2)
            overall_rating = round((hotel_rating + flight_rating + attraction_pack_rating) / 3.0, 2)

            offer = Offer(offer_id, hotel_id, flight_id, attraction_pack_id, max_participants_number,
                          participants, overall_rating, hotel_price, hotel_rating, flight_price, flight_rating,
                          attraction_pack_price, attraction_pack_rating)
            offers.append(offer)

            file.write(offer.csv_format())
            if i != int(number_of_offers/10)-1:
                file.write('\n')


def generate_work_efficiency_data(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(0, number_of_offers):
            string = ''
            string += str(i+1) + ','
            string += str(random.choice(workers).get_id()) + ','
            hotel_time = random.randint(5, 60)
            flight_time = random.randint(5, 60)
            attraction_pack_time = random.randint(5, 60)
            additional_vaccinations_time = random.randint(5, 60)
            additional_docs = random.randint(5, 60)
            hotel_sale = random.randint(100, 500)
            time = hotel_time + flight_time + attraction_pack_time + additional_docs + additional_vaccinations_time
            string += str(hotel_time) + ','
            string += str(flight_time) + ','
            string += str(attraction_pack_time) + ','
            string += str(additional_vaccinations_time) + ','
            string += str(additional_docs) + ','
            string += str(hotel_sale)+','
            string += str(time) + ','
            string += str(random.choice(dates).get_id()) + ','
            string += str(random.choice(times).get_id())
            file.write(string)
            if i != number_of_offers - 1:
                file.write('\n')


if __name__ == '__main__':
    # data at T1
    generate_dates('Data/T1/dates_t1.bulk')
    generate_times('Data/T1/times_t1.bulk')
    generate_airlines('Data/T1/airlines_t1.bulk')
    generate_workers_personal_data('Data/T1/workers_data_t1.bulk')
    generate_locations('Data/T1/locations_t1.bulk')
    generate_flights('Data/T1/flights_t1.bulk')
    generate_hotels_data('Data/T1/hotels_data_t1.bulk')
    generate_attraction_packs_data('Data/T1/attraction_packs_data_t1.bulk')
    generate_offers_data('Data/T1/offers_data_t1.bulk')
    generate_work_efficiency_data('Data/T1/work_efficiency_data_t1.bulk')

    # data at T2
    generate_airlines_t2('Data/T2/airlines_t2.bulk')
    generate_workers_personal_data_t2('Data/T2/workers_data_t2.bulk')
    generate_locations_t2('Data/T2/locations_t2.bulk')
    generate_flights_t2('Data/T2/flights_t2.bulk')
    generate_hotels_data_t2('Data/T2/hotels_data_t2.bulk')
    generate_attraction_packs_data_t2('Data/T2/attraction_packs_data_t2.bulk')
    generate_offers_data_t2('Data/T2/offers_data_t2.bulk')
