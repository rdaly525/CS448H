import os

# utility
from magma.bits import *
from magma.bitwise import *

# lowest-level wiring abstraction
from magma.port import *

# types
from magma.t import *
from magma.bit import *
from magma.array import *
from magma.tuple import *
from magma.interface import *

from magma.wire import *
from magma.circuit import *

from magma.peripheral import *
from magma.part import *
from magma.fpga import *

from magma.board import *

# verilog 
from magma.verilog import *
from magma.higher import *

if os.getenv("MAGMA_COMPILE_STYLE") == "abstract":
    from magma.compile_abstract import *
else:
    from magma.compile import *


