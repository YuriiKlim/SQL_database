-- СТВОРЕННЯ ТАБЛИЦІ ВІДПУСТКИ (VACATIONS)
CREATE TABLE VACATIONS (
    ID SERIAL PRIMARY KEY,
    END_DATE DATE NOT NULL CHECK (END_DATE > START_DATE),
    START_DATE DATE NOT NULL,
    DOCTOR_ID INT NOT NULL,
    FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTORS(ID)
);

-- ЗАПОВНЕННЯ ТАБЛИЦІ ВІДПУСТКИ
INSERT INTO VACATIONS (END_DATE, START_DATE, DOCTOR_ID) VALUES
('2024-01-20', '2024-01-10', 1),
('2024-02-15', '2024-02-05', 2),
('2024-03-12', '2024-03-02', 3),
('2024-04-10', '2024-03-31', 4),
('2024-05-18', '2024-05-08', 5),
('2024-06-25', '2024-06-15', 6),
('2024-07-22', '2024-07-12', 7),
('2024-08-19', '2024-08-09', 8),
('2024-09-16', '2024-09-06', 9),
('2024-10-13', '2024-10-03', 10),
('2024-11-20', '2024-11-10', 11),
('2024-12-18', '2024-12-08', 12),
('2024-01-15', '2024-01-05', 13),
('2024-02-22', '2024-02-12', 14),
('2024-03-20', '2024-03-10', 15),
('2024-04-17', '2024-04-07', 16),
('2024-05-24', '2024-05-14', 17),
('2024-06-21', '2024-06-11', 18),
('2024-07-19', '2024-07-09', 19),
('2024-08-16', '2024-08-06', 20);

