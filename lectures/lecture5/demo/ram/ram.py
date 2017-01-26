from magma import *
from mantle import *

def REGs(n):
    return [Register(8, ce=True) for i in range(n)]

def MUXs(n):
    return [Mux(2,8) for i in range(n)]

def readport(logn, regs, raddr):
    n = 1 << logn

    muxs = MUXs(n-1)
    for i in range(n/2):
        muxs[i](regs[2*i], regs[2*i+1], raddr[0])

    k = 0
    l = 1 << (logn-1)
    for i in range(logn-1):
        for j in range(l/2):
            muxs[k+l+j](muxs[k+2*j], muxs[k+2*j+1], raddr[i+1])
        k += l
        l /= 2

    return muxs[n-2]

def writeport(logn, regs, WADDR, I, WE):
    n = 1 << logn

    decoder = Decoder(logn)
    enable = And(2,1<<logn)
    enable(decoder(WADDR), array(*(n*[WE])))

    for i in range(n):
        regs[i](I, CE=enable.O[i])

def RAM(logn, RADDR, WADDR, I, WE):
    assert len(RADDR) == logn
    assert len(WADDR) == logn

    regs = REGs(1 << logn)
    writeport(logn, regs, WADDR, I, WE)
    return readport(logn, regs, RADDR)

def DualRAM(logn, RADDR0, RADDR1, WADDR, I, WE):
    assert len(RADDR0) == logn
    assert len(RADDR1) == logn
    assert len(WADDR) == logn

    regs = REGs(1 << logn)
    writeport(logn, regs, WADDR, I, WE)
    return readport(logn, regs, RADDR0), readport(logn, regs, RADDR1)
