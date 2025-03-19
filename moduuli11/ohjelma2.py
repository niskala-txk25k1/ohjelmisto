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


class ElectricVehicle(Car):
    def __init__(self, registration, top_speed, battery_capacity):
        super().__init__(registration, top_speed)
        self.battery_capacity = battery_capacity

class GasVehicle(Car):
    def __init__(self, registration, top_speed, gas_capacity):
        super().__init__(registration, top_speed)
        self.gas_capacity = gas_capacity

def main():
    ev = ElectricVehicle("ABC-15", 180, 52.5)
    gv = ElectricVehicle("ACD-123", 165, 32.3)

    ev.accelerate(15)
    gv.accelerate(11)

    ev.travel(3)
    gv.travel(3)

    print(ev.traveled)
    print(gv.traveled)

if __name__ == "__main__":
    main()
