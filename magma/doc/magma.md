Magma is a low-level language embedded in python for building circuits.

There are two steps in creating a circuit with Magma.
The first step involves involves instantiating circuits
from their definitions.
The second step involves wiring the instantiated circuits together.

The best way to lean Magma is through examples. 
In class, we have shown many examples.
The examples also show how to use Magma with the
Lattice IceStick Board.

Magma has built-in circuit definitions for hardware primitives in FPGAs.
The two common low-level primitives in FPGAs 
are lookup tables (LUTs)
and D-flip-flops (FFs).

The following code snippet
```
logic1 = LUT2(I0&I1)
logic2 = LUT2(I0|I1)
```
will create two 2-input lookup tables,
one that implements the logical AND function
and the other that implements the OR function.
There are also functions to create LUTs
corresponding to 1, 2, 3, or 4 bits
(`LUT1`, `LUT2`, `LUT3`, and `LUT4`).

`LUT2` is a python function 
that instantiates and configures a hardware lookup table.
Each invocation of `LUT2` instantiates a new lookup table.
The value returned by `LUT2` and refers to that hardware lookup table.
The hardware lookup table is a combinational logic function
that computes an output value as a function of its input values.
Combinational logic functions are not the same as python functions.
A python function runs immediately on the host computer.
The hardware function is implemented in the lookup table functional unit
that runs on the FPGA.
When writing Magma programs,
it is important to keep in mind whether 
a function is a python function or a hardware functional unit.

The contents of the lookup table is configured 
to compute the given logical expresson.
There are multiple ways to do this.
Recall, that a 4-bit logic function can be represented as a 16-bit number.
Each bit in this number correponds to the output of the LUT
for the corresponding input value when treated as a number between 0 and 15..
The AND function can be initialized using the
16-bit number 0x8000. 
The number 0x8000 has 0's in its first 15 positions
(corresponding to the input values 0 to 14)
and 1 in position 15
(which means that the output will be 1 if all the
input bits are 1, corresponding an input of 15).
To create a function of only the first two bits,
replicate a 4-bit pattern. 
The 16-bit number 0x8888 will correspond to an
AND of the first two bits, since the values of the
third and fourth bit do not effect the result.

There is a simple bit twiddling trick to create
these 16-bit values.
Magma defines the following symbolic constants
`I0`, `I1`, `I2`, and `I3`.
The 16-bit number corresponding to a given logical
expression can be formed by using a python logical expression.
In the example above,
we formed the AND function using `I0&I1` 
and the OR function using `I0|I1`.

A third way to specify the logical function is to explicitly give
the truth table as a python sequence.
The list `[0,0,0,1]` would specify the AND function.
The 4th way to specify the LUT function
is to pass in a function of n argments.
This function is called for each possible bit pattern.
If the function returns 0, then the truth value is 0;
if it returns 1, then the truth value is 1. 

The other common low-level hardware primitive on an FPGA is the D flip-flop,
```
dff = DFF()
```
This instanatiates a single DFF on the FPGA.

#### Wiring Functional Units

The circuits created above have the following interfaces
```
print logic1.interface
I0 : In(Bit), I1 : In(Bit) -> O : Out(Bit)
print logic2.interface
I0 : In(Bit), I1 : In(Bit) -> O : Out(Bit)
print dff.interface
I : In(Bit), CLK : In(Bit) -> O : Out(Bit)
```
The first two print outs describe combinational circuits
with two inputs `I0` and `I1`
and one output `O`.
The inputs and outputs have type `Bit`.
Note that types are qualified to be either inputs (`In`) or outputs (`Out`).
The third print out describes a flip-flop.
Besides an input and an output,
this circuit has a clock `CLK`.

The next step is to wire functional units together 
to create more complex circuits.
This involves connecting the outputs of circuits
to the inputs of other circuits.

There are two ways to wire circuits in Magma.
The first uses the `wire` function.
```
wire( SWITCH0, logic1.I0 )
wire( SWITCH1, logic1.I1 )
wire( logic1.O, LED0 )
```
The inputs and outputs of a circuit
are named attributes of the instantiated circuit.
Here, we assume that `SWITCH0`, `SWITCH1` and `LED0` are predefined.

The second way to wire circuits is to use the function call syntax.
```
logic1( SWITCH0, SWITCH1 )
```
This statement will wire the arguments to the inputs of the function.
In this example, 
the first statement wires `SWITCH0` and `SWITCH1` 
to the `I0` and `I1` of the `logic1` function.

We can easily wire the output of `logic1` to `dff`.
```
dff ( logic1( switch1, switch2 ) )
```
Note the nested calls. 
When wiring a circuit using the function call syntax,
the outputs are returned.
These outputs can be passed to the inputs of another circuit
(the above works since the `logic1` has one output
and `dff` has one input).

Note that instantiated circuits can only be wired once.
Magma will generated a warning if you try to wire the inputs
more than once.
