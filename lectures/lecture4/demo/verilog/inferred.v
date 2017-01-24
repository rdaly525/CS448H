module main ( input clk, input [3:0] J1, output D5 );

reg q;

// inferred latch
//
// A latch is inferred within a combinatorial block 
// when there are situations in which it is not
// not assigned to a value. The latch is necessary
// since it must keep its old value.
always @(*) 
    if (J2[1])
        q = J1[0]; 


assign D5 = q;

endmodule
