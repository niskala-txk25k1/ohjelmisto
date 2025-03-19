#!/usr/bin/env python3

# Muutin nimet englanniksi, ei kai haittaa

class Elevator:
    def __init__(self, floor_min, floor_max):
        self.floor_min = floor_min
        self.floor_max = floor_max
        self.floor = floor_min
    
    def move_to_floor(self, target):
        target = min(self.floor_max, max(target, self.floor_min))
        while self.floor != target:
            if self.floor < target:
                self.move_up()
            else:
                self.move_down()

    def move_up(self):
        self.floor = min(self.floor_max, max(self.floor+1, self.floor_min))

    def move_down(self):
        self.floor = min(self.floor_max, max(self.floor-1, self.floor_min))


class House:
    def __init__(self, floor_min, floor_max, elevator_count):
        self.elevators = []
        self.floor_min = floor_min
        self.floor_max = floor_max
        for i in range(elevator_count):
            self.elevators.append( Elevator(floor_min, floor_max) )

    def move_elevator(self, index, floor):
        self.elevators[index].move_to_floor(floor)
 
    def fire_alarm(self):
        print("Fire alarm!")
        for elevator in self.elevators:
            elevator.move_to_floor(self.floor_min)
            
    def print(self):
        print(f"Elevators:")
        for elevator in self.elevators:
            print(f"{elevator.floor}")


def main():
    house = House(1, 10, 2)
    house.print()
    house.move_elevator(0, 4)
    house.print()
    
    house.fire_alarm()
    house.print()

if __name__ == "__main__":
    main()
