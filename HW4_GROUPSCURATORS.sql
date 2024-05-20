-- СТВОРЕННЯ ТАБЛИЦІ ГРУПИ ТА КУРАТОРИ (GROUPSCURATORS)
CREATE TABLE GROUPSCURATORS (
    ID SERIAL PRIMARY KEY,
    CURATOR_ID INT NOT NULL,
    GROUP_ID INT NOT NULL
);

-- ЗАПОВНЕННЯ ТАБЛИЦІ ГРУПИ ТА КУРАТОРИ
INSERT INTO GROUPSCURATORS (CURATOR_ID, GROUP_ID) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12),
(13, 13),
(14, 14),
(15, 15),
(16, 16),
(17, 17),
(18, 18),
(19, 19),
(20, 20);
