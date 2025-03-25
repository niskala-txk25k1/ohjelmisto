#!/usr/bin/env python3

import numpy as np


print("Tehtävä 1.1")
print( np.degrees( 2.493 ) )
print( np.degrees( 0.911 ) )

print("\nTehtävä 1.2")
print( np.radians( 137.7 ) )
print( np.radians( 62.3 ) )


print("\nTehtävä 1.3")
degrees = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

print(f"Deg  | Rads")
for n in degrees:
    print(f"{n:<4} | {np.radians(n):0.4f}")




print("\nTehtävä 2")
# Kolmio

alpha = 43.3
a = 17.5

beta = 90 - alpha
b = a * np.tan(np.radians(beta))
c = np.sqrt( a**2 + b**2 )
print(c)

