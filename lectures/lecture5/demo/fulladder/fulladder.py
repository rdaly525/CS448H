import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
for i in range(3):
    icestick.J1[i].input().on()
for i in range(2):
    icestick.J3[i].output().on()

main = icestick.main()

def FullAdder():
    return fork([ROM3(I0^I1^I2), 
                 ROM3((I0&I1)|(I1&I2)|(I2&I0))])

fa = FullAdder()
wire( fa(main.J1), main.J3 )

compile(sys.argv[1], main)
