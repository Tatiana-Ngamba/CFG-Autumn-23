/*
Section 4: SQL Challenge [25 marks]
In this section you will be fleshing out a database and performing queries.
*/
-- Creating a database
CREATE DATABASE foundation_exam;
-- Using the database
USE foundation_exam;

-- creating table 1
CREATE TABLE Movie_info (
Movie_ID INTEGER NOT NULL PRIMARY KEY,
Movie_Name VARCHAR(100),
Movie_Length TIME,
Age_Rating VARCHAR(5)
);

-- creating table 2
CREATE TABLE Screens (
screen_ID INTEGER NOT NULL PRIMARY KEY,
Four_K BOOLEAN
);

-- creating table 3
CREATE TABLE Showings (
Showing_ID INTEGER NOT NULL PRIMARY KEY,
Movie_ID INTEGER,
Screen_ID INTEGER,
Start_Time TIME,
Available_Seats INTEGER,
UNIQUE KEY (Movie_ID,Screen_ID,Start_Time)
);

--  table 1 - Inserting data values for each column

INSERT INTO movie_info
(movie_ID, movie_name, movie_length, age_rating)
 VALUES
 (1, "The Movie", "2:19:00", "12A"),
 (2, "The Other Movie", "1:30:00", "15"),
 (3, "The 3D Amazing Movie",  "1:42:00", "PG"),
 (4, "La Allure", "1:09:00", "18"),
 (5, "The Cartoon", "1:15:00", "U"),
 (6, "The Scary Cartoon", "1:23:00", "PG"),
 (7, "The Coming Of Age", "1:40:00", "12A"),
 (8, "The War", "2:07:00", "15"),
 (9, "The Murder Mystery", "1:47:00", "15");

SELECT * FROM  Movie_info;

--  table 2 - Inserting data values for each column
 INSERT INTO screens(screen_ID, four_k)
 VALUES
  (1, True),
  (2, False),
  (3, True),
  (4, True),
  (5, True),
  (6, True),
  (7, True),
  (8, False),
  (9, True),
  (10, True);

SELECT * FROM  Screens;

--  table 3 - Inserting data values for each column
INSERT INTO Showings
(showing_ID, movie_ID,screen_ID, start_time, available_seats)
 VALUES
  (1, 1, 2, '12:00:00', 10),
  (2, 1, 2, '17:00:00', 23),
  (3, 2, 9, '10:30:00', 30),
  (4, 3, 1, '07:00:00', 38),
  (5, 3, 5, '10:00:00', 26),
  (6, 3, 1, '17:00:00', 5),
  (7, 3, 1, '19:00:00', 0),
  (8, 3, 5, '14:00:00', 2),
  (9, 4, 9, '20:00:00', 14),
  (10, 4, 9, '23:00:00', 23),
  (11, 5, 6, '09:30:00', 30),
  (12, 5, 6, '12:30:00', 7),
  (13, 5, 6, '14:30:00', 0),
  (14, 5, 6, '15:20:00', 0),
  (15, 6, 10, '10:00:00', 32),
  (16, 6, 10, '13:30:00', 25),
  (17, 6, 10, '17:00:00', 14),
  (18, 7, 7, '12:00:00', 36),
  (19, 8, 4, '15:00:00', 24),
  (20, 9, 3, '17:00:00', 0);

SELECT * FROM Showings;

/* 4.2 Write a query to return the name and time of all movies that play after
12:00 given there is at least 1 available seat. Display the results in time order.6 marks */

SELECT M.Movie_Name,S.Start_Time
FROM Movie_info AS M
RIGHT JOIN Showings AS S
ON M.Movie_ID = S.Movie_ID
WHERE S.Start_time > '12:00:00' AND S.Available_Seats > 0
ORDER BY S.Start_time;


/*  4.3 Return the name of the movie with the most showings.  9 marks */

SELECT M.Movie_Name
FROM Movie_info AS M
LEFT JOIN Showings S ON M.movie_id = S.movie_id
GROUP BY m.movie_name
ORDER BY COUNT(s.showing_id) DESC
LIMIT 1;




