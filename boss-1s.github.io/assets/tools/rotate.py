import math

rd = ["radians", "degrees"]
ask1 = "2"# = input("2D or 3D rotation? 2D[2] 3D [3] "), DONT UNCOMMENT
ask2 = input("rad mode or deg mode? Default is deg. rad[0] deg[1] ")
if ask2 == "":
  actualrd = rd[1]
else:
  actualrd = rd[int(ask2)]

if ask1 == "2":
  #--------------------------
  #Formula if (xo, yo) = (0, 0)
  #x' = x * cos(θ) - y * sin(θ)
  #y' = x * sin(θ) + y * cos(θ)
  #Formula if (xo, yo) not = (0, 0)
  #x' = xo + (x - xo) * cos(θ) - (y - yo) * sin(θ)
  #y' = yo + (x - xo) * sin(θ) + (y - yo) * cos(θ)
  #--------------------------
  idk = ["", 0]
  x = float(input("Enter the value of x(the original x-value): "))
  y = float(input("Enter the value of y(the original y-value): "))
  xo = input("Enter the value of xo(the x-value to be rotated around) - leave blank for (0,0): ")
  if not xo in idk:
    yo = input("Enter the value of yo(the y-value to be rotated around) - leave blank for (0,0): ")
    if yo == "":
      yo == 0
      mode = "orgin"
    else:
      xo = float(xo)
      yo = float(yo)
      mode = "abritary"
  elif xo == "":
    xo = 0
    yo = 0
    mode = "orgin"
  else:
    mode = "abritary"
  a = float(input(f"Enter the value of the angle of rotation. Must be in {actualrd}: "))
  if mode == "orgin" and actualrd == "radians":
    xfinal = x * math.cos(a) - y * math.sin(a)
    yfinal = x * math.sin(a) + y * math.cos(a)
    xwork = f"\033[34mWork for x-coords:\n{x} * cos({a} {actualrd}) - {y} * sin({a} {actualrd})\n"
    xwork = xwork + f"{x} * {math.cos(a)} - {y} * {math.sin(a)}\n"
    xwork = xwork + f"{x * math.cos(a)} - {y} * {math.sin(a)}\n"
    xwork = xwork + f"{x * math.cos(a)} - {y * math.sin(a)}\n"
    xwork = xwork + f"{x * math.cos(a) - y * math.sin(a)}\n\033[0m"
    ywork = f"\033[34mWork for y-coords:\n{x} * sin({a} {actualrd}) + {y} * cos({a} {actualrd})\n"
    ywork = ywork + f"{x} * {math.sin(a)} + {y} * {math.cos(a)}\n"
    ywork = ywork + f"{x * math.sin(a)} + {y} * {math.cos(a)}\n"
    ywork = ywork + f"{x * math.sin(a)} + {y * math.cos(a)}\n"
    ywork = ywork + f"{x * math.sin(a) + y * math.cos(a)}\033[0m"
    print(f"\033[32mAnswer: ({xfinal}, {yfinal})")
    print(xwork)
    print(ywork)
  elif mode == "orgin" and actualrd == "degrees":
    xfinal = x * math.cos(math.radians(a)) - y * math.sin(math.radians(a))
    yfinal = x * math.sin(math.radians(a)) + y * math.cos(math.radians(a))
    xwork = f"\033[34mWork for x-coords:\n{x} * cos({a} {actualrd}) - {y} * sin({a} {actualrd})\n"
    xwork = xwork + f"{x} * {math.cos(math.radians(a))} - {y} * {math.sin(math.radians(a))}\n"
    xwork = xwork + f"{x * math.cos(math.radians(a))} - {y} * {math.sin(math.radians(a))}\n"
    xwork = xwork + f"{x * math.cos(math.radians(a))} - {y * math.sin(math.radians(a))}\n"
    xwork = xwork + f"{x * math.cos(math.radians(a)) - y * math.sin(math.radians(a))}\n\033[0m"
    ywork = f"\033[34mWork for y-coords:\n{x} * sin({a} {actualrd}) + {y} * cos({a} {actualrd})\n"
    ywork = ywork + f"{x} * {math.sin(math.radians(a))} + {y} * {math.cos(math.radians(a))}\n"
    ywork = ywork + f"{x * math.sin(math.radians(a))} + {y} * {math.cos(math.radians(a))}\n"
    ywork = ywork + f"{x * math.sin(math.radians(a))} + {y * math.cos(math.radians(a))}\n"
    ywork = ywork + f"{x * math.sin(math.radians(a)) + y * math.cos(math.radians(a))}\n\033[0m"
    print(f"\033[32mAnswer: ({xfinal}, {yfinal})")
    print(xwork)
    print(ywork)
  elif mode == "abritary" and actualrd == "radians":
    xfinal = xo + (x - xo) * math.cos(a) - (y - yo) * math.sin(a)
    yfinal = yo + (x - xo) * math.sin(a) + (y - yo) * math.cos(a)
    xwork = f"\033[34mWork for x-coords:\n"
    xwork = xwork + f"{xo} + ({x} - {xo}) * cos({a}) - ({y} - {yo}) * sin({a})\n"
    xwork = xwork + f"{xo} + {x - xo} * cos({a}) - {y - yo} * sin({a})\n"
    xwork = xwork + f"{xo + (x - xo)} * cos({a}) - {y - yo} * sin({a})\n"
    xwork = xwork + f"{xo + (x - xo)} * {math.cos(a)} - {y - yo} * {math.sin(a)}\n"
    xwork = xwork + f"{xo + (x - xo) * math.cos(a)} - {y - yo} * {math.sin(a)}\n"
    xwork = xwork + f"{xo + (x - xo) * math.cos(a)} - {(y - yo) * math.sin(a)}\n"
    xwork = xwork + f"{xo + (x - xo) * math.cos(a) - (y - yo) * math.sin(a)}\n\033[0m"
    ywork = f"\033[34mWork for x-coords:\n"
    ywork = ywork + f"{xo} + ({x} - {xo}) * sin({a}) + ({y} - {yo}) * cos({a})\n"
    ywork = ywork + f"{xo} + {x - xo} * sin({a}) + {y - yo} * cos({a})\n"
    ywork = ywork + f"{xo + (x - xo)} * sin({a}) + {y - yo} * cos({a})\n"
    ywork = ywork + f"{xo + (x - xo)} * {math.sin(a)} + {y - yo} * {math.cos(a)}\n"
    ywork = ywork + f"{xo + (x - xo) * math.sin(a)} + {y - yo} * {math.cos(a)}\n"
    ywork = ywork + f"{xo + (x - xo) * math.sin(a)} + {(y - yo) * math.cos(a)}\n"
    ywork = ywork + f"{xo + (x - xo) * math.sin(a) + (y - yo) * math.cos(a)}\n\033[0m"
    print(f"\033[32mAnswer: ({xfinal}, {yfinal})")
    print(xwork)
    print(ywork)
  elif mode == "abritary" and actualrd == "degrees":
    xfinal = xo + (x - xo) * math.cos(math.radians(a)) - (y - yo) * math.sin(math.radians(a))
    yfinal = yo + (x - xo) * math.sin(math.radians(a)) + (y - yo) * math.cos(math.radians(a))
    print(f"\033[32mAnswer: ({xfinal}, {yfinal})")
