import psycopg2

USER = "postgres"
PASSWORD = "11223355"

class CarsDatabase:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.connected = False
        self.cur = ""
        self.conn = ""
        
    def create_cars_database(self):
        try:
            # Connexion à PostgreSQL
            conn = psycopg2.connect(user=self.user, password=self.password, host="localhost", port=5432)
            conn.autocommit = True
            cur = conn.cursor()
            self.conn = conn
            self.cur = cur
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
        
            conn.autocommit = True
            self.connected = True
                        
            print("Connection réuissi à la base de données cars")

        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL database: {e}")
            
        return conn
            
    def close_connect(self):
        if self.connected:
            self.cur.close()
            self.conn.close()
            
            

class Cars:
    def __init__(self, conn):
        self.conn = conn
    
    def create_table_car(self):
        self.conn.autocommit = True
        cur = self.conn.cursor()
        
        cur.execute("""
                    CREATE TABLE cars (
                        id SERIAL PRIMARY KEY,
                        make VARCHAR(30),
                        model VARCHAR(30),
                        price NUMERIC(7, 2),
                        fabrication_date DATE
                    ); 
        """)
        
    def insert_car(self, car):
        self.conn.autocommit = True
        cur = self.conn.cursor()
        
        cur.execute("""
                    INSERT INTO cars
                        (make, model, price, outfit_colors, fabrication_date)
                        Values (?, ?, ?, ?) 
                    """, car)
                            
    def insert_many_cars(self, cars_list):
        
        self.conn.autocommit = True
        cur = self.conn.cursor()
        
        cur.executemany("""
                    INSERT INTO cars
                        (make, model, price, outfit_colors, fabrication_date)
                        Values (?, ?, ?, ?) 
                    """, cars_list)
