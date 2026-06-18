from faker import Faker
from faker_vehicle import VehicleProvider
import random
import datetime

def cars_generator(count):
    
    fake = Faker()
    random.seed(0)
    fake.add_provider(VehicleProvider)
    fake.seed_instance(0)
    cars = []
    
    for _ in range(count):
        
        car = fake.vehicle_year_make_model().split()[:3]
        make = car[1]
        model = car[2]
        year = int(car[0])
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        fabrication_date = datetime.datetime(year, month, day).strftime('%Y-%m-%d')
        price = round(random.uniform(10000, 40000), 2)
        cars.append((make, model, price, fabrication_date))
        
    return cars

#print(cars_generator(2))