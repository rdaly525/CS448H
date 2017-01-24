import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
for i in range(4):
    icestick.J1[i].input().on()
icestick.D5.on()

main = icestick.main()

print hex(I0), hex(I1), hex(I2), hex(I3)
A = I0
B = I1
S0 = I2
S1 = I3
eqn = ((S0&S1)&(A^B))|((~S0&S1)&(A&B))|((S0&~S1)&(A|B))|((~S0&~S1)&(B))
logic = ROM4(eqn)

wire( logic(main.J1), main.D5 )

compile(sys.argv[1], main)

