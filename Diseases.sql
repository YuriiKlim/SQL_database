-- СТВОРЕННЯ ТАБЛИЦІ ЗАХВОРЮВАННЯ (DISEASES)

CREATE TABLE DISEASES ( 
	ID SERIAL PRIMARY KEY,
	NAME VARCHAR(100) NOT NULL UNIQUE CHECK (NAME <> ''),
	SEVERITY INT NOT NULL CHECK (SEVERITY >= 1) DEFAULT 1
);

-- НАПОВНЕННЯ ТАБЛИЦІ ЗАХВОРЮВАННЯ

INSERT INTO diseases (name, severity) VALUES
('Hypertension', 2),
('Diabetes Mellitus', 3),
('Asthma', 2),
('Chronic Obstructive Pulmonary Disease', 4),
('Chronic Kidney Disease', 3),
('Alzheimers Disease', 5),
('Parkinsons Disease', 4),
('Epilepsy', 3),
('Migraine', 2),
('Osteoporosis', 2),
('Rheumatoid Arthritis', 3),
('Systemic Lupus Erythematosus', 4),
('Multiple Sclerosis', 4),
('Celiac Disease', 2),
('Crohns Disease', 3),
('Ulcerative Colitis', 3),
('Psoriasis', 2),
('Eczema', 1),
('Hepatitis B', 4),
('Hepatitis C', 4),
('Tuberculosis', 5),
('Malaria', 5),
('HIV/AIDS', 5),
('Influenza', 3),
('Pneumonia', 4),
('Bronchitis', 2),
('Sinusitis', 1),
('Tonsillitis', 1),
('Appendicitis', 3),
('Gastritis', 2),
('Peptic Ulcer Disease', 3),
('Pancreatitis', 4),
('Cholecystitis', 3),
('Gallstones', 2),
('Hernia', 2),
('Prostate Cancer', 5),
('Breast Cancer', 5),
('Lung Cancer', 5),
('Colorectal Cancer', 5),
('Skin Cancer', 3),
('Leukemia', 5),
('Lymphoma', 5),
('Myeloma', 5),
('Anemia', 2),
('Hemophilia', 4),
('Thalassemia', 3),
('Sickle Cell Disease', 4),
('Down Syndrome', 4),
('Autism Spectrum Disorder', 3),
('Schizophrenia', 5);

