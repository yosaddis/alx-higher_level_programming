#!/usr/bin/python3
import calculator_1 as cal

a = 10
b = 5

add_str = str(a) + " + " + str(b)
sub_str = str(a) + " - " + str(b)
mul_str = str(a) + " * " + str(b)
div_str = str(a) + " / " + str(b)

print(add_str + " = {:d}".format(cal.add(int(a), int(b))))
print(sub_str + " = {:d}".format(cal.sub(int(a), int(b))))
print(mul_str + " = {:d}".format(cal.mul(int(a), int(b))))
print(div_str + " = {:d}".format(cal.div(int(a), int(b))))
