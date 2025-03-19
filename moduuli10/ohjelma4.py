#!/usr/bin/env python3

# Muutin nimet englanniksi, ei kai haittaa

import random

class Car:
    def __init__(self, registration, top_speed):
        self.registration = registration
        self.top_speed = top_speed
        self.speed = 0
        self.traveled = 0
    
    # Muutin nyt englanniksi kuin en tykkää ääkkösistä funktionimissä
    def accelerate(self, change):
        self.speed = min(self.top_speed, max(self.speed + change, 0))

    def travel(self, time):
        self.traveled += self.speed * time

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
        self.time = 0

    def tick(self):
        for car in self.cars:
            car.accelerate( random.randint(-10, +15) )
            car.travel(1)
        self.time += 1

    def print(self):
        print_header()
        print_cars(self.cars)

    def is_finished(self):
        for car in self.cars:
            if car.traveled >= self.distance:
                return True
        return False

def print_header():
    print(f"{'Registration':<20} {'Top speed':<15} {'Speed':15} {'Traveled':15}")

def print_cars(cars):
    for car in cars:
        print(f"{car.registration:<20} "
              f"{str(car.top_speed)+' km/h':<15} "
              f"{str(car.speed)+' km/h':<15} "
              f"{str(car.traveled)+' km':<15}"
        )

def main():
    print_header()

    cars = []

    for i in range(10):
        cars.append( Car(f"ABC-{i+1}", random.randint(100, 200)) )

    race = Race("Suuri Romuralli", 8000, cars)

    while not race.is_finished():
        race.tick()
        if race.time % 10 == 0:
            race.print()
    race.print()

    

if __name__ == "__main__":
    main()
