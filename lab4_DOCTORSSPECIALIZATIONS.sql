-- СТВОРЕННЯ ТАБЛИЦІ ЛІКАРІ ТА СПЕЦІАЛІЗАЦІЇ
CREATE TABLE DOCTORSSPECIALIZATIONS (
    ID SERIAL PRIMARY KEY,
    DOCTOR_ID  INT NOT NULL REFERENCES DOCTORS(ID),
    SPECIALIZATION_ID INT NOT NULL REFERENCES SPECIALIZATIONS(ID)
);

-- Заповнення таблиці Лікарі та спеціалізації
INSERT INTO DOCTORSSPECIALIZATIONS (DOCTOR_ID, SPECIALIZATION_ID) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 2),
(3, 4),
(4, 3),
(4, 5),
(5, 4),
(5, 6),
(6, 1),
(6, 2),
(7, 1),
(7, 3),
(8, 2),
(8, 4),
(9, 3),
(9, 5),
(10, 4),
(10, 6),
(11, 1),
(11, 2),
(12, 1),
(12, 3),
(13, 2),
(13, 4),
(14, 3),
(14, 5),
(15, 4),
(15, 6),
(16, 1),
(16, 2),
(17, 1),
(17, 3),
(18, 2),
(18, 4),
(19, 3),
(19, 5),
(20, 4),
(20, 6),
(21, 1),
(21, 2),
(22, 1),
(22, 3),
(23, 2),
(23, 4),
(24, 3),
(24, 5),
(25, 4),
(25, 6);
