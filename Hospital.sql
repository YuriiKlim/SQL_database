-- CREATE DATABASE HOSPITAL

-- 1. Вивести вміст таблиці палат.
-- SELECT * FROM WARDS

-- 2. Вивести прізвища та телефони усіх лікарів.
-- SELECT SURNAME, PHONE 
-- FROM DOCTORS

-- 3. Вивести усі поверхи без повторень, де розміщуються
-- палати.
-- SELECT DISTINCT FLOOR 
-- FROM WARDS

-- 4. Вивести назви захворювань під назвою « Name of
-- Disease» та ступінь їхньої тяжкості під назвою «Severity
-- of Disease».
-- SELECT NAME AS "NAME OF DISEASE", 
-- SEVERITY AS "SEVERITY OF DISEASE" FROM DISEASES

-- 5. Вивести назви відділень, які знаходяться у корпусі 5
-- з фондом фінансування меншим, ніж 30000.
-- SELECT NAME 
-- FROM DEPARTMENTS 
-- WHERE BUILDING = 5 AND FINANCING < 30000

-- 6. Вивести назви відділень, які знаходяться у корпусі 3 з
-- фондом фінансування у діапазоні від 12000 до 15000.
-- SELECT NAME 
-- FROM DEPARTMENTS 
-- WHERE BUILDINg = 3 
-- AND FINANCING BETWEEN 12000 AND 15000

-- 8. Вивести назви палат, які знаходяться у корпусах 4 та
-- 5 на 1-му поверсі.
-- SELECT NAME 
-- FROM WARDS
-- WHERE BUILDING IN (4, 5) AND FLOOR = 1

-- 9. Вивести назви, корпуси та фонди фінансування відділень, які знаходяться у корпусах 3 або 6 та мають
-- фонд фінансування менший, ніж 11000 або більший
-- за 25000.
-- SELECT NAME, BUILDING, FINANCING
-- FROM DEPARTMENTS
-- WHERE (BUILDING = 3 OR BUILDING = 6)
-- AND (FINANCING < 11000 OR FINANCING > 25000)

-- 10. Вивести прізвища лікарів, зарплата (сума ставки та
-- надбавки 120) яких перевищує 1500.
-- SELECT SURNAME 
-- FROM DOCTORS 
-- WHERE SALARY + 1000 > 60000

-- 11. Вивести прізвища лікарів, у яких половина зарплати
-- перевищує триразову надбавку у вигляді 500.
-- SELECT SURNAME 
-- FROM DOCTORS
-- WHERE SALARY / 2 > 3 * 10000

-- 12. Вивести назви обстежень без повторень, які проводяться у перші три дні тижня з 12:00 до 15:00.
-- SELECT DISTINCT NAME
-- FROM EXAMINATIONS
-- WHERE DAYOFWEEK IN (1, 2, 3)
-- AND STARTTIME >= '12:00:00'
-- AND ENDTIME <= '15:00:00'

-- 13. Вивести назви та номери корпусів відділень, які знаходяться у корпусах 1, 3, 8 або 10.
-- SELECT NAME, BUILDING 
-- FROM DEPARTMENTS 
-- WHERE BUILDING IN (1, 3, 8, 10)

-- 14. Вивести назви захворювань усіх ступенів тяжкості,
-- крім 1-го та 2-го.
-- SELECT NAME 
-- FROM DISEASES 
-- WHERE SEVERITY NOT IN (1, 2)

-- 15. Вивести назви відділень, які не знаходяться у
-- першому або третьому корпусі.
-- SELECT NAME 
-- FROM DEPARTMENTS 
-- WHERE BUILDING NOT IN (1, 3)


-- 16. Вивести назви відділень, які знаходяться у першому
-- або третьому корпусі.
-- SELECT NAME 
-- FROM DEPARTMENTS 
-- WHERE BUILDING IN (1, 3)

-- 17. Вивести прізвища лікарів, що починаються з літери
-- «N».
-- SELECT SURNAME
-- FROM DOCTORS 
-- WHERE SURNAME LIKE 'N%'
