# Gettting Started with the Icestick

The Icestick is a small FPGA with an open-source tool chain.

### Icestorm tools

To install the icestorm tools,
go to the [project icestorm](http://www.clifford.at/icestorm/} web site
and follow the instructions under "How to Install the Tools".
You will need to install

* icestorm tools for generating bitstreams and programming the icestick
* arachne-pnr for placing and routing 
* yosys verilog synthesis tool

These programs should be installed in a public bin directory.

Note that if you are using a Mac,
follow these [instruction](http://www.clifford.at/icestorm/notes_osx.html).

###Installation Gotchas

Packages people have needed

```
Bison
pkg-config
libffi
```

Bison Error

```
frontends/ilang/ilang_lexer.l:33:10: fatal error: 'ilang_parser.tab.h' file not found \#include "ilang_parser.tab.h"
```



Make sure you have the Bison package installed.

One annoying problem on the Mac is the FTDI drivers.
There are three different FTDI drivers for OSX:
(1) Apple's driver,
(2) FTDI's driver,
and (3) the open-source ftdi driver.
In order to use the icestorm programmer,
you need to uninstall the Apple and FTDI drivers.
To see which driver is currently installed, run

```
kextstat | fgrep FTDI
```

And then remove the one that is installed.

```
% sudo kextunload -b com.FTDI.driver.FTDIUSBSerialDriver
% sudo kextunload -b com.apple.driver.AppleUSBFTDI
```

These drivers are installed on boot,
and may need to be installed if you reboot.



To build a bitstream for the icestick, run make.

```
% make
yosys -q -p 'synth_ice40 -top main -blif counter.blif' counter.v
arachne-pnr -q -d 1k -o counter.txt -p counter.ucf counter.blif 
icepack counter.txt counter.bin
```
`yosys` is the verilog synthesizer. It creates a file called "counter.blif".  
`arachne-pnr` is the place and router. It takes as input "counter.blif" and produces an ascii bit stream file "counter.txt".  
`icepack` converts the ascii bit stream file
to a binary bit stream file "counter.bin"

Now plug in your icestick, and upload the the bitstream file.  
If this fails, verify that you have removed the installed FTDI driver.

```
% make upload
iceprog counter.bin
```

The LED on the icestick should blink approximately 3 times per second.

Congratulations, everything is installed correctly and working!
