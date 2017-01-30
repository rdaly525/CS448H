import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
for i in range(8):
    icestick.J1[i].input().on()
for i in range(5):
    icestick.J3[i].output().on()

main = icestick.main()

def Add(n):
     def f(y):
         return FullAdder()
     return braid( col(f, n), foldargs={"CIN":"COUT"})

add = Add(4)
add(main.J1[0:4], main.J1[4:8])
wire(0, add.CIN)

wire(add.O, main.J3[0:4])
wire(add.COUT, main.J3[4])

compile(sys.argv[1], main)
