"""
Midpoint Formula Program
v1.0/v2026.4.27b

will add 3d when i actually have time
 
(c) Boss_1s. Refer to license in main.py
"""
import math

ask = "2" #input("2D -> [2]; 3D -> [3]")

if ask == "2":
  x1 = int(input("Enter the value of x1: "))
  y1 = int(input("Enter the value of y1: "))
  x2 = int(input("Enter the value of x2: "))
  y2 = int(input("Enter the value of y2: "))
  
  calcx, calcy = ((x2+x1)/2, (y2+y1)/2)
  print(f"\033[32mAnswer: ({calcx}, {calcy})")
  print(f"\033[34mWork:\n"+
        f"M=(({x2} + {x1})/2, ({y2} + {y1})/2)\n"+
        f"M=(({x2 + x1})/2, ({y2 + y1})/2)\n"+
        f"M=({(x2 + x1)/2}, {(y2 + y1)/2})\n"
       )
"""
elif ask == "3":
  x1 = int(input("Enter the value of x1: "))
  y1 = int(input("Enter the value of y1: "))
  z1 = int(input("Enter the value of z1: "))
  x2 = int(input("Enter the value of x2: "))
  y2 = int(input("Enter the value of y2: "))
  z2 = int(input("Enter the value of z2: "))
  
  calc = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2))
  print(f"\033[32mAnswer: {calc}")
  print(f"\033[34mWork:\nd=√({x2} - {x1})^2 + ({y2} - {y1})^2 + ({z2} - {z1})^2\nd=√{x2 - x1}^2 + {y2 - y1}^2 + {z2 - z1}^2")
  print(f"d=√{(x2 - x1) ** 2} + {(y2 - y1) ** 2} + {(z2 - z1) ** 2}\nd=√{(x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2}\nd={calc}\033[0m")
"""