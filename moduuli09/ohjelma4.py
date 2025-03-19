#!/usr/bin/env python3

import random

class Auto:
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
    
def print_header():
    print(f"{'Registration':<20} {'Top speed':<15} {'Speed':15} {'Traveled':15}")

def print_cars(cars):
    for car in cars:
        print(f"{car.registration:<20} "
              f"{str(car.top_speed)+' km/h':<15} "
              f"{str(car.speed)+' km/h':<15} "
              f"{str(car.traveled)+' km':<15}"
        )


def race(cars):
    while True:
        for car in cars:
            car.accelerate( random.randint(-10, +15) )
            car.travel(1)
            if car.traveled >= 10_000:
                return

def main():
    print_header()

    cars = []

    for i in range(10):
        cars.append( Auto(f"ABC-{i+1}", random.randint(100, 200)) )

    race(cars)
    print_cars(cars)
    

if __name__ == "__main__":
    main()
