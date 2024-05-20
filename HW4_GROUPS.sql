-- СТВОРЕННЯ ТАБЛИЦІ ГРУПИ (GROUPS)
CREATE TABLE GROUPS (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(10) NOT NULL UNIQUE CHECK (NAME <> ''),
    YEAR INT NOT NULL CHECK (YEAR >= 1 AND YEAR <= 5),
    DEPARTMENT_ID INT NOT NULL
);

-- ЗАПОВНЕННЯ ТАБЛИЦІ ГРУПИ
INSERT INTO GROUPS (NAME, YEAR, DEPARTMENT_ID) VALUES
('GRP001', 1, 1),
('GRP002', 2, 2),
('GRP003', 3, 3),
('GRP004', 4, 4),
('GRP005', 5, 5),
('GRP006', 1, 6),
('GRP007', 2, 7),
('GRP008', 3, 8),
('GRP009', 4, 9),
('GRP010', 5, 10),
('GRP011', 1, 1),
('GRP012', 2, 2),
('GRP013', 3, 3),
('GRP014', 4, 4),
('GRP015', 5, 5),
('GRP016', 1, 6),
('GRP017', 2, 7),
('GRP018', 3, 8),
('GRP019', 4, 9),
('GRP020', 5, 10);
