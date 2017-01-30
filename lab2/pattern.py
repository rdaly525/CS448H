import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.D1.on()
#Uncomment following lines to use other LEDs
#icestick.D2.on()
#icestick.D3.on()
#icestick.D4.on()
#icestick.D5.on()

main = icestick.main()

#Your code here.

#Delete the following line
wire(1, main.D1)


compile(sys.argv[1], main)
