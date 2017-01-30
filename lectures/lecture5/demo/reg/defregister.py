import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick = IceStick()
icestick.Clock.on()
for i in range(8):
    icestick.J1[i].input().on()
for i in range(8):
    icestick.J3[i].output().on()

main = icestick.main()

def FFs(n):
    def f(y):
        return DFF()
    return join(col(f, n))

def DefineRegister(n):
    reg = DefineCircuit('Register'+str(n),
               "I",   In(Array(n,Bit)),
               "CLK", In(Bit),
               "O",   Out(Array(n,Bit)))

    ffs = FFs(n)
    wire(ffs(reg.I), reg.O)
    wire(reg.CLK, ffs.CLK)

    EndCircuit()
    return reg

Register8 = DefineRegister(8)
register8 = Register8()

wire(register8(main.J1), main.J3)

compile(sys.argv[1], main)
