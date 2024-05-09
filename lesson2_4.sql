-- ПІДРАХУВАТИ КІЛЬКІСТЬ СТУДЕНТІВ КОЖНОЇ ПРОФЕСІЙ
SELECT JOB, COUNT(*)
FROM STUDENT
GROUP BY JOB;

-- ПІДРАХУВАТИ СЕРЕДНІЙ ВІК СТУДЕНТІВ КОЖНОЇ ПРОФЕСІЙ
SELECT JOB, AVG(AGE) AS AVG_AGE
FROM STUDENT
GROUP BY JOB;

-- ПІДРАХУВАТИ СЕРЕДНІЙ ВІК СТУДЕНТІВ КОЖНОЇ ПРОФЕСІЙ, АЛЕ НЕ ВКЮЧАТИ HENRY
SELECT JOB, AVG(AGE) AS AVG_AGE
FROM STUDENT
WHERE FIRST_NAME != 'Henry'
GROUP BY JOB;

-- ПІДРАХУВАТИ СЕРЕДНІЙ ВІК СТУДЕНТІВ КОЖНОЇ ПРОФЕСІЙ. ДАНІ ВДСОРТУВАТИ
SELECT JOB, AVG(AGE) AS AVG_AGE
FROM STUDENT
GROUP BY JOB
ORDER BY AVG_AGE;  -- ASC АБО DESC

SELECT JOB, AVG(AGE) AS AVG_AGE, COUNT(*) AS COUNT
FROM STUDENT
GROUP BY JOB
ORDER BY COUNT, AVG_AGE;

-- ПІДРАХУВАТИ КІЛЬКІСТЬ ПАР JOB, LAST_NAME
SELECT JOB, LAST_NAME, COUNT(*)
FROM STUDENT
GROUP BY JOB, LAST_NAME