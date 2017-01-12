import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.J1[0].rename('J1[0]').input().on()
icestick.J1[1].rename('J1[1]').input().on()
icestick.J1[2].rename('J1[2]').input().on()
icestick.J1[3].rename('J1[3]').input().on()
icestick.J1[4].rename('J1[4]').input().on()
icestick.J1[5].rename('J1[5]').input().on()
icestick.J1[6].rename('J1[6]').input().on()
icestick.J1[7].rename('J1[7]').input().on()
icestick.J3[0].rename('J3[0]').output().on()
icestick.J3[1].rename('J3[1]').output().on()
icestick.J3[2].rename('J3[2]').output().on()
icestick.J3[3].rename('J3[3]').output().on()
icestick.J3[4].rename('J3[4]').output().on()
icestick.J3[5].rename('J3[5]').output().on()
icestick.J3[6].rename('J3[6]').output().on()
icestick.J3[7].rename('J3[7]').output().on()

main = icestick.main()

wire(main.J1, main.J3)

compile(sys.argv[1], main)
