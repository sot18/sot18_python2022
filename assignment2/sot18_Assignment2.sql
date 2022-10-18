USE sot18;

DROP TABLE IF EXISTS DOCTOR cascade ;
CREATE TABLE DOCTOR(
doctor_id VARCHAR(32) primary key,
first_name varchar(32) not null,
middle_initial char(1) not null,
last_name varchar(32) not null,
birthday date not null,
age int not null,
speciality varchar(50) not null,
title varchar(50) not null
);

DROP TABLE IF EXISTS PATIENT CASCADE;
CREATE TABLE PATIENT (
patient_id VARCHAR(32) not null primary key,
first_name varchar(32) not null,
middle_initial char(1) null,
last_name varchar(32) not null,
age int not null,
birthday date not null,
previous_health_conditions varchar(100) not null,
allergies varchar(200) null
);

DROP TABLE IF EXISTS VISIT CASCADE;
CREATE TABLE VISIT(
visit_id VARCHAR(32) primary key not null,
reason_for_the_visit varchar(100) not null,
visit_date date not null,
FK_patient_id varchar(32) not null,
FK_doctor_id varchar(32) not null,
FOREIGN KEY(FK_patient_id) REFERENCES PATIENT(patient_id) ON DELETE CASCADE,
FOREIGN KEY(FK_doctor_id) REFERENCES DOCTOR(doctor_id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS DIAGNOSIS CASCADE;
CREATE TABLE DIAGNOSIS (
diagnosis_id varchar(32) primary key not null,
diagnosis varchar(200) not null,
diagnosis_date date not null
);

DROP TABLE IF EXISTS VISIT_DIAGNOSIS CASCADE;
CREATE TABLE VISIT_DIAGNOSIS(
visit_diagnosis_id varchar(32) not null primary key,
FK_visit_id varchar(32) not null,
FK_diagnosis_id varchar(32) not null,
FOREIGN KEY(FK_visit_id) REFERENCES VISIT(visit_id) ON DELETE cascade,
FOREIGN KEY(FK_diagnosis_id) REFERENCES DIAGNOSIS(diagnosis_id) ON DELETE CASCADE
); 

DROP TABLE IF EXISTS PROCEDURE1 CASCADE;
CREATE TABLE PROCEDURE1(
procedure_id varchar(32) not null primary key,
procedure_name varchar(300) not null,
procedure_date date not null
);

DROP TABLE IF EXISTS VISIT_PROCEDURE CASCADE;
CREATE TABLE VISIT_PROCEDURE(
visit_procedure_id varchar(32) not null primary key,
FK_visit_id varchar(32) not null,
FK_procedure_id varchar(32) not null,
FOREIGN KEY(FK_visit_id) REFERENCES VISIT(visit_id) ON DELETE CASCADE,
FOREIGN KEY(FK_procedure_id) REFERENCES PROCEDURE1(procedure_id) ON DELETE CASCADE
); 
