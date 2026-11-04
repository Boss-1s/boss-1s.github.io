a = int(input("Enter the 'a' value of triangle.\n"))
if a <= 0:
  raise ValueError("Length cannot be less than or equal to zero.")

b = int(input("Enter the 'b' value of triangle.\n"))
if b <= 0:
  raise ValueError("Length cannot be less than or equal to zero.")

c = int(input("Enter the 'c' value of triangle.\n"))
if c <= 0:
  raise ValueError("Length cannot be less than or equal to zero.")
elif c <= a or c <= b:
  raise ValueError("Length of hypotenuse must be greater than the " +
                    "length of the legs, seperatly.")

if (c**2) == (a**2) + (b**2):
  print("\033[32mThis triangle is a right triangle.\033[0m")
else:
  print("\033[31mThis triangle is NOT a right triangle.\033[0m")

print(f"The numbers used to calculate were: {a ** 2}, {b ** 2}, and {c ** 2}.")
print(f"The equation used to calculate was: {a ** 2} + {b ** 2} ?= {c ** 2}.")