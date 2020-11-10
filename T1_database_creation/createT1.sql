CREATE TABLE Dates
(
	DateId INTEGER PRIMARY KEY,
	DateValue DATE,
	DateYear varchar(4),
	DateMonth varchar(2),
	DateDay varchar(2)
)

CREATE TABLE Times
(
	TimeId INTEGER PRIMARY KEY,
	TimeValue varchar(8),
	TimeHour varchar(2),
	TimeMinute varchar(2),
	TimeSecond varchar(2)
)

CREATE TABLE Airlines 
(
	AirlineId integer PRIMARY KEY,
    Name nvarchar(50), 
    Rating varchar(5),
    PlaneName varchar(40),
    MaxPassengersNumber varchar(25)
)

CREATE TABLE AttractionPacks
(
    AttractionPackId INTEGER PRIMARY KEY,
    Name varchar(30),
    Description varchar(200)
)

CREATE TABLE Locations
(
    LocationId INTEGER PRIMARY KEY,
    Country varchar(70),
    City varchar(50),
    Population varchar(30)
)

CREATE TABLE Hotels
(
    HotelId INTEGER PRIMARY KEY,
    Name varchar(50),
    LocationId INTEGER FOREIGN KEY REFERENCES Locations,
    Stars INTEGER
)

CREATE TABLE Flights
(
    FlightId INTEGER PRIMARY KEY,
    Airline INTEGER FOREIGN KEY REFERENCES Airlines,
    Departure integer FOREIGN KEY REFERENCES Locations,
	Destination integer FOREIGN KEY REFERENCES Locations,
    DepartureDate INTEGER FOREIGN KEY REFERENCES Dates,
    DepartureTime INTEGER FOREIGN KEY REFERENCES Times
)

CREATE TABLE Offers
(
    OfferId INTEGER PRIMARY KEY,
    HotelId INTEGER FOREIGN KEY REFERENCES Hotels,
    FlightId INTEGER FOREIGN KEY REFERENCES Flights,
    AttractionPackId INTEGER FOREIGN KEY REFERENCES AttractionPacks,
    MaxPatricipiantsNumber INTEGER,
	Participants INTEGER,
    OverallRating FLOAT,
    HotelPrice varchar(25),
    HotelRating  FLOAT,
	FlightPrice varchar(25),
    FlightRating FLOAT,
	AttractionPackPrice varchar(25),
    AttractionPackRating  FLOAT
)

CREATE TABLE Workers
(
    PersonId INTEGER PRIMARY KEY,
    Name varchar(50),
	Surname varchar(50),
    Age varchar(25),
    Email varchar(50),
    PhoneNumber varchar(9),
    WorkExperience varchar(30)
)

CREATE TABLE TimeEfficiency
(
	OfferId INTEGER FOREIGN KEY REFERENCES Offers,
	PersonId INTEGER FOREIGN KEY REFERENCES Workers,
	HotelTimeReservation INTEGER,
	FlightTimeReservation INTEGER,
	AttractionPackTimeReservation INTEGER,
	VaccinesTimeReservation INTEGER,
	AdditionalDocsTimeReservation INTEGER,
	HotelNegociatedBargain INTEGER,
	TimeSum INTEGER,
	CreationDate INTEGER FOREIGN KEY REFERENCES Dates,
	CreationTime INTEGER FOREIGN KEY REFERENCES Times
)


