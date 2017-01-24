module main ( input clk, input [3:0] J1, output D5 );

reg q;

always @(*) // execute if any variables change, in this case J1[0]
    q = J1[0];

// q is declared as a reg, but will actually be a wire!!

assign D5 = q;

endmodule
