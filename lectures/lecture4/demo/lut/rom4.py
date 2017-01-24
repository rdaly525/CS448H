import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
for i in range(4):
    icestick.J1[i].input().on()
icestick.D5.on()

main = icestick.main()

rom4 = ROM4(I0&I1&I2&I3)

rom4(main.J1)

wire( rom4, main.D5 )

compile(sys.argv[1], main)
