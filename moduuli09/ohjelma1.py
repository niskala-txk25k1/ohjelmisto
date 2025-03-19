#!/usr/bin/env python3

class Auto:
    def __init__(self, registration, top_speed):
        self.registration = registration
        self.top_speed = top_speed
        self.speed = 0
        self.traveled = 0
    
def print_cars(cars):
    print(f"{'Registration':<20} {'Top speed':<15} {'Speed':15} {'Traveled':15}")
    for car in cars:
        print(f"{car.registration:<20} "
              f"{str(car.top_speed)+' km/h':<15} "
              f"{str(car.speed)+' km/h':<15} "
              f"{str(car.traveled)+' km':<15}"
        )

def main():
    car = Auto("ABC-123", 142)
    print_cars([car])

if __name__ == "__main__":
    main()
