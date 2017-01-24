module main ( input clk, input reset, input [3:0] J1, output D5 );

reg q;

always @(posedge clk)
    if(reset) q <= 1'b0; // synchronous reset 
    else      q <= &J1;

assign D5 = q;

endmodule
