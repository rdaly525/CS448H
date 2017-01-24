module main ( input clk, input [3:0] J1, output D5 );

reg q;

// all signals assigned to in an always block must be reg

always @(posedge clk) // sensitivity list, execute if condition is satisfied
    q <= J1[0]; // assign to q on rising edge of clock

assign D5 = q;

endmodule
