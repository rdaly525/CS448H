NAME = counter

DEVICE = 1k
QUIET = -q

PNR=arachne-pnr
#PNR=~/git/arachne-pnr-fork/bin/arachne-pnr

$(NAME).bin: $(NAME).v $(PCF)
	yosys $(QUIET) -p 'synth_ice40 -top main -blif $(NAME).blif' $(NAME).v
	$(PNR) $(QUIET) -d $(DEVICE) -o $(NAME).txt -p $(NAME).pcf \
       --post-pack-blif $(NAME).pack.blif \
       --post-place-blif $(NAME).place.blif \
       $(NAME).blif 
	icepack $(NAME).txt $(NAME).bin

upload: $(NAME).bin
	iceprog $(NAME).bin

explain: top.txt
	icebox_explain $<

timing:
	icetime -d hx$(DEVICE) -t $(NAME).txt

verilog:
	echo "read_verilog $(NAME).v"        > synth.scr
	echo "synth_ice40 -top main"        >> synth.scr
	echo "write_verilog $(NAME).synth.v" >> synth.scr
	yosys $(QUIET) -s synth.scr

floorplan:
	yosys $(QUIET) -p 'synth_ice40 -top main -blif $(NAME).blif' $(NAME).v
	$(PNR) $(NAME).blif --post-place-blif $(NAME).place.blif -d 8k 
	yosys -q -o $(NAME).place.json $(NAME).place.blif

show:
	yosys -q -p 'show -format dot -prefix counter' counter.v
	dot -T ps -o counter.ps counter.dot
	convert counter.ps counter.png
	open counter.png


%.vv: %.blif
	echo "read_blif $<"      > synth.scr
	echo "write_verilog $@" >> synth.scr
	yosys $(QUIET) -s synth.scr

%.ilang: %.blif
	echo "read_blif $<"    > synth.scr
	echo "write_ilang $@" >> synth.scr
	yosys $(QUIET) -s synth.scr

clean:

clean:
	rm -f *.bin *.txt *.blif *.json *.vv


.PRECIOUS: %.bin %.txt %.blif 

.PHONY: all explain install clean
