import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
for i in range(4):
    icestick.J1[i].input().on()
icestick.D5.on()

main = icestick.main()

logic = ROM4([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1])

wire( logic(main.J1), main.D5 )

compile(sys.argv[1], main)

