import math

def solveVarWhich():
  choice = input("Solve for a, b, or c? ")
  choices = ["a", "b", "c"]
  if not choice in choices:
    solveVarWhich()
  else:
    return choice

choice = solveVarWhich()
if not choice == "a":
  a = int(input("Enter the 'a' value of triangle.\n"))
  if a <= 0:
    raise ValueError("Length cannot be less than or equal to zero.")
 
if not choice == "b": 
  b = int(input("Enter the 'b' value of triangle.\n"))
  if b <= 0:
    raise ValueError("Length cannot be less than or equal to zero.")

if not choice == "c":
  c = int(input("Enter the 'c' value of triangle.\n"))
  if c <= 0:
    raise ValueErrorError("Length cannot be less than or equal to zero.")

if choice == "a":
  work = f"a^2 + {b}^2 = {c}^2"
  b = b ** 2
  c = c ** 2
  work = work + f"\na^2 + {b} = {c}\na^2 (+ {b} - {b}) = {c} - {b}"
  c = c - b
  work = work + f"\na^2 = {c}\n√a^2 = √{c}"
  c = math.sqrt(c)
  work = work + f"\na = {c}"
elif choice == "b":
  work = f"{a}^2 + b^2 = {c}^2"
  a = a ** 2
  c = c ** 2
  work = work + f"\n{a} + b^2 = {c}\n({a} - {a}) + b^2 = {c} - {a}"
  c = c - a
  work = work + f"\nb^2 = {c}\n√b^2 = √{c}"
  c = math.sqrt(c)
  work = work + f"\nb = {c}"
else:
  work = f"{a}^2 + {b}^2 = c^2"
  a = a ** 2
  b = b ** 2
  work = work + f"\n{a} + {b} = c^2"
  c = a + b
  work = work + f"\n{c} = c^2\n√{c} = √c^2"
  c = math.sqrt(c)
  work = work + f"\n{c} = c"

print(f"\033[32mAnswer: {c}")
print(f"\033[34mWork: \n{work}\033[0m")
  
  