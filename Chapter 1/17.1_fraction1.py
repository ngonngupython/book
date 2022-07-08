class Fraction:
  def __init__(self, numerator, denominator):
    self.num = numerator
    self.den = denominator

  def plus(self, another_fraction):
    cd=self.den * another_fraction.den
    cn = self.nu * another_fraction.den + self.den * another_fraction.num
    return Fraction(cn, cd)

  def __str__(self):
    return str(self.num) + "/" + str(self.den)

f1 = Fraction(1, 2)
f2 = Fraction(2, 3)
# Khi muốn cộng hai phân số, phải định nghĩa hàm rộng plus
print(f1.plus(f2))
