
/* 1. Ile œrednio czasu zajmuje pracownikom zarezerwowanie samolotu? */
SELECT AVG(FlightTimeReservation) as AvgTime
FROM TimeEfficiency


/* 2. Kto tworzy najlepiej oceniane oferty?  */
SELECT TOP 1  W.Name, W.Surname, AVG(O.OverallRating) AS AvgOfferRating
FROM Workers W
INNER JOIN TimeEfficiency TE ON TE.PersonId = W.PersonId
INNER JOIN Offers O ON O.OfferId = TE.OfferId
GROUP BY W.PersonId, W.Name, W.Surname
ORDER BY 3 DESC


/* 3. Kto przeprowadza najd³u¿sze rozmowy z hotelami? */
SELECT TOP 1 Name, Surname, AVG(HotelTimeReservation) as AvgTime
FROM TimeEfficiency TE
INNER JOIN Workers W on W.PersonId = TE.PersonId
GROUP BY W.PersonId, W.Name, W.Surname 
ORDER BY 3 DESC


/* 4. Kto jest w stanie wynegocjowaæ œredni¹ najwiêksz¹ zni¿kê za hotel? */
SELECT TOP 1 Name, Surname, AVG(HotelNegociatedBargain) as AvgBargain
FROM TimeEfficiency TE
INNER JOIN Workers W on W.PersonId = TE.PersonId
GROUP BY W.PersonId, W.Name, W.Surname 
ORDER BY 3 DESC


/* 5. Jaka jest liczba ofert tworzonych d³u¿ej ni¿ godzinê oraz ocenionych na wiêcej ni¿ 4 gwiazdki porównuj¹c miesi¹c bie¿¹cy oraz poprzedni? */
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



/* 6. Czy oferty, których czas rezerwacji hotelu by³ d³u¿szy ni¿ 15 minut, maj¹ wy¿sze oceny hoteli ni¿ te oferty, których czas rezerwacji by³ mniejszy ni¿ 15 minut? */
SELECT AVG(O.HotelRating) AS AvgHotelRatingAbove15mins
FROM TimeEfficiency TE
INNER JOIN Offers O ON O.OfferId = TE.OfferId
WHERE FlightTimeReservation > 15 

SELECT AVG(O.HotelRating) AS AvgHotelRatingUnder15mins
FROM TimeEfficiency TE
INNER JOIN Offers O ON O.OfferId = TE.OfferId
WHERE FlightTimeReservation < 15 


/* 7. Jakim zainteresowaniem cieszy³y siê w poprzednim roku 3 najni¿ej ocenione oferty w tym roku? */
/*SELECT TOP 3 Participants, MaxPatricipiantsNumber
FROM Offers O
INNER JOIN Flights F on O.FlightId = F.FlightId
WHERE F.DepartureTime > GETDATE() - 365
ORDER BY  O.OverallRating ASC*/


/* Jak doœwiadczenie pracownika przek³ada siê na efektywnoœæ/szybkoœæ jego pracy? */
