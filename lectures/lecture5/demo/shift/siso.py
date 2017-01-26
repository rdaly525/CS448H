import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('I').input().on()
icestick.J3[0].rename('O').output().on()

main = icestick.main()

def DefineSISO(n):
    """
    Generate Serial-In, Serial-Out shift register.

    I : Bit -> O : Bit
    """

    class _SISO(Circuit):
        name = 'SISO'+str(n)
        IO = ['I', In(Bit), 'O', Out(Bit)] + ClockInterface()

        @classmethod
        def definition(siso):
            ffs = FFs(n)
            reg = braid(ffs, foldargs={"I":"O"})
            reg(siso.I)
            wire(reg.O, siso.O)
            wireclock(siso, reg)

    return _SISO

SISO8 = DefineSISO(8)
siso8 = SISO8()

siso8(main.I)
wire(siso8, main.O)

compile(sys.argv[1], main)
