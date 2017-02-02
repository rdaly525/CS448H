module main (
    input clk,
    output [7:0] J3
);

reg [7:0] counter;

always @(posedge clk)
   counter <= counter + 1;

assign J3 = counter;

endmodule
