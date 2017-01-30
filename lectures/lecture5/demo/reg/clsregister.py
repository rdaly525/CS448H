import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
for i in range(8):
    icestick.J1[i].input().on()
for i in range(8):
    icestick.J3[i].output().on()

main = icestick.main()

def DefineRegister(n):
    """
    Generate an n-bit register
    
    I : Array(n, Bit) -> O : Array(n, Bit)
    """ 
    
    T = Array(n, Bit)
    class _Register(Circuit):
        name = 'Register'+str(n)
        IO  = ['I', In(T), 'O', Out(T), "CLK", In(Bit)]

        @classmethod
        def definition(reg):
            ffs = join(FFs(n))
            wire(reg.I, ffs.I) 
            wire(ffs.O, reg.O)
            wire(reg.CLK, ffs.CLK)
    return _Register

Register8 = DefineRegister(8)
register8 = Register8()

wire(register8(main.J1), main.J3)

compile(sys.argv[1], main)
