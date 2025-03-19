#!/usr/bin/env python3

class Auto:
    def __init__(self, registration, top_speed):
        self.registration = registration
        self.top_speed = top_speed
        self.speed = 0
        self.traveled = 0
    
    # Muutin nyt englanniksi kuin en tykkää ääkkösistä funktionimissä
    def accelerate(self, change):
        self.speed = min(self.top_speed, max(self.speed + change, 0))
    
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
    car = Auto("ABC-123", 142)
    print_header()

    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    print_cars([car])
    car.accelerate(-200)
    print_cars([car])

if __name__ == "__main__":
    main()
