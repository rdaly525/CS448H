module main ( input clk, input [3:0] J1, output D5 );

reg q;

always @(posedge clk)
    q <= ~q; // invert q on rising edge of clock

assign D5 = q;

endmodule
