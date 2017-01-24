import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
for i in range(6):
    icestick.J3[i].output().on()

main = icestick.main()

def Counter(n):
    add = [FullAdder() for i in range(n)]
    reg = [DFF() for i in range(n)]

    CIN = 1
    O = []
    for i in range(n):
        wire(reg[i].O, add[i].I0)
        wire(0, add[i].I1)
        wire(CIN, add[i].CIN)
        CIN = add[i].COUT
        wire(add[i].O, reg[i].I)
        O.append(reg[i].O)
    return array(*O), CIN

count, cout = Counter(4)

wire(main.CLKIN, main.J3[0])
wire(count, main.J3[1:5])
wire(cout, main.J3[5])

compile(sys.argv[1], main)

