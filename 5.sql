-- ПІДРАХУВАТИ СЕРЕДНІЙ ВІК СТУДЕНТІВ ТИХ ПРОФЕСІЙ, ДЕ Є БІЛЬШЕ ОДНОГО ПРЕДСТАВНИКА
SELECT JOB, AVG(AGE)
FROM STUDENT
GROUP BY JOB
HAVING COUNT(*) > 1