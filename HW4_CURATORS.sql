-- СТВОРЕННЯ ТАБЛИЦІ КУРАТОРИ (CURATORS)
CREATE TABLE CURATORS (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR NOT NULL CHECK (NAME <> ''),
    SURNAME VARCHAR NOT NULL CHECK (SURNAME <> '')
);

-- Заповнення таблиці Куратори
INSERT INTO Curators (Name, Surname) VALUES
('John', 'Doe'),
('Jane', 'Smith'),
('Alice', 'Johnson'),
('Bob', 'Williams'),
('Charlie', 'Brown'),
('David', 'Jones'),
('Eve', 'Garcia'),
('Frank', 'Martinez'),
('Grace', 'Davis'),
('Hank', 'Rodriguez'),
('Ivy', 'Martinez'),
('Jack', 'Hernandez'),
('Kate', 'Lopez'),
('Leo', 'Gonzalez'),
('Mia', 'Wilson'),
('Nick', 'Anderson'),
('Olivia', 'Thomas'),
('Paul', 'Taylor'),
('Quinn', 'Moore'),
('Rose', 'Jackson');
