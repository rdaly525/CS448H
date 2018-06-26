from magma import *
from mantle import *
from rom import ROM
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
for i in range(2):
    icestick.J3[i].output().on()

main = icestick.main()

clock = CounterModM(103, 8)
baud = clock.COUT

wire(main.CLKIN, main.J3[0])
wire(baud,       main.J3[1])


