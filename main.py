import math

print("Divide 8/3")
print(8 / 3)  # float value. In this case it will be 2.66666666

print("Divide with floor option.")
print(math.floor(8 / 3))  # rouding down value
print(8 // 3)

print("Divide with round option")
print(round(8 / 3))
print(round(8 / 3, 2))

print("Divide with trunc option")
print(math.trunc(8 / 3))

print("Divide with ceil option")
print(math.ceil(8 / 3))

print("Mod % option")
print(9 % 4)

print("Fraction")
from fractions import Fraction

print(Fraction(11, 35))
# returns Fraction(11, 35)

print(Fraction(10, 18))
# returns Fraction(5, 9)

print(Fraction())
# returns Fraction(0, 1)

print(Fraction(-5, 12))
# returns Fractions(-5, 12)

# print(Fraction(2/0))
# devide by 0. ZeroDivision error.
result = Fraction(13, 4) + Fraction(11, 18) + Fraction(3, 19)
print(result)

from decimal import Decimal
# Decimal
print("Decimal")
print(Decimal(12) / Decimal(4))
print(Decimal(4) / Decimal(12))
result = Decimal(12) + Decimal(4) + Decimal(-4) - Decimal(7) / Decimal(9)
print(result)
