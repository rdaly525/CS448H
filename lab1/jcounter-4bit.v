//You can Define additional Modules here.




module jcounter(input clk, output [3:0] out);
  //You do not need to use SEED for the main assignment. Just make sure the
  //power-on state is 4'hF
  parameter SEED=4'hF;

  //Your code here (delete the following line)
  assign out = SEED;

endmodule


module decoder(input [3:0] in, output [2:0] out);
  
  //Your code here (delete the following line)
  assign out = 3'b100;

endmodule


// Do not edit main!
module main(output D5, output D4, output D3, output D2, output D1, input CLKIN);
  parameter SEED = 4'hF;
  
  wire [3:0] jcounter_out;
  wire [2:0] decode_out;

  jcounter #(.SEED(SEED)) jcounter_inst(.clk(CLKIN),.out(jcounter_out));
  decoder decoder_inst(.in(jcounter_out),.out(decode_out));

  assign D5 = 1'b0;
  assign D4 = 1'b0;
  assign D3 = decode_out[2];
  assign D2 = decode_out[1];
  assign D1 = decode_out[0];



endmodule
