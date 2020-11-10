
/* 1. Ile �rednio czasu zajmuje pracownikom zarezerwowanie samolotu? */
SELECT AVG(FlightTimeReservation) as AvgTime
FROM TimeEfficiency


/* 2. Kto tworzy najlepiej oceniane oferty?  */
SELECT TOP 1  W.Name, W.Surname, AVG(O.OverallRating) AS AvgOfferRating
FROM Workers W
INNER JOIN TimeEfficiency TE ON TE.PersonId = W.PersonId
INNER JOIN Offers O ON O.OfferId = TE.OfferId
GROUP BY W.PersonId, W.Name, W.Surname
ORDER BY 3 DESC


/* 3. Kto przeprowadza najd�u�sze rozmowy z hotelami? */
SELECT TOP 1 Name, Surname, AVG(HotelTimeReservation) as AvgTime
FROM TimeEfficiency TE
INNER JOIN Workers W on W.PersonId = TE.PersonId
GROUP BY W.PersonId, W.Name, W.Surname 
ORDER BY 3 DESC


/* 4. Kto jest w stanie wynegocjowa� �redni� najwi�ksz� zni�k� za hotel? */
SELECT TOP 1 Name, Surname, AVG(HotelNegociatedBargain) as AvgBargain
FROM TimeEfficiency TE
INNER JOIN Workers W on W.PersonId = TE.PersonId
GROUP BY W.PersonId, W.Name, W.Surname 
ORDER BY 3 DESC


/* 5. Jaka jest liczba ofert tworzonych d�u�ej ni� godzin� oraz ocenionych na wi�cej ni� 4 gwiazdki por�wnuj�c miesi�c bie��cy oraz poprzedni? */
SELECT COUNT(O.OfferID) AS CurrentMonth
FROM TimeEfficiency TE
INNER JOIN Offers O ON O.OfferId = TE.OfferId
INNER JOIN Dates D ON D.DateId = TE.CreationDate
WHERE OverallRating > 4.0 AND TE.TimeSum > 60 AND D.DateValue > GETDATE() - 30

SELECT COUNT(O.OfferID) AS PreviousMonth
FROM TimeEfficiency TE
INNER JOIN Offers O ON O.OfferId = TE.OfferId
INNER JOIN Dates D ON D.DateId = TE.CreationDate
WHERE OverallRating > 4.0 AND TE.TimeSum > 60 AND D.DateValue > GETDATE() - 60 AND  D.DateValue < GETDATE() - 30



/* 6. Czy oferty, kt�rych czas rezerwacji hotelu by� d�u�szy ni� 15 minut, maj� wy�sze oceny hoteli ni� te oferty, kt�rych czas rezerwacji by� mniejszy ni� 15 minut? */
SELECT AVG(O.HotelRating) AS AvgHotelRatingAbove15mins
FROM TimeEfficiency TE
INNER JOIN Offers O ON O.OfferId = TE.OfferId
WHERE FlightTimeReservation > 15 

SELECT AVG(O.HotelRating) AS AvgHotelRatingUnder15mins
FROM TimeEfficiency TE
INNER JOIN Offers O ON O.OfferId = TE.OfferId
WHERE FlightTimeReservation < 15 


/* 7. Jakim zainteresowaniem cieszy�y si� w poprzednim roku 3 najni�ej ocenione oferty w tym roku? */
/*SELECT TOP 3 Participants, MaxPatricipiantsNumber
FROM Offers O
INNER JOIN Flights F on O.FlightId = F.FlightId
WHERE F.DepartureTime > GETDATE() - 365
ORDER BY  O.OverallRating ASC*/


/* Jak do�wiadczenie pracownika przek�ada si� na efektywno��/szybko�� jego pracy? */
