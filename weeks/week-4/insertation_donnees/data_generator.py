{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "907c46e6-faaa-4660-9a07-ae39be2175c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "from faker import Faker\n",
    "from faker_vehicle import VehicleProvider\n",
    "import random\n",
    "import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "805a5a17-d1e3-4af4-9bb9-04ee2a67281c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cars_generator(count):\n",
    "    \n",
    "    fake = Faker()\n",
    "    random.seed(0)\n",
    "    fake.add_provider(VehicleProvider)\n",
    "    fake.seed_instance(0)\n",
    "    cars = []\n",
    "    \n",
    "    for _ in range(count):\n",
    "        \n",
    "        car = fake.vehicle_year_make_model().split()[:3]\n",
    "        make = car[1]\n",
    "        model = car[2]\n",
    "        year = int(car[0])\n",
    "        month = random.randint(1, 12)\n",
    "        day = random.randint(1, 28)\n",
    "        fabrication_date = datetime.datetime(year, month, day)\n",
    "        price = round(random.uniform(10000, 40000), 2)\n",
    "        cars.append((make, model, price, fabrication_date))\n",
    "        \n",
    "    return cars\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "8803a3ed-770c-49f8-9415-2d3d05355f9d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from pprint import pprint"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "90ba345c-e949-411f-a926-558f310ed4aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('Ford', 'E350', 17767.5, datetime.datetime(2003, 7, 2, 0, 0)),\n",
      " ('Land', 'Rover', 37547.03, datetime.datetime(1996, 8, 13, 0, 0)),\n",
      " ('Ford', 'Mustang', 27501.46, datetime.datetime(2007, 8, 12, 0, 0)),\n",
      " ('INFINITI', 'FX', 18455.14, datetime.datetime(2011, 9, 5, 0, 0)),\n",
      " ('Audi', 'Q3', 17515.19, datetime.datetime(2016, 10, 26, 0, 0))]\n"
     ]
    }
   ],
   "source": [
    "pprint(cars_generator(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f58885de-3b7e-450f-b36e-80502d73ac57",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
