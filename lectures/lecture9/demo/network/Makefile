NAME = and
PCF = icestick.pcf

DEVICE = 1k
QUIET = -q

PNR=arachne-pnr

$(NAME).bin: $(NAME).v $(PCF)
	yosys $(QUIET) -p 'synth_ice40 -top main -blif $(NAME).blif' $(NAME).v
	arachne-pnr $(QUIET) -d $(DEVICE) -o $(NAME).txt -p $(PCF) $(NAME).blif 
	icepack $(NAME).txt $(NAME).bin

explain: and.txt
	icebox_explain $<

verilog:
	icebox_vlog -p $(PCF) $(NAME).txt

clean:
	rm -f *.bin *.txt *.blif *.json *.vv

.PRECIOUS: %.bin %.txt %.blif 

.PHONY: all explain install clean
