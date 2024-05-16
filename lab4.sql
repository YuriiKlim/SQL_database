-- 1. Виведіть повні імена лікарів та їх спеціалізації.
-- SELECT 
--     DOCTORS.NAME || ' ' || DOCTORS.SURNAME AS FULL_NAME, 
--     SPECIALIZATIONS.NAME AS SPECIALIZATION
-- FROM 
--     DOCTORS
-- JOIN 
--     DOCTORSSPECIALIZATIONS ON DOCTORS.ID = DOCTORSSPECIALIZATIONS.DOCTOR_ID
-- JOIN 
--     SPECIALIZATIONS ON DOCTORSSPECIALIZATIONS.SPECIALIZATION_ID = SPECIALIZATIONS.ID;

-- 2. Виведіть прізвища та зарплати (сума ставки та надбавки) лікарів, які не перебувають у відпустці.
-- SELECT 
--     DOCTORS.SURNAME, 
--     DOCTORS.SALARY + DOCTORS.PREMIUM AS TOTAL_SALARY
-- FROM 
--     DOCTORS
-- LEFT JOIN 
--     VACATIONS ON DOCTORS.ID = VACATIONS.DOCTOR_ID 
--     AND CURRENT_DATE BETWEEN VACATIONS.START_DATE AND VACATIONS.END_DATE
-- WHERE 
--     VACATIONS.DOCTOR_ID IS NULL;

-- 3. Виведіть назви палат, які знаходяться у відділенні
-- «Intensive Treatment».
-- SELECT 
--     WARDS.NAME AS WARD_NAME
-- FROM 
--     WARDS
-- JOIN 
--     DEPARTMENTS ON WARDS.BUILDING = DEPARTMENTS.BUILDING
-- WHERE 
--     DEPARTMENTS.NAME = 'Intensive Treatment';

-- 4. Виведіть назви відділень без повторень, які спонсоруються компанією «Umbrella Corporation».
-- SELECT DISTINCT 
--     DEPARTMENTS.NAME
-- FROM 
--     DONATIONS
-- JOIN 
--     DEPARTMENTS ON DONATIONS.DEPARTMENT_ID = DEPARTMENTS.ID
-- JOIN 
--     SPONSORS ON DONATIONS.SPONSOR_ID = SPONSORS.ID
-- WHERE 
--     SPONSORS.NAME = 'Umbrella Corporation';

-- 5. Виведіть усі пожертвування за останній місяць у вигляді: відділення, спонсор, сума пожертвування, дата
-- пожертвування.
-- SELECT 
--     DEPARTMENTS.NAME AS DEPARTMENT, 
--     SPONSORS.NAME AS SPONSOR, 
--     DONATIONS.AMOUNT, 
--     DONATIONS.DATE
-- FROM 
--     DONATIONS
-- JOIN 
--     DEPARTMENTS ON DONATIONS.DEPARTMENT_ID = DEPARTMENTS.ID
-- JOIN 
--     SPONSORS ON DONATIONS.SPONSOR_ID = SPONSORS.ID
-- WHERE 
--     DONATIONS.DATE >= (CURRENT_DATE - INTERVAL '1 month');

-- 6. Виведіть прізвища лікарів із зазначенням відділень,
-- в яких вони проводять обстеження. Враховуйте обстеження, які проводяться лише у будні дні.
SELECT
    DOCTORS.SURNAME, 
    DEPARTMENTS.NAME AS DEPARTMENT
FROM 
    DOCTORS
JOIN 
    DOCTORSEXAMINATIONS ON DOCTORS.ID = DOCTORSEXAMINATIONS.DOCTOR_ID
JOIN 
    DEPARTMENTS ON DOCTORS.ID = DEPARTMENTS.ID
JOIN
	EXAMINATIONS ON EXAMINATIONS.ID = DOCTORSEXAMINATIONS.EXAMINATION_ID
WHERE 
    EXAMINATIONS.DAYOFWEEK BETWEEN 1 AND 5;

-- 7. Виведіть назви відділень, які отримували пожертву-вання
-- у розмірі понад 100000, із зазначенням їх лікарів.

-- 8. Виведіть назви відділень, в яких лікарі не отримують
-- надбавки.

-- 9. Виведіть назви відділень і назви захворювань, обстеження з яких вони проводили за останні півроку.
