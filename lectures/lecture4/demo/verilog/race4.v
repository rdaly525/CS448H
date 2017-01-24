module main ( input clk, input [3:0] J1, output D5 );

wire q1, q2;

// allows multiple assignments to q1 and q2!

assign q1 = 1'b0;
assign q2 = q1;

assign q1 = 1'b1;
assign q2 = q1;

assign D5 = q2;

endmodule
