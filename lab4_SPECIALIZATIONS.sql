-- СТВОРЕННЯ ТАБЛИЦІ СПЕЦІАЛІЗАЦІЇ (SPECIALIZATIONS)
CREATE TABLE SPECIALIZATIONS (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(100) NOT NULL UNIQUE CHECK (NAME <> '')
);

-- ЗАПОВНЕННЯ ТАБЛИЦІ СПЕЦІАЛІЗАЦІЇ
INSERT INTO SPECIALIZATIONS (NAME) VALUES
('Cardiology'),
('Neurology'),
('Orthopedics'),
('Pediatrics'),
('Dermatology'),
('Radiology'),
('Gastroenterology'),
('Oncology'),
('Endocrinology'),
('Nephrology'),
('Hematology'),
('Rheumatology'),
('Pulmonology'),
('Ophthalmology'),
('Otolaryngology'),
('Urology'),
('Gynecology'),
('Pathology'),
('Immunology'),
('Infectious Disease'),
('Anesthesiology'),
('General Surgery'),
('Plastic Surgery'),
('Vascular Surgery'),
('Thoracic Surgery'),
('Neurosurgery'),
('Emergency Medicine'),
('Internal Medicine'),
('Family Medicine'),
('Geriatrics');
