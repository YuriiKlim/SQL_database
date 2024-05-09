-- ВИВЕСТИ МІНІМАЛЬНИЙ ВІК
SELECT MIN(AGE)
FROM STUDENT;

-- -- ВИВЕСТИ ІНФОРМАЦІЮ ПРО СТУДЕНТА З ВІК ЯКОГО МІНІМАЛЬНИЙ
SELECT *
FROM STUDENT
WHERE AGE = (SELECT MIN(AGE)
			 FROM STUDENT
          );


-- ВИВЕСТИ іНФОРМАЦІЮ ПРО СТУДЕНТІВ ВІК ЯКИХ БІЛЬШЕ СЕРЕДНЬОГО
SELECT *
FROM STUDENT
WHERE AGE > (SELECT AVG(AGE)
			 FROM STUDENT
			)
