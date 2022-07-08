class Fraction2:
  def __init__(self, numerator, denominator):
    self.num = numerator
    self.den = denominator

  def __add__(self, another_fraction):
    cd = self.den * another_fraction.den
    cn = self.num * another_fraction.den + self.den * another_fraction.num
    return Fraction(cn, cd)

  def __str__(self):
    return str(self.num) + "/" + str(self.den)

f1 = Fraction2(1, 2)
f2 = Fraction2(2,3)
print(f1+f2)     # sử dụng được + như ký hiệu toán học.
