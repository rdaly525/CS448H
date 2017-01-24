import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on() # need to turn the clock on
icestick.J1[0].rename('I').input().on()
icestick.D5.on()

main = icestick.main()

# create ff holding state first
ff = FF()

# lut computes the next state ...
#  function of the previous state and the input
lut = LUT2( I0^I1 )
lut(main.I, ff)

# lut computes the next state
ff(lut)

wire( ff, main.D5 )

compile(sys.argv[1], main)
