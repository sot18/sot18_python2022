import uuid
import pymysql
import json

class Config:
    def __init__(self):
        con_params = self.__read_config()
        self.db_conn = pymysql.connect(host=con_params["host"],
                             user=con_params["user"],
                             password=con_params["password"],
                             db=con_params["db"],
                             charset=con_params["charset"],
                             cursorclass=pymysql.cursors.DictCursor)
    def __read_config(self):
        try:
            f = open("config.txt")
            data = f.read()
            return dict(json.loads(data))
        finally:
            f.close()
            
class Patient:
    def __init__(self, patient_id="", first_name = "",middle_initial = "", last_name = "",age = "", birthday="",previous_health_conditions = "", allergies = ""):
        self.__f_name = first_name
        self.__middle_initial = middle_initial
        self.__l_name = last_name
        self.__age = age
        self.__birthday = birthday
        self.__previous_health_condititon = previous_health_conditions
        self.__allergies = allergies
        
        if patient_id == "":
            self.__patient_id = str(uuid.uuid4())
            
            try: 
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO patient (patient_id, first_name,middle_initial, last_name, age, birthday, previous_health_conditions, allergies)'
                    qry = qry + 'VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__patient_id, self.__f_name,self.__middle_initial, self.__l_name,self.__age,self.__birthday,self.__previous_health_condititon,self.__allergies)) 
                    con.commit()
            finally:
                con.close()
                
        else:
            self.__patient_id = patient_id
            
            try:
                config = Config()
                con = config.db_conn
                    
                with con.cursor() as cur:
                    qry = "SELECT * FROM patient WHERE patient_id = '" + patient_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    
                    for row in rows:
                        self.__patient_id = row["patient_id"]
                        self.__f_name = row["first_name"]
                        self.__middle_initial = row["middle_initial"]
                        self.__l_name = row["last_name"]
                        self.__f_name = row["first_name"]
                        self.__age = row["age"]
                        self.__birthday = row["birthday"]
                        self.__previous_health_condititon = row["previous_health_conditions"]
                        self.__allergies = row["allergies"]
                        
            finally:
                con.close()
                
    def get_first_name(self):
        return self.__f_name
    
    def get_age(self):
        return self.__age
    
    def get_birthday(self):
        return self.__birthday
    
    def get_last_name(self):
        return self.__l_name
    
    def get_patient_id(self):
        return self.__patient_id

    def set_first_name(self, first_name):
        self.__f_name = first_name
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE Patient SET first_name = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__f_name, self.__patient_id)) 
                con.commit()
        finally:
            con.close()
    
    def set_last_name(self, last_name):
        self.__l_name = last_name
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE Patient SET last_name = %s WHERE patient_id = %s;'
                print(qry)
                cur.execute(qry, (self.__l_name, self.__patient_id)) 
                con.commit()
        finally:
            con.close()
            
    def delete_entry_based_on_age(self, age):
        self.age = age
        
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM Patient WHERE age >= %s;'
                print(qry)
                cur.execute(qry, (self.__l_name, self.__patient_id)) 
                con.commit()
        finally:
            con.close()
            
    def to_json(self):
        field_data = {
            "id" : self.__patient_id,
            "first_name" : self.__f_name,
            "last_name" : self.__l_name,
            "age" : self.__age,
            "birthday" : self.__birthday,
            "previous _health_condition" : self.__previous_health_condititon,
            "allergies" : self.__allergies         
        }
        
        return json.dumps(field_data)
                
class Doctor:
    def __init__(self, doctor_id="", first_name = "",middle_initial = "", last_name = "",birthday="",age = "",speciality = "", title = ""):
        self.__f_name = first_name
        self.__middle_initial = middle_initial
        self.__l_name = last_name
        self.__birthday = birthday
        self.__age = age
        self.__speciality = speciality
        self.__title = title
        
        if doctor_id == "":
            self.__doctor_id = str(uuid.uuid4())
            
            try: 
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO DOCTOR (doctor_id, first_name,middle_initial, last_name,birthday, age, speciality, title)'
                    qry = qry + 'VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__doctor_id, self.__f_name,self.__middle_initial, self.__l_name,self.__birthday,self.__age,self.__speciality,self.__title)) 
                    con.commit()
            finally:
                con.close()
                
        else:
            self.__doctor_id = doctor_id
            
            try:
                config = Config()
                con = config.db_conn
                    
                with con.cursor() as cur:
                    qry = "SELECT * FROM doctor WHERE doctor_id = '" + doctor_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    
                    for row in rows:
                        self.__doctor_id = row["doctor_id"]
                        self.__f_name = row["first_name"]
                        self.__middle_initial = row["middle_initial"]
                        self.__l_name = row["last_name"]
                        self.__birthday = row["birthday"]
                        self.__age = row["age"]
                        self.__speciality = row["speciality"]
                        self.__title = row["title"]
                        
            finally:
                con.close()
                
    def get_first_name(self):
        return self.__f_name
    
    def get_speciality(self):
        return self.__speciality
    
    def get_title(self):
        return self.__title
    
    def get_age(self):
        return self.__age
    
    def get_birthday(self):
        return self.__birthday
    
    def get_last_name(self):
        return self.__l_name
    
    def get_doctor_id(self):
        return self.__doctor_id

    def set_first_name(self, first_name):
        self.__f_name = first_name
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE Doctor SET first_name = %s WHERE doctor_id = %s;'
                print(qry)
                cur.execute(qry, (self.__f_name, self.__doctor_id)) 
                con.commit()
        finally:
            con.close()
    
    def set_last_name(self, last_name):
        self.__l_name = last_name
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE Doctor SET last_name = %s WHERE doctor_id = %s;'
                print(qry)
                cur.execute(qry, (self.__l_name, self.__doctor_id)) 
                con.commit()
        finally:
            con.close()
            
    def delete_entry(self):
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM Doctor WHERE age >= %s;'
                print(qry)
                cur.execute(qry, (self.__l_name, self.__doctor_id)) 
                con.commit()
        finally:
            con.close()
            
    def to_json(self):
        field_data = {
            "id" : self.__doctor_id,
            "first_name" : self.__f_name,
            "last_name" : self.__l_name,
            "age" : self.__age,
            "birthday" : self.__birthday,
            "speciality" : self.__speciality,
            "title" : self.__title
                     
        }
        
        return json.dumps(field_data)
        
            
    
                
class Visit:
    def __init__(self, visit_id="", reason_for_visit = "",visit_date = "", fk_patient_id = "",fk_doctor_id =""):
        self.__reason_for_visit = reason_for_visit
        self.__visit_date = visit_date
        self.__fk_patient_id = fk_patient_id
        self.__fk_doctor_id = fk_doctor_id
        
        if visit_id == "":
            self.__visit_id = str(uuid.uuid4())
            
            try: 
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO Visit (visit_id, reason_for_visit,visit_date, fk_patient_id,fk_doctor_id)'
                    qry = qry + 'VALUES(%s, %s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__visit_id, self.__reason_for_visit,self.__visit_date, self.__fk_patient_id,self.__fk_doctor_id)) 
                    con.commit()
            finally:
                con.close()
                
        else:
            self.__visit_id = visit_id
            
            try:
                config = Config()
                con = config.db_conn
                    
                with con.cursor() as cur:
                    qry = "SELECT * FROM visit WHERE visit_id = '" + visit_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    
                    for row in rows:
                        self.__visit_id = row["visit_id"]
                        self.__reason_for_visit = row["reason_for_visit"]
                        self.__visit_date = row["visit_date"]
                        self.__fk_patient_id = row["fk_patient_id"]
                        self.__fk_doctor_id = row["fk_doctor_id"]
                        
            finally:
                con.close()
                
    def get_visit_id(self):
        return self.__visit_id
    
    def get_visit_date(self):
        return self.__visit_date
    
    def get_reason_for_visit(self):
        return self.__reason_for_visit
    
    def set_reason_for_visit(self):
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE VIST SET REASON_FOR_VISIT = %s WHERE FK_PATIENT_ID = %s;'
                print(qry)
                cur.execute(qry, (self.__reason_for_visit, self.__fk_patient_id)) 
                con.commit()
        finally:
            con.close()
            
    def delete_entry(self):
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM Visit WHERE fk_doctor_id = %s;'
                print(qry)
                cur.execute(qry, (self.__fk_doctor_id)) 
                con.commit()
        finally:
            con.close()
            
    def to_json(self):
        field_data = {
            "id" : self.__visit_id,
            "reason_for_visit" : self.__reason_for_visit,
            "visit_date" : self.__visit_date,
            "fk_patient_id" : self.__fk_patient_id,
            "fk_doctor_id" : self.__fk_doctor_id      
        }
        
        return json.dumps(field_data)
        


class Diagnosis:
    def __init__(self, diagnosis_id="",diagnosis = "",diagnosis_date = ""):
        self.__diagnosis = diagnosis
        self.__diagnosis_date = diagnosis_date
       
        
        if diagnosis_id == "":
            self.__diagnosis_id = str(uuid.uuid4())
            
            try: 
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO DIAGNOSIS (diagnosis_id, diagnosis,diagnosis_date)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__diagnosis_id, self.__diagnosis,self.__diagnosis_date)) 
                    con.commit()
            finally:
                con.close()
                
        else:
            self.__diagnosis_id = diagnosis_id
            
            try:
                config = Config()
                con = config.db_conn
                    
                with con.cursor() as cur:
                    qry = "SELECT * FROM diagnosis WHERE diagnosis_id = '" + diagnosis_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    
                    for row in rows:
                        self.__diagnosis_id = row["diagnosis_id"]
                        self.__diagnosis = row["diagnosis"]
                        self.__diagnosis_date = row["diagnosis_date"]
                        
            finally:
                con.close()
                
    def get_diagnosis_id(self):
        return self.__diagnosis_id
    
    def get_diagnosis(self):
        return self.__diagnosis
    
    def get_diagnosis_date(self):
        return self.__diagnosis_date
    
    def set_diagnosis(self):
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE DIAGNOSIS SET DIAGNOSIS = %s WHERE DIAGNOSIS_ID = %s;'
                print(qry)
                cur.execute(qry, (self.__diagnosis, self.__diagnosis_id)) 
                con.commit()
        finally:
            con.close()
            
    def delete_entry(self):
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM Diagnosis WHERE diagnosis_id = %s;'
                print(qry)
                cur.execute(qry, (self.__diagnosis_id)) 
                con.commit()
        finally:
            con.close()
            
    def to_json(self):
        field_data = {
            "id" : self.__diagnosis_id,
            "diagnosis" : self.__diagnosis,
            "diagnosis_date" : self.__diagnosis_date     
        }
        
        return json.dumps(field_data)
        
    
                
                
class Procedure:
    def __init__(self, procedure_id="",procedure = "",procedure_date = ""):
        self.__procedure = procedure
        self.__procedure_date = procedure_date
       
        
        if procedure_id == "":
            self.__procedure_id = str(uuid.uuid4())
            
            try: 
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO PROCEDURE1 (diagnosis_id, procedure,procedure_date)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__procedure_id, self.__procedure,self.__procedure_date)) 
                    con.commit()
            finally:
                con.close()
                
        else:
            self.__procedure_id = procedure_id
            
            try:
                config = Config()
                con = config.db_conn
                    
                with con.cursor() as cur:
                    qry = "SELECT * FROM PROCEDURE1 WHERE procedure_id = '" + procedure_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    
                    for row in rows:
                        self.__procedure_id = row["procedure_id"]
                        self.__procedure = row["procedure"]
                        self.__procedure_date = row["procedure_date"]
                        
            finally:
                con.close()
    
    def get_procedure_id(self):
        return self.__diagnosis_id
    
    def get_procedure(self):
        return self.__diagnosis
    
    def get_procedure_date(self):
        return self.__diagnosis_date
    
    def set_procedure(self):
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE Procedure1 SET procedure = %s WHERE procedure_ID = %s;'
                print(qry)
                cur.execute(qry, (self.__procedure, self.__procedure_id)) 
                con.commit()
        finally:
            con.close()
            
    def delete_entry(self):
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'DELETE FROM Procedure WHERE procedure_id = %s;'
                print(qry)
                cur.execute(qry, (self.__procedure_id)) 
                con.commit()
        finally:
            con.close()   
            
    def to_json(self):
        field_data = {
            "id" : self.__procedure_id,
            "diagnosis" : self.__procedure,
            "diagnosis_date" : self.__procedure_date     
        }
        
        return json.dumps(field_data)       




                

    

            
        
        
