import os
import magma.verilog
import magma.blif

__all__ = ['compile']

def compileqsf(basename, fpga):
    file = open(basename+'.qsf','w')
    name = basename.split('/')
    code = fpga.qsf(name[-1])
    file.write(code)
    file.close()

def compilepcf(basename, fpga):
    file = open(basename+'.pcf','w')
    code = fpga.pcf()
    file.write(code)
    file.close()

def compileucf(basename, fpga):
    file = open(basename+'.ucf','w')
    code = fpga.ucf()
    file.write(code)
    file.close()

def compileverilog(basename, main):
    file = open(basename+'.v','w')
    code = magma.verilog.compile(main)
    file.write(code)
    file.close()
    #print('touch -m ' + basename + '.v')
    #os.system('touch -m ' + basename + '.v')

def compileblif(basename, main, origin):
    file = open(basename+'.blif','w')
    code = magma.blif.compile(main, origin)
    file.write(code)
    file.close()

def compile(basename, main, output='verilog', origin=None):
    assert output in ['blif', 'verilog']
    if output == 'verilog':
        compileverilog(basename, main)
    elif output == 'blif':
        compileblif(basename, main, origin)

    if hasattr(main, 'fpga'):
        vendor = os.getenv('MANTLE', 'lattice')
        if   vendor == 'altera':
            compileqsf(basename, main.fpga)
        elif vendor == 'xilinx':
            compileucf(basename, main.fpga)
        elif vendor == 'lattice':
            compilepcf(basename, main.fpga)

