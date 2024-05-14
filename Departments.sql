-- СТВОРЕННЯ ТАБЛИЦІ ВІДДІЛЕННЯ (DEPARTMENTS)

CREATE TABLE DEPARTMENTS ( 
	ID SERIAL PRIMARY KEY,
	BUILDING INT NOT NULL CHECK (BUILDING >= 1,																														AND BUILDING <= 5), FINANCING NUMERIC NOT NULL CHECK (FINANCING >= 0) DEFAULT 0,
	NAME VARCHAR(100) NOT NULL UNIQUE CHECK (NAME <> '')
);

-- НАПОВНЕННЯ ТАБЛИЦІ ВІДДІЛЕННЯ

INSERT INTO departments (building, financing, name) VALUES
(1, 10000.00, 'Cardiology'),
(2, 15000.00, 'Neurology'),
(3, 20000.00, 'Orthopedics'),
(4, 25000.00, 'Pediatrics'),
(5, 30000.00, 'General Surgery'),
(1, 11000.00, 'Dermatology'),
(2, 12000.00, 'Ophthalmology'),
(3, 13000.00, 'Gynecology'),
(4, 14000.00, 'Oncology'),
(5, 16000.00, 'Radiology'),
(1, 17000.00, 'Urology')