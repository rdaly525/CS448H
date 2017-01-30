#LAB2
Welcome to the second lab!

###Due date: 
Monday 2/6 at 11:59pm

###Instructions:
First, make sure you get magma running on your computer (magma/READEME.md) and can run blink on your icestick. 

Next you will create visually pleasing patterns using your LEDs.

####Setting the LED Brightness
You have been using your LEDs in just two states: On or Off (0 or 1). Can we set the brightness of the LED to be somewhere in between on and off? Brightness is related to average voltage applied to the LED. Since we only have two voltage values, 0 and 1, how do we get a value in between?

####Pulse Width Modulation
From your previous lab, you were probably able to output bit 24 or 25 of a counter to see the LED blinking on and off. What happens when you output bit 8 or even bit 1? We get a dimmer LED, not quite as bright as being full on, and not off. So what is happening here? Our eyes cannot cannot detect the quick changes to the LED so we perceive the *average* brightness.

So what is bit 8 of the counter doing? It really is just a cyclic square wave with a frequency of 47kHz and a Duty cycle of 50%.
A Duty cycle just tells us what percentage of the period the signal is 1. 

So can what would we do to create an even dimmer LED? 
If we had a way to adjust the Duty cycle to 25%, then we could produce an even dimmer LED!

What does an N bit counter look like if you graph time on the X axis and Value (between 0 and Max=2^N) on the Y axis? It looks like a sawtooth wave! What happens if you graph the function ```Output = (Counter < (0.25)*Max)```? You will get our desired 25% duty cycle! Check out the graph in PWM25.png to see this. 

Now how do we fade an LED from off to on? You can just slowly change the value which you are comparing to the counter! In fact you can create any arbitrary function for how the brightness of the light behaves over time.

####Actual Lab
 This is a more open ended lab. You will be creating some sort of simple visually pleasing dynamic pattern on the LEDs. 

###Rules:

1. Make sure that all of your code exists in pattern.py
2. You need to use at least 4 of your LEDs to create a fun visually pleasing smooth-changing pattern. I have provided an example of what I am looking for in the video ```circle.mov```.
3. Each LED should have slightly different behavior.
4. At least one of your LEDs should change its brightness according to a sin or cos wave. (Since this function is continuous, there should be NO discrete jumps in brightness)
5. Even though you will need to discretize the functions, they should be perceived to be continuous.
6. Verify that your design can be compiled via Magma and run on your icestick 

###Hints: 
  * You have the full capabilities of Python (meta-programming, closures, first class functions, etc). Use it to your advantage!
  * Think of how to use LUTs/ROMs in order to quantize and encode functions such as sin or cos. 
  * Try to user higher order magma functions like fork, join, braid, col, etc. These will make your life easier!
  * For coming up with patterns, take advantage of the fact that the LEDs are spaced in somewhat of a grid.


###Grading.
  * The ability to compile from magma and run on an icestick
  * Following all the rules
    

###Submission Instructions
	
1. Log into corn ```<ssid>@corn.stanford.edu```
2. Create a local directory ```mkdir tmp; cd tmp```
3. Create a README with your ssid ```echo '<ssid>' > README```
4. Copy pattern.py (and scaling.py if you did it) into this directory
5. Create a file called writeup.txt with a few sentences describing your apporach to the problem, any challenges you faced, and any ideas of features to make this lab easier to express.
6. Run: ```python /afs/ir/class/cs448h/bin/submit2.py```
7. Verify that your files are in ```/afs/ir/class/cs448h/submissions/lab2```
8. Rejoice and start thinking about project ideas!

###Bonus
(1) You dont just have to have one dynamic pattern on the LEDs, but you could cycle through multiple different dynamic patterns to create a show!
(2) Unfortunately voltage to perceived brightness of an LED is not completely 1 to 1. Fortunately LED manufactures provide graphs describing the characteristics of the physical component. Try to take these graphs into account to show *brightness* scaling linearly from 0 to 1. Put this in a new file called scaling.py
