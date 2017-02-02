# Gettting Started with Magma and Mantle on the Icestick

Add magma to your PYTHONPATH

```
export PYTHONPATH=$PYTHONPATH:<YOUR_PATH>/CS448H/magma
```

Magma uses a build system based on `fabricate`.
Download and install the 
[fabricate build environment](https://github.com/SimonAlfie/fabricate).
The file `fabricate.py` 
should be installed in site-packages for your version of python.



Then try to build and run the blink program

```
% cd blink
% . doit
```

The script, `doit` builds the program `blink.py` 
That script is pretty simple,

```
% cat doit
export MANTLE=lattice
export MANTLE_TARGET=ice40
./bake clean
./bake
%
```
To use the icestick board with Magma,
you need to set the MANTLE and MANTLE_TARGET environment variables.

```
% export MANTLE=lattice
% export MANTLE_TARGET=ice40
```
These variables causes magma to use the lattice ice40 version
of the mantle library.

The build script is called `bake`.
`bake` is like `make`, but it uses `fabricate`.

The output of the build script is placed in the `build` directory.
```
% cd build
% ls
Makefile
blink.ucf
blink.v
```

From here, run the program on the icestack the same as lab1

to clean the build dir, do 
``` 
make clean
```

to clean magma generated files
```
./bake clean
```

