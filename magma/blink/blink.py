import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.D1.on()

main = icestick.main()

c = Counter(25)

wire(c.O[24], main.D1)

compile(sys.argv[1], main)
