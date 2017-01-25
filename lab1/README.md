#LAB1
Welcome to the first lab!


You will be building a Johnson Counter and a decoder in structural verilog, and should be able to see it running on your icestick!

###Due date: 
Friday 1/27 at 11:59pm

###Instructions:
First, go through the icestick tutorial and make sure you get the blink program running on your own machine. Also make sure you understand each step of the tool chain.

Next you will create a verilog implementation of a 4-bit Johnson Counter and a Decoder that will produce a 3-bit binary integer.

####Johnson Counter:
An N-bit Johnson Counter is a simple circular shift-register circuit that cycles through 2N unique states. You create it by connecting the inverted output of the last bit into the input of the first bit. Check the png for an example 4-bit johnson counter. This will correctly cycle through 2N states, but these states are not encoded as the binary integer that we want. 

####Decoder:
This decoder will take in the N bits of the Johnson Counter and produce a binary integer (of bitsize (log2(2N)).


For example, Here is a 3-bit Johnson Counter cycling through all of its states.  
jcounter -> decoded value  
0 0 0    -> 0  
1 0 0    -> 1  
1 1 0    -> 2  
1 1 1    -> 3  
0 1 1    -> 4  
0 0 1    -> 5  
0 0 0	  -> 0  
1 0 0    -> 1
...



One cool thing about a Johnson Counter is that any state transition only changes 1 bit! This is called a Hamming distance of 1. What could this be useful for?

Feel free to read more about Johnson Counters on Wikipedia.

###Rules:

1. Make sure that all of your code exists in jcounter-4bit.v
2. Do not change any module definition and implement the johnson counter in 'module jcounter' and the decoder in 'module decoder'
3. Only use structural hardware! This means:
  * You can **only**: define modules, instantiate modules, connect wires, and connect constants. 
  * You **cannot** use: always/initial blocks, logical/arithmetic operations (+,-,&,|,^,<<,==, etc...), or verilog primitive modules (and,or,xor,not,etc...). This will be checked for during grading.  
  * You can instantiate any ice40 primitive defined in doc/SBTICETechnologyLibrary201504.pdf
4. The jcounter should shift about once or twice per second (does not need to be exact)
5. The power-on state (seed) of the jcounter should be 4'hF (all ones). Remember this should actually decode to the value 4 (3'b100).
6. Connect all the bits of the decoded jcounter to the outputs D3-D1 (jcounter[0] to D1 ... jcounter[2] to D3)  
7. Verify that your design runs correctly by checking the LEDs. You should be able to see the LEDs counting up in binary. 

###Hints: 
  * Try to write higher level psuedo code before connecting things together. 
  * Think modular! What new modules can you define to make this easier?
  * Drawing out the circuit is always helpful!
  * You can use your icestick to verify sub-components of your design! 
  * We do not have a reset signal in our design. Is there a way to create a flip-flop that logically powers on to 1?
  * The clock frequency is 12MHz  
  * Notice ways in which it would be nice to be able to metaprogram some (or all) aspects of the design. This will be helpful for the next assingment and your project!  

###Grading.
A script will be run to verify:
  
  * Functional correctness of the johnson counter with seed 4'hF shifting ~once per second
  * The correct use of structural verilog
  * The ability to run the program on an icestick
    

###Submission Instructions
	
1. Log into corn ```<ssid>@corn.stanford.edu```
2. Create a local directory ```mkdir tmp; cd tmp```
3. Create a README with your ssid ```echo '<ssid>' > README```
4. Copy jcounter-4bit.v into this directory
5. Copy any bonus files you implimented (jcounter-16bit.v, jcounter_bonus.v)
6. Create a file called writeup.txt with a few sentences describing your apporach to the problem, any challenges you faced, and any ideas of language features to make this lab easier to express.
7. Run: ```python /afs/ir/class/cs448h/bin/submit1.py```
8. Verify that your files are in ```/afs/ir/class/cs448h/submissions/lab1```
9. Rejoice and get excited for the magma lab!

###Bonus
(1) How could we build a larger (16-bit) Johnson Counter? We cannot use simple lookup table tricks because the lookup table would have to be on the order of 2^16 bits!!
  One major hint is the fact that only 1 bit changes at a time, and not only that but the location of that 'edge' fully encodes what value the johnson counter should be!
  
  * Please implement this in jcounter-16bit.v.
  * Change the NAME var in the makefile to jcounter-16bit

(2) What happens if we want to change the seed to the Johnson Counter? Can you come up with a design that will work by simply just changing the parameter 'SEED'?
  
   * If you decide to try this, please submit a seperate file named jcounter_bonus.v.
   * You can define new parameters and do arbitrary logical/arithmetic computations on them, but still **not** on wires.
