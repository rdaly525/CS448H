NAME = and4
#NAME = andn4

#NAME = comb1
#NAME = comb2

#NAME = dff
#NAME = tff

#NAME = dffr

#NAME = always_comb1

#NAME = latch

#NAME = qqnonblocking
#NAME = qqblocking
#NAME = blocking
#NAME = shift

#NAME = always_comb2
#NAME = always_comb3

#NAME = race1
#NAME = race2
#NAME = race3
#NAME = race4

PCF = icestick.pcf

DEVICE = 1k
QUIET = -q

$(NAME).bin: $(NAME).v $(PCF)
	yosys $(QUIET) -p 'synth_ice40 -top main -blif $(NAME).blif' $(NAME).v
	arachne-pnr $(QUIET) -d $(DEVICE) -o $(NAME).txt -p $(PCF) $(NAME).blif
	icepack $(NAME).txt $(NAME).bin

upload: $(NAME).bin
	iceprog $(NAME).bin

clean:
	rm -f *.bin *.txt *.blif *.rpt

.PHONY: all explain install clean
