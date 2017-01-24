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

def Add(A, B):
    n = len(A)
    add = [FullAdder() for i in range(n)]

    CIN = 0
    O = []
    for i in range(n):
        wire(A[i], add[i].I0)
        wire(B[i], add[i].I1)
        wire(CIN, add[i].CIN)
        CIN = add[i].COUT
        O.append(add[i].O)
    return array(*O), CIN

sum, cout = Add(main.J1[0:4], main.J1[4:8])

wire(sum, main.J3[0:4])
wire(cout, main.J3[4])

compile(sys.argv[1], main)
