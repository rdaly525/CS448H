module main ( input clk, input [3:0] J1, output D5 );

reg q;

// procedural always blocks: allow if/then/else/case statements

// case statements should handle all cases
always @(*) // execute if J1 changes, combinational, q will not be a DFF!
    case (J1)
       4'b0000: q = 1'b0;
       4'b0001: q = 1'b1;
       4'b0010: q = 1'b0;
       4'b0011: q = 1'b1;
       4'b0100: q = 1'b0;
       4'b0101: q = 1'b1;
       4'b0110: q = 1'b0;
       4'b0111: q = 1'b1;
       4'b1000: q = 1'b0;
       4'b1001: q = 1'b1;
       4'b1010: q = 1'b0;
       4'b1011: q = 1'b1;
       4'b1100: q = 1'b0;
       4'b1101: q = 1'b1;
       4'b1110: q = 1'b0;
       4'b1111: q = 1'b1;
    endcase

assign D5 = q;

endmodule
