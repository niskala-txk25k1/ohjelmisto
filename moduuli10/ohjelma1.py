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


def main():
    elevator = Elevator(0, 20)

    elevator.move_to_floor(21)
    print(elevator.floor)
    elevator.move_to_floor(-1)
    print(elevator.floor)

if __name__ == "__main__":
    main()
