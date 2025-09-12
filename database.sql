CREATE DATABASE InduccionCSharp;
USE InduccionCSharp;

CREATE TABLE Patients (
	id_patient INT PRIMARY KEY AUTO_INCREMENT,
    name_patient VARCHAR(100),
    lastName_patient VARCHAR(100),
    brithdate_patient DATE,
    gender_patient VARCHAR(10)
);
CREATE TABLE Appointments (
	folio INT PRIMARY KEY AUTO_INCREMENT,
    id_pta INT,
    date_appointment TIMESTAMP,
    turn_apointment VARCHAR(12),
    hour_appointment TIME,
    age INT,
    weight FLOAT,
    height FLOAT,
    bloodPressure VARCHAR(10),
    diagnosis VARCHAR(300),
    FOREIGN KEY (id_pta) REFERENCES Patients(id_patient)
);

SELECT * FROM patients;
SELECT * FROM Appointments;

SELECT * FROM patients p INNER JOIN appointments a ON p.id_patient = a.id_pta WHERE a.id_pta = 2;