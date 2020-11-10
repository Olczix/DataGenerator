BULK INSERT Dates
FROM 'D:\Code\PythonProjects\untitled\Data\T1\dates_t1.bulk'
WITH(
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n'
)
BULK INSERT Times
FROM 'D:\Code\PythonProjects\untitled\Data\T1\times_t1.bulk'
WITH(
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n'
)

BULK INSERT Airlines
FROM 'D:\Code\PythonProjects\untitled\Data\T1\airlines_t1.bulk'
WITH(
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n'
)

BULK INSERT AttractionPacks
FROM 'D:\Code\PythonProjects\untitled\Data\T1\attraction_packs_data_t1.bulk'
WITH(
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n'
)

BULK INSERT Locations
FROM 'D:\Code\PythonProjects\untitled\Data\T1\locations_t1.bulk'
WITH(
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n'
)

BULK INSERT Hotels
FROM 'D:\Code\PythonProjects\untitled\Data\T1\hotels_data_t1.bulk'
WITH(
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n'
)

BULK INSERT Flights
FROM 'D:\Code\PythonProjects\untitled\Data\T1\flights_t1.bulk'
WITH(
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n'
)

BULK INSERT Offers
FROM 'D:\Code\PythonProjects\untitled\Data\T1\offers_data_t1.bulk'
WITH(
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n'
)

BULK INSERT Workers
FROM 'D:\Code\PythonProjects\untitled\Data\T1\workers_data_t1.bulk'
WITH(
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n'
)

BULK INSERT TimeEfficiency
FROM 'D:\Code\PythonProjects\untitled\Data\T1\work_efficiency_data_t1.bulk'
WITH(
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n'
)



