from sql_tables import CarsDatabase, Cars
from data_generator import cars_generator
import time
from statistics import median
from sqlalchemy import create_engine


import pandas as pd

# 1000 / 100 000 / 1 000 000
data_size = 1000000
# liste du temps d'execution de chaque methode

def main():

    cars_db = CarsDatabase("postgres", "Mkilo1990")
    # Creer une base de donnees cars_db si elle n'existe pas
    cars_db.create_cars_database()
    # Connexion a la base des donnees "cars_db"
    conn = cars_db.connect_to_cars_database()
    
    cars_table = Cars(conn)
    # Suprission de la table "cars" si elle existe
    cars_table.delete_cars_table()
    # Creation de la table cars
    cars_table.create_table_cars()
    # Generation d'une liste des voitures 
    cars_data = cars_generator(data_size)
    
    df = pd.DataFrame(
                cars_data,
                columns=["make", "model", "price", "fabrication_date"]
    )
    
    engine = create_engine(
            "postgresql+psycopg2://postgres:Mkilo1990@localhost:5432/cars_db"
        )
    
    method1 = []
    method2 = []
    method3 = []
    method4 = []
    method5 = []
    method6 = []
    method7 = []
    method8 = []
    
    for j in range(10):
        """
        # Tester la methode 1
        ###################################################
        start = time.perf_counter()
        for car in cars_data:
            cars_table.insert_car(car)
            conn.commit()
            
        end = time.perf_counter()
        method1.append(end - start)
        #################################################
        cars_table.delete_cars_table()
        cars_table.create_table_cars()
        
        # Tester la methode 2 
        #################################################
        start = time.perf_counter()
        for car in cars_data:
            cars_table.insert_car(car)

        conn.commit()
            
        end = time.perf_counter()
        method2.append(end - start)
        #################################################
    
        cars_table.delete_cars_table()
        cars_table.create_table_cars()
        
        # Tester la methode 3
        #################################################
        start = time.perf_counter()

        cars_table.insert_many_cars(cars_data)
        
        end = time.perf_counter()
        method3.append(end - start)
        #################################################
        """
        
        cars_table.delete_cars_table()
        cars_table.create_table_cars()
        
        # Tester la methode 4
        #################################################
        start = time.perf_counter()
        cars_table.insert_cars_with_batch(cars_data)
        end = time.perf_counter()
        method4.append(end - start)
        #################################################
        
        cars_table.delete_cars_table()
        cars_table.create_table_cars()
        
        # Tester la methode 5
        #################################################
        start = time.perf_counter()
        cars_table.insert_cars_with_values(cars_data)
        end = time.perf_counter()
        method5.append(end - start)
        #################################################
        
        cars_table.delete_cars_table()
        cars_table.create_table_cars()
        
        # Tester la methode 6
        #################################################
        start = time.perf_counter()
        cars_table.insert_cars_with_copy(cars_data)
        end = time.perf_counter()
        method6.append(end - start)
        
        #################################################
        
        cars_table.delete_cars_table()
        cars_table.create_table_cars()
        
        # Tester la methode 7
        #################################################
        start = time.perf_counter()
        cars_table.insert_cars_with_pandas_to_sql(df, engine)
        end = time.perf_counter()
        method7.append(end - start)
        
        #################################################
        
        cars_table.delete_cars_table()
        cars_table.create_table_cars()
        
        # Tester la methode 8
        #################################################
        start = time.perf_counter()
        cars_table.insert_cars_with_pandas_to_sql_multi(df, engine)
        end = time.perf_counter()
        method8.append(end - start)
        
   # print(f"temps d'execution methode 1: {round(median(method1), 3)} seconds")
    #print(f"temps d'execution methode 2: {round(median(method2), 3)} seconds")
   # print(f"temps d'execution methode 3: {round(median(method3), 3)} seconds")
    print(f"temps d'execution methode 4: {round(median(method4), 3)} seconds")
    print(f"temps d'execution methode 5: {round(median(method5), 3)} seconds")
    print(f"temps d'execution methode 6: {round(median(method6), 3)} seconds")
    print(f"temps d'execution methode 7: {round(median(method7), 3)} seconds")
    print(f"temps d'execution methode 8: {round(median(method8), 3)} seconds")

    
    #print(f"temps d'execution methode : {end - start:.3f} seconds")
    #print(f"nombre des lignes: {cars_table.count_cars()}\n")
    
    conn.close()
    
if __name__ == "__main__":
    main()
    
