module main ( input clk, input [3:0] J1, output D5 );

reg a, b, c;

always @(*) 
  begin
     a = J1[0] & J1[1];
     b = a | J1[2];;
     c = b ^ J1[3];
  end

assign D5 = c;

endmodule
