-- 1. Вивести таблицю кафедр, але розташувати її поля у зворотному порядку.
SELECT NAME, FINANCING::NUMERIC::FLOAT8, 
ID FROM DEPARTMENTS;

-- 2. Вивести назви груп та їх рейтинги з уточненнями до назв
-- полів відповідно до назви таблиці.
SELECT NAME AS "Groups.Name", 
RATING AS "Groups.Rating" FROM GROUPS;

-- 3. Вивести для викладачів їх прізвища, відсоток ставки по
-- відношенню до надбавки та відсоток ставки по відношенню до зарплати (сума ставки та надбавки).
SELECT SURNAME,
       (SALARY / PREMIUM * 100) 
	   AS "Salary to Premium Percentage",
       (SALARY / (SALARY + PREMIUM) * 100) 
	   AS "Salary to Total Percentage"
FROM TEACHERS;

-- 4. Вивести таблицю факультетів одним полем у такому форматі: «The dean of faculty [faculty] is [dean].».
SELECT CONCAT('The dean of faculty ', 
			  NAME, ' is ', DEAN, '.') 
			  AS "Faculty Information" 
			  FROM FACULTIES;

-- 5. Вивести прізвища професорів, ставка яких перевищує 1050.
SELECT SURNAME 
FROM TEACHERS 
WHERE ISPROFESSOR = B'1' AND SALARY::NUMERIC > 1050;

-- 6. Вивести назви кафедр, фонд фінансування яких менший,
-- ніж 11000 або більший за 25000.
SELECT NAME 
FROM DEPARTMENTS 
WHERE FINANCING::NUMERIC < 11000 OR FINANCING::NUMERIC > 25000;

-- 7. Вивести назви факультетів, окрім факультету «Computer
-- Science».
SELECT NAME 
FROM FACULTIES 
WHERE NAME <> 'Faculty of Computer Science';

-- 8. Вивести прізвища та посади викладачів, які не є професорами.
SELECT SURNAME, POSITION 
FROM TEACHERS 
WHERE ISPROFESSOR = B'0';

-- 9. Вивести прізвища, посади, ставки та надбавки асистентів,
-- надбавка яких у діапазоні від 160 до 550.
SELECT SURNAME, POSITION, SALARY, PREMIUM 
FROM TEACHERS 
WHERE ISASSISTANT = B'1' AND PREMIUM::NUMERIC BETWEEN 160 AND 550;

-- 10. Вивести прізвища та ставки асистентів.
SELECT SURNAME, SALARY 
FROM TEACHERS 
WHERE ISASSISTANT = B'1';

-- 11. Вивести прізвища та посади викладачів, які були прийняті
-- на роботу до 01.01.2000.
SELECT SURNAME, POSITION 
FROM TEACHERS 
WHERE EMPLOYMENTDATE < '2000-01-01';

-- 12. Вивести назви кафедр, які в алфавітному порядку розміщені до кафедри «Software Development». Виведене поле
-- назвіть «Name of Department».
SELECT NAME AS "Name of Department" 
FROM DEPARTMENTS 
WHERE NAME < 'Software Development' ORDER BY NAME;

-- 13. Вивести прізвища асистентів із зарплатою (сума ставки
-- та надбавки) не більше 1200.
SELECT SURNAME 
FROM TEACHERS 
WHERE ISASSISTANT = B'1' AND (SALARY + PREMIUM)::NUMERIC <= 4000;

-- 14. Вивести назви груп 5-го курсу з рейтингом у діапазоні
-- від 2 до 4.
SELECT NAME 
FROM GROUPS
WHERE YEAR = 5 AND RATING BETWEEN 2 AND 4;

-- 15. Вивести прізвища асистентів зі ставкою менше, ніж 550
-- або надбавкою менше, ніж 200.
SELECT SURNAME 
FROM TEACHERS 
WHERE ISASSISTANT = B'1' AND (SALARY::NUMERIC < 3550 
							  OR PREMIUM::NUMERIC < 200);
