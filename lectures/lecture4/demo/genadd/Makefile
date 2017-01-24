NAME = addn

PCF = icestick.pcf

DEVICE = 1k
QUIET = -q

$(NAME).bin: $(NAME).v $(PCF)
	yosys $(QUIET) -p 'synth_ice40 -top main -blif $(NAME).blif' $(NAME).v
	arachne-pnr $(QUIET) -d $(DEVICE) -o $(NAME).txt -p $(PCF) $(NAME).blif
	icepack $(NAME).txt $(NAME).bin

upload: $(NAME).bin
	iceprog $(NAME).bin

timing:
	icetime -d hx$(DEVICE) -t $(NAME).txt

clean:
	rm -f *.bin *.txt *.blif *.rpt

.PHONY: all explain install clean
