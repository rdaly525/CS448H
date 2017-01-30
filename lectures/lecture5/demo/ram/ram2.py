import sys
from magma import *
from mantle import *
from ram import RAM
from boards.icestick import IceStick

LOGN = 2

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('RADDR[0]').input().on()
icestick.J1[1].rename('RADDR[1]').input().on()
icestick.J1[2].rename('WADDR[0]').input().on()
icestick.J1[3].rename('WADDR[1]').input().on()
icestick.J1[4].rename('I0').input().on()
icestick.J1[5].rename('I1').input().on()
icestick.J1[6].rename('WE').input().on()
for i in range(8):
    icestick.J3[i].output().on()


main = icestick.main()
I = array(main.I0, main.I1, 0, 0, 0, 0, 0, 0)

rom = RAM(LOGN, main.RADDR, main.WADDR, I, main.WE)

wire(rom, main.J3)

compile(sys.argv[1], main)
