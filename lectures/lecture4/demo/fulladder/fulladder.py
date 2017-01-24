import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
for i in range(3):
    icestick.J1[i].input().on()
icestick.D1.on()
icestick.D2.on()

main = icestick.main()

def and2(a, b):
    return And2()(a,b)

def or3(a,b,c):
    return Or3()(a,b,c)

def xor3(a,b,c):
    return Xor3()(a,b,c)

def FullAdder(a,b,c):
    S = xor3(a,b,c)
    C = or3(and2(a,b),and2(b,c),and2(c,a))
    return S, C

S, C = FullAdder(main.J1[0],main.J1[1],main.J1[2])

wire( S, main.D1 )
wire( C, main.D2 )

compile(sys.argv[1], main)
