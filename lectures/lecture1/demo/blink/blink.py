import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on() # default clock is 12Mhz
icestick.D5.on()

main = icestick.main()

N = 22

counter = Counter(N)
wire(counter.O[N-1], main.D5)

compile(sys.argv[1], main)
