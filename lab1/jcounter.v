//You can Define additional Modules here.




module jcounter(input clk, output [15:0] out);
  //You do not need to use SEED for the main assignment. Just make sure the
  //power-on state is 16'hFFFF
  parameter SEED=16'hFFFF;

  //Your code here (delete the following line)
  assign out = SEED;

endmodule


module decoder(input [15:0] in, output [4:0] out);
  
  //Your code here (delete the following line)
  assign out = 5'd16;

endmodule


// Do not edit main!
module main(output D5, output D4, output D3, output D2, output D1, input CLKIN);
  parameter SEED = 16'hFFFF;
  
  wire [15:0] jcounter_out;
  wire [4:0] decode_out;

  jcounter #(.SEED(SEED)) jcounter_inst(.clk(CLKIN),.out(jcounter_out));
  decoder decoder_inst(.in(jcounter_out),.out(decode_out));

  assign D5 = decode_out[4];
  assign D4 = decode_out[3];
  assign D3 = decode_out[2];
  assign D2 = decode_out[1];
  assign D1 = decode_out[0];



endmodule
