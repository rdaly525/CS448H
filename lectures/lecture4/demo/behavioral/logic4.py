import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
for i in range(4):
    icestick.J1[i].input().on()
icestick.D5.on()

main = icestick.main()

def alu(A, B, S0, S1):
    if S1:
        if S0: return A^B
        else:  return A&B
    else:
        if S0: return A|B
        else:  return B

logic = ROM4(alu)

wire( logic(main.J1), main.D5 )

compile(sys.argv[1], main)

