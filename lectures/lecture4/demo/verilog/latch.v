module main ( input clk, input [3:0] J1, output D5 );

reg q;

always @(clk or J1) 
    if( clk) 
        q <= J1[0]; // since q does not always change, a latch is inferred

assign D5 = q;

endmodule
