-- СТВОРЕННЯ ТАБЛИЦІ ГРУПИ ТА ЛЕКЦІЇ (GROUPSLECTURES)
CREATE TABLE GROUPSLECTURES (
    ID SERIAL PRIMARY KEY,
    GROUP_ID INT NOT NULL,
    LECTURE_ID INT NOT NULL
);

-- ЗАПОВНЕННЯ ТАБЛИЦІ ГРУПИ ТА ЛЕКЦІЇ
INSERT INTO GROUPSLECTURES (GROUP_ID, LECTURE_ID) VALUES
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

