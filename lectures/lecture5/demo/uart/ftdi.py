import sys
from magma import *
from mantle import *
from rom import ROM
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.TX.output().on()

main = icestick.main()

valid = 1

init = [array(*int2seq(ord(c), 8)) for c in 'hello, world  \r\n']

printf = Counter(4, ce=True)
rom = ROM(4, init, printf.O)

data = array(rom.O[7], rom.O[6], rom.O[5], rom.O[4],
             rom.O[3], rom.O[2], rom.O[1], rom.O[0], 0 )

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

shift = PISO(9, ce=True)
load = LUT2(I0&~I1)(valid,run)
shift(1,data,load)
wire(baud, shift.CE)

ready = LUT2(~I0 & I1)(run, baud)
wire(ready, printf.CE)

wire(shift, main.TX)

compile(sys.argv[1], main)

