import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
for i in range(4):
    icestick.J1[i].input().on()
icestick.D5.on()

main = icestick.main()

lut4 = LUT4(I0&I1&I2&I3)

lut4(main.J1[0], main.J1[1], main.J1[2], main.J1[3])

wire( lut4, main.D5 )

compile(sys.argv[1], main)
