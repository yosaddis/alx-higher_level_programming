#!/usr/bin/python3
import calculator_1 as cal

a = "10"
b = "5"

add_str = a + " + " + b
sub_str = a + " - " + b
mul_str = a + " * " + b
div_str = a + " / " + b

print(add_str + " = {:d}".format(cal.add(int(a), int(b))))
print(sub_str + " = {:d}".format(cal.sub(int(a), int(b))))
print(mul_str + " = {:d}".format(cal.mul(int(a), int(b))))
print(div_str + " = {:d}".format(cal.div(int(a), int(b))))
