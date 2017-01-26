import sys
from magma import *
from mantle import *
from rom import ROM
from boards.icestick import IceStick

icestick = IceStick()
for i in range(4):
    icestick.J1[i].input().on()
for i in range(8):
    icestick.J3[i].output().on()

LOGN = 4

main = icestick.main()

init = []
for i in range(1<<LOGN):
    init.append( array(*int2seq(i, 8)) )

rom = ROM(LOGN, init, main.J1)

wire(rom, main.J3)

compile(sys.argv[1], main)
