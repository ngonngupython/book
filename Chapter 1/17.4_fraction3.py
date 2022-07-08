class Fraction:
  def __init__(self, numerator, denominator):
    self.numerator = numerator
    self.denominator = denominator

  def plus(self, another_fraction):
    common_denominator = self.denominator * another_fraction.denominator
    common_numerator = self.numerator * another_fraction.denominator + self.denominator * another_fraction.numerator
    return Fraction(common_numerator, common_denominator)

  def __str__(self):
    return str(self.numerator) + "/" + str(self.denominator)


f1 = Fraction(1, 2)
#print(f1)

f2 = Fraction(2, 3)
#print(f1.plus(f2))
#print(f1 + f2)


class Fraction3:
  def __init__(self, num, den):
    self.num = num
    self.den = den

  def __add__(self, other):
    common_den = self.den * other.den
    common_num = self.num * other.den + self.den * other.num
    return Fraction(common_num, common_den)

  def __gt__(self, other):
      return self.num * other.den > self.den * other.num

  def __lt__(self, other):
      return self.num * other.den < self.den * other.num

  def __eq__(self, other):
      return self.num * other.den == self.den * other.num


  def __str__(self):
    return str(self.num) + "/" + str(self.den)

f1 = Fraction3(1, 2)
f2 = Fraction3(2,3)
print(f1, ">", f2, f1 > f2)
print(f1, "<", f2, f1 < f2)
print(f1, "=", f2, f1 == f2)