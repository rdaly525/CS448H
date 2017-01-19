#!/usr/bin/python
#Example usage: ./lut4.py "((I0&I1)^I2)|I3"
import sys

I0 = 0b1010101010101010
I1 = 0b1100110011001100
I2 = 0b1111000011110000
I3 = 0b1111111100000000

print(hex(eval(sys.argv[1])))
