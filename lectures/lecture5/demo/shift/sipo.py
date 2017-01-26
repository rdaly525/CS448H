import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('I').input().on()
for i in range(8):
    icestick.J3[i].output().on()

main = icestick.main()

def DefineSIPO(n):
    """
    Generate Serial-In, Parallel-Out shift register.

    I : Bit -> O : Array(n, Bit)
    """

    class _SIPO(Circuit):
        name = 'SIPO'+str(n)
        IO = ['I', In(Bit), 'O', Out(Array(n,Bit))] + ClockInterface()

        @classmethod
        def definition(sipo):
            ffs = FFs(n)
            reg = braid(ffs, scanargs={"I":"O"})
            wire(sipo.I, reg.I)
            wire(reg.O, sipo.O)
            wireclock(sipo, reg)

    return _SIPO

SIPO8 = DefineSIPO(8)
sipo8 = SIPO8()

sipo8(main.I)
wire(sipo8, main.J3)

compile(sys.argv[1], main)
