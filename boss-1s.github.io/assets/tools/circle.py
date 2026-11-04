#Fix c,cs,as work output (5/6/25)
#Fix cs radius & as -> work product (5/7/25)
import math
import warnings

print("\033[33m"+
      "RuntimeWarning: WARNING! When calculating sector circumference "+
      "with radius and sector area with radius and/or d"+
      "iameter, work will not output properly. Please "+
      "do not take that work seriously.\033[0m")

dante = input("circumference -> [c]; area -> [a]; sector(circumference) -> [cs]; sector(area) -> [as]")
pi = input("Use 3.14 for pi? Yes[Y] No[N] ")
if pi == "y" or pi =="Y":
  pi = 3.14
elif pi == "n" or pi == "N":
  pi = math.pi
else:
  pi = math.pi

if dante == "c":
  # C = πd or C = 2πr
  radius = input("Enter radius. Leave blank for diameter. ")
  if radius == "":
    diameter = float(input("Enter diameter. "))
    print(f"\033[32mAnswer: {diameter * pi}")
    print(f"\033[34mWork: {diameter} * π\n{diameter * pi}\033[0m")
  else:
    radius = float(radius)
    print(f"\033[32mAnswer: {2 * radius * pi}")
    print(f"\033[34mWork: 2 * {radius} * π\n{2 * radius} * π\n{2 * radius * pi}\033[0m")
    
elif dante == "a":
  # A = π(d/2)^2 or A = πr^2
  radius = input("Enter radius. Leave blank for diameter. ")
  if radius == "":
    diameter = float(input("Enter diameter. "))
    print(f"\033[32mAnswer: {((diameter/2) ** 2) * pi}")
    print(f"\033[34mWork: ({diameter} / 2) ^ 2 * π\n{diameter/2} ^ 2 * π\n{(diameter/2) ** 2} * π\n{((diameter/2) ** 2) * pi}\033[0m")
  else:
    radius = float(radius)
    print(f"\033[32mAnswer: {(radius ** 2) * pi}")
    print(f"\033[34mWork: {radius} ^ 2 * π\n{radius ** 2} * π\n{(radius ** 2) * pi}\033[0m")
    
elif dante == "cs":
  # C = (a/360)πd or C = (a/360)2πr
  radius = input("Enter radius. Leave blank for diameter. ")
  if radius == "":
    diameter = float(input("Enter diameter. "))
    a = float(input("Enter angle."))
    print(f"\033[32mAnswer: {(a/360) * diameter * pi}")
    print(f"\033[34mWork: ({a}/360) * {diameter} * π\n{a/360} * {diameter} * π\n{(a/360)*diameter} * π\n{(a/360) * diameter * pi}\033[0m")
  else:
    radius = float(radius)
    a = float(input("Enter angle."))
    print(f"\033[32mAnswer: {(a/360) * 2 * radius * pi}")
    print(f"\033[34mWork: ({a}/360) * 2 * {radius} * π\033[0m")
    
elif dante == "as":
    # A = (a/360)π(d/2)^2 or A = (a/360)πr^2
  radius = input("Enter radius. Leave blank for diameter. ")
  if radius == "":
    diameter = float(input("Enter diameter. "))
    a = float(input("Enter angle."))
    print(f"\033[32mAnswer: {(a/360) * ((diameter/2) ** 2) * pi}")
    print(f"\033[34mWork: ({a}/360) * ({diameter} / 2) ^ 2 * π\033[0m")
  else:
    radius = float(radius)
    a = float(input("Enter angle."))
    print(f"\033[32mAnswer: {(a/360) * (radius ** 2) * pi}")
    print(f"\033[34mWork: ({a}/360) * {radius} ^ 2 * π\033[0m")
