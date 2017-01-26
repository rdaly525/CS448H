import sys
from magma import *
from mantle import *
from rom import ROM
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
for i in range(8):
    icestick.J3[i].output().on()

main = icestick.main()

valid = 1

clock = CounterModM(103, 8)
baud = clock.COUT

count = Counter(4, ce=True, r=True)
done = Decode(15, 4)(count)

run = DFF(ce=True)
run_n = LUT3([0,0,1,0, 1,0,1,0])
run_n(done, valid, run)
run(run_n)
wire(baud, run.CE)

reset = LUT2(I0&~I1)(done, run)
count(CE=baud, RESET=reset)

wire(main.CLKIN, main.J3[0])
wire(baud,       main.J3[1])
wire(run,        main.J3[2])
wire(done,       main.J3[3])
wire(count,      main.J3[4:8])

compile(sys.argv[1], main)

