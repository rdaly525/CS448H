import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
for i in range(8):
    icestick.J1[i].input().on()
for i in range(4):
    icestick.J3[i].output().on()

main = icestick.main()

def And(n):
     def f(y):
         return And2()
     return join( col(f, n) )

a = And(4)
print a.interface
a(main.J1[0:4], main.J1[4:8])

wire(a.O, main.J3)

compile(sys.argv[1], main)
