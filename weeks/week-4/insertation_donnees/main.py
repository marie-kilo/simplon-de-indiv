from sql_tables import CarsDatabase

cars_db = CarsDatabase("postgres", "11223355")

cars_db.create_cars_database()