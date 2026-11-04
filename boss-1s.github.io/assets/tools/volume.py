import math
#V=Bh, B varies

figure = int(input("Rectanglular Prism[1] Triangular Prism[2] Pyramid[3] Cone[4] Sphere[5] Cylinder[6] "))
work = "\033[34mWork:\n"
pis = [4, 5, 6]

if figure in pis:
  askpi = input("Use 3.14 for pi? Yes[Y] No[N] ")
  if askpi == "Y" or askpi == "y":
    pi = 3.14
  else:
    pi = math.pi



if figure == 1:
  #V=lwh
  #B=lw
  B = input("Enter base area. Leave blank to key in individual base length and base width. ")
  if B == "":
    bl = float(input("Enter base length. "))
    bw = float(input("Enter base width. "))
    area = True
    B = bw * bl
  else:
    area = False
    B = float(B)
  h = float(input("Enter height. "))
  print(f"\033[32mAnswer: {B * h}")
  if area:
    work = work + f"{bl} * {bw} * {h}\n"
    work = work + f"{B} * {h}\n"
    work = work + f"{B * h}\033[0m"
  else:
    work = work + f"{B} * {h}\n"
    work = work + f"{B * h}\033[0m"
  print(work)
elif figure == 3:
  type = int(input("Square/Rectangular Base[0] Triangular Base[1] (For circular base, exit program and choose cone.) "))
  if type == 0:
    #V=(1/3)lwh
    #B=lw
    B = input("Enter base area. Leave blank to key in individual base length and base width. ")
    if B == "":
      bl = float(input("Enter base length. "))
      bw = float(input("Enter base width. "))
      area = True
      B = bw * bl
    else:
      area = False
      B = float(B)
    h = float(input("Enter height. "))
    print(f"\033[32mAnswer: {(1/3) * B * h} u^3")
    if area:
      work = work + f"(1/3) * {bl} * {bw} * {h}\n"
      work = work + f"{(1/3) * bl} * {bw} * {h}\n"
      work = work + f"{(1/3) * B} * {h}\n"
      work = work + f"{(1/3) * B * h} u^3\033[0m"
    else:
      work = work + f"(1/3) * {B} * {h}\n"
      work = work + f"{(1/3) * B} * {h}\n"
      work = work + f"{(1/3) * B * h} u^3\033[0m"
    print(f"\033[34m{work}\033[0m")
  elif type == 1:
    #V=(1/3)(bH/2)h
    #B=bh/2
    B = input("Enter base area. Leave blank to key in individual base length and base width. ")
    if B == "":
      bb = float(input("Enter base base. "))
      bh = float(input("Enter base height. "))
      area = True
      B = (1/2) * bb * bh
    else:
      area = False
      B = float(B)
    h = float(input("Enter height."))
    print(f"\033[32mAnswer: {(1/3) * B * h} u^3")
    if area:
      work = work + f"(1/3) * (1/2) * {bb} * {bh} * {h}\n"
      work = work + f"(1/3) * (1/2) * {bb * bh} * {h}\n"
    work = work + f"(1/3) * {B} * {h}\n"
    work = work + f"(1/3) * {B * h}\n"
    work = work + f"{(1/3) * B * h} u^3\033[0m"
    print(f"\033[34m{work}\033[0m")
elif figure == 5:
  #V=(4/3)πr^3
  #B=none
  radius = input("Enter radius. Leave blank for diameter. ")
  if radius == "":
    diameter = float(input("Enter diameter. "))
    print(f"\033[32mAnswer: {(4/3) * ((diameter/2) ** 3) * pi}")
    print(f"\033[34mWork: (4/3) * ({diameter} / 2) ^ 3 * π\n(4/3) * {diameter/2} ^ 3 * π\n(4/3) * {(diameter/2) ** 3} * π\n{(4/3) * (diameter/2) ** 3} * π\n{(4/3) * ((diameter/2) ** 3) * pi}\033[0m")
  else:
    radius = float(radius)
    print(f"\033[32mAnswer: {(4/3) * (radius ** 3) * pi}")
    print(f"\033[34mWork: (4/3) * {radius} ^ 3 * π\n(4/3) * {radius ** 3} * π\n{(4/3) * (radius ** 3)} * π\n{(4/3) * (radius ** 3) * pi}\033[0m")