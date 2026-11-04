"""
Quadratics

a simple script to get information about a quadratic
function given the values of a, b, and c in the
formula ax^2+bx+c

(c) 2026 Boss_1s. This work is licensed under
the CC BY-NC-SA 3.0 Int'l License. To view a copy of the license,
visit https://creativecommons.org.

v26.8.21
(8/21/2026)
"""


import math
from fractions import Fraction
from typing import Union

def find_factors(c):
  factor_list = []
  for number in range(int((c + 1) / 2)):
    if number == 0:
      continue
    if c % number == 0:
      factor_list.append((float(number), float(c / number),))

  return factor_list

def evaluate(a: Union[int, str],
             b: Union[int, str],
             c: Union[int, str]) -> None:
  a=float(Fraction(a)if'/'in a else a)
  b=float(Fraction(b)if'/'in b else b)
  c=float(Fraction(c)if'/'in c else c)
  d = (b**2)-4*a*c
  aos = (-b)/(2*a)
  
  print('\nequation:')
  print(
    'x='+
    f'-({b})±√(({b}^2)-4*{a}*{c})\n'+
    ('-'*len(f'-({b})±√(({b}^2)-4*{a}*{c})\n'))+
    f'\n2*{a}\n'
  )
  
  print('Domain: all reals')
  print(
    'Range: {y|y'+
    ('>' if a > 0 else '<')+
    str(aos)+
    '}'
  )
  print(f'Axis of Symmetry: x={aos}')
  print(f'Vertex: ({aos}, {(a*(aos**2))+(b*aos)+c})')
  
  print(f"solutions: {'0' if d < 0 else 'at least 1'}")
  print(f"discriminant: {d}\n")
  
  
  
  print('roots:')
  
  if d > 0:
    a2=2*a
    b2=math.sqrt((b**2)-4*a*c)
    if not '.0' in str(b2):
      print(f"{-b}±√({(b**2)-4*a*c})/{2*a}\n")
    print(
      ((-b)+math.sqrt((b**2)-4*a*c))/(2*a),
      ((-b)-math.sqrt((b**2)-4*a*c))/(2*a),
      sep=', '
    )
  elif d == 0:
    a2=((-b)+math.sqrt((b**2)-4*a*c))/(2*a)
    b2=((-b)-math.sqrt((b**2)-4*a*c))/(2*a)
    if a2 == b2:
      print(a2)
    else:
      raise RuntimeError("Something went wrong in calculating the single root.")
  else:
    print("no solution!")

  print("\n")

  if a > 1:
    print(f"Factoring quadratics with an 'a' value of {a} is not yet supported.")
    return
  
  c2 = a * c
  factors: list[tuple[int]] = find_factors(c2)
  factors.append((1.0,c2,))
  m = None
  p = None
  
  if not c2.is_integer:
    print(f"Factored form: Cannot factor due to decimals!")
    return

  c2 = int(c2)

  for item in factors:
    k = item[0]
    l = item[1]
    if k * l == c2 and k+l == b:
      m = k
      p = l
      break
  
  if m or p:
    if int(m) > 0 and not str(m).startswith('+'):
      m = '+' + str(m)
    if int(p) > 0 and not str(p).startswith('+'):
      p = '+' + str(p)
    print(f"Factored form: (x{m.removesuffix(".0")})(x{p.removesuffix(".0")})")
    return
  
  print(f"Factored form: Not factorable!")

if __name__ == "__main__":
  a=input('a: ')
  b=input('b: ')
  c=input('c: ')
  
  if a=='0':raise ValueError("the value of 'a' cannot be equal to zero.")
  if not a:a='1'
  if not b:b='0'
  if not c:c='0'
  evaluate(a, b, c)