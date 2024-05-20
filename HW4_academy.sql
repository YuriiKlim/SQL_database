-- 1. Виведіть усі можливі пари рядків викладачів і груп.
SELECT 
    T.NAME AS TEACHER_NAME, 
    T.SURNAME AS TEACHER_SURNAME, 
    G.NAME AS GROUP_NAME 
FROM 
    TEACHERS T, 
    GROUPS G;

-- 2. Виведіть назви факультетів, фонд фінансування кафедр
-- яких перевищує фонд фінансування факультету.
SELECT 
    F.NAME AS FACULTY_NAME 
FROM 
    FACULTIES F 
JOIN 
    DEPARTMENTS D ON F.ID = D.FACULTY_ID 
WHERE 
    D.FINANCING > F.FINANCING;

-- 3. Виведіть прізвища кураторів груп і назви груп, які вони
-- курирують.
SELECT 
    C.SURNAME AS CURATOR_SURNAME, 
    G.NAME AS GROUP_NAME 
FROM 
    CURATORS C 
JOIN 
    GROUPS G ON C.ID = G.ID;

-- 4. Виведіть імена та прізвища викладачів, які читають лекції
-- у групі «P107».
SELECT 
    T.NAME AS TEACHER_NAME, 
    T.SURNAME AS TEACHER_SURNAME 
FROM 
    TEACHERS T 
JOIN 
    LECTURES L ON T.ID = L.TEACHER_ID 
JOIN 
    GROUPSLECTURES GL ON L.ID = GL.LECTURE_ID 
JOIN 
    GROUPS G ON GL.GROUP_ID = G.ID 
WHERE 
    G.NAME = 'P107';

-- 5. Виведіть прізвища викладачів і назви факультетів, на яких
-- вони читають лекції.
SELECT 
    T.SURNAME AS TEACHER_SURNAME, 
    F.NAME AS FACULTY_NAME 
FROM 
    TEACHERS T 
JOIN 
    LECTURES L ON T.ID = L.TEACHER_ID 
JOIN 
    GROUPSLECTURES GL ON L.ID = GL.LECTURE_ID 
JOIN 
    GROUPS G ON GL.GROUP_ID = G.ID 
JOIN 
    DEPARTMENTS D ON G.DEPARTMENT_ID = D.ID 
JOIN 
    FACULTIES F ON D.FACULTY_ID = F.ID;

-- 6. Виведіть назви кафедр і назви груп, які до них належать.
SELECT 
    D.NAME AS DEPARTMENT_NAME, 
    G.NAME AS GROUP_NAME 
FROM 
    DEPARTMENTS D 
JOIN 
    GROUPS G ON D.ID = G.DEPARTMENT_ID;

-- 7. Виведіть назви предметів, які викладає викладач «Samantha
-- Adams».
SELECT 
    S.NAME AS SUBJECT_NAME 
FROM 
    SUBJECTS S 
JOIN 
    LECTURES L ON S.ID = L.SUBJECT_ID 
JOIN 
    TEACHERS T ON L.TEACHER_ID = T.ID 
WHERE 
    T.NAME = 'SAMANTHA' AND T.SURNAME = 'ADAMS';

-- 8. Виведіть назви кафедр, на яких викладається дисципліна
-- «Database Theory».
SELECT 
    D.NAME AS DEPARTMENT_NAME 
FROM 
    DEPARTMENTS D 
JOIN 
    GROUPS G ON D.ID = G.DEPARTMENT_ID 
JOIN 
    GROUPSLECTURES GL ON G.ID = GL.GROUP_ID 
JOIN 
    LECTURES L ON GL.LECTURE_ID = L.ID 
JOIN 
    SUBJECTS S ON L.SUBJECT_ID = S.ID 
WHERE 
    S.NAME = 'DATABASE THEORY';

-- 9. Виведіть назви груп, що належать до факультету «Computer
-- Science».
SELECT 
    G.NAME AS GROUP_NAME 
FROM 
    GROUPS G 
JOIN 
    DEPARTMENTS D ON G.DEPARTMENT_ID = D.ID 
JOIN 
    FACULTIES F ON D.FACULTY_ID = F.ID 
WHERE 
    F.NAME = 'COMPUTER SCIENCE';

-- 10. Виведіть назви груп 5-го курсу, а також назви факультетів,
-- до яких вони належать.
SELECT 
    G.NAME AS GROUP_NAME, 
    F.NAME AS FACULTY_NAME 
FROM 
    GROUPS G 
JOIN 
    DEPARTMENTS D ON G.DEPARTMENT_ID = D.ID 
JOIN 
    FACULTIES F ON D.FACULTY_ID = F.ID 
WHERE 
    G.YEAR = 5;

-- 11. Виведіть повні імена викладачів і лекції, які вони читають
-- (назви предметів та груп). Зробіть відбір по тим лекціям,
-- які проходять в аудиторії «B103»
SELECT 
    T.NAME || ' ' || T.SURNAME AS TEACHER_NAME, 
    S.NAME AS SUBJECT_NAME, 
    G.NAME AS GROUP_NAME 
FROM 
    TEACHERS T 
JOIN 
    LECTURES L ON T.ID = L.TEACHER_ID 
JOIN 
    SUBJECTS S ON L.SUBJECT_ID = S.ID 
JOIN 
    GROUPSLECTURES GL ON L.ID = GL.LECTURE_ID 
JOIN 
    GROUPS G ON GL.GROUP_ID = G.ID 
WHERE 
    L.LECTURE_ROOM = 'B103';
