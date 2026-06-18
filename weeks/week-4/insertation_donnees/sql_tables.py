import psycopg2
import psycopg2.extras
from io import StringIO
import pandas as pd
from sqlalchemy import create_engine

class CarsDatabase:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        
    def create_cars_database(self):
        try:
            # Connexion à PostgreSQL
            conn = psycopg2.connect(
                user=self.user,
                password=self.password,
                host="localhost",
                port=5432)
            
            conn.autocommit = True
            cur = conn.cursor()

            # Pour pouvoir ré exécuter le code
            cur.execute("DROP DATABASE IF EXISTS cars_db;")

            # Création d'une nouvelle base de données
            cur.execute("CREATE DATABASE cars_db;")
            print("Database created successfully.")

            # Connexion à la nouvelle base de données
            conn.close()


        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL database: {e}")
            
    def connect_to_cars_database(self):
        try:
            conn = psycopg2.connect(
                dbname="cars_db",
                user=self.user,
                password=self.password,
                host="localhost",
                port=5432)
                                
            print("Connection réuissi à la base de données cars")

        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL database: {e}")
            
        return conn
            

class Cars:
    def __init__(self, conn):
        self.conn = conn
    
    def create_table_cars(self):
        cur = self.conn.cursor()
        
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS cars (
                        id SERIAL PRIMARY KEY,
                        make VARCHAR(30),
                        model VARCHAR(30),
                        price NUMERIC(7, 2),
                        fabrication_date DATE
                    ); 
        """)
        self.conn.commit()
        
    def delete_cars_table(self):
        cur = self.conn.cursor()
        cur.execute("DROP TABLE IF EXISTS cars")
        self.conn.commit()
        
    def insert_car(self, car):
        cur = self.conn.cursor()
        
        cur.execute("""
                    INSERT INTO cars
                        (make, model, price, fabrication_date)
                        Values (%s, %s, %s, %s); 
                    """, car)
                            
    def insert_many_cars(self, cars_list):
        
        cur = self.conn.cursor()
        
        cur.executemany("""
                    INSERT INTO cars
                        (make, model, price, fabrication_date)
                        Values (%s, %s, %s, %s);
                    """, cars_list)

        self.conn.commit()
        
    def count_cars(self):
        
        cur = self.conn.cursor()
        cur.execute("""
                    SELECT COUNT(*)
                    FROM cars
                    """    
                )
        return cur.fetchone()[0]
    
    def insert_cars_with_batch(self, cars_list):
        cur = self.conn.cursor()
        query = """
                    INSERT INTO cars
                        (make, model, price, fabrication_date)
                        Values (%s, %s, %s, %s);
                """
        psycopg2.extras.execute_batch(cur, query, cars_list, page_size=100)
        self.conn.commit()
        
    def insert_cars_with_values(self, cars_list):
        cur = self.conn.cursor()
        query = """
                    INSERT INTO cars
                        (make, model, price, fabrication_date)
                        Values %s;
                """
        psycopg2.extras.execute_values(cur, query, cars_list, page_size=1000)
        self.conn.commit()
        
    def insert_cars_with_copy(self, cars_list):
        cur = self.conn.cursor()
        buffer = StringIO()

        for row in cars_list:
            buffer.write(','.join(map(str, row)) + '\n')

        buffer.seek(0)

        cur.copy_expert("""
            COPY cars (make, model, price, fabrication_date)
            FROM STDIN
            WITH CSV
        """, buffer)
        self.conn.commit()
        
    def insert_cars_with_pandas_to_sql(self, cars_df, engine):
        
        cars_df.to_sql(
            "cars",
            engine,
            if_exists="append",
            index=False
        )
        
    def insert_cars_with_pandas_to_sql_multi(self, cars_df, engine):
        
        cars_df.to_sql(
            "cars",
            engine,
            if_exists="append",
            index=False,
            method="multi",
            chunksize=500
        )