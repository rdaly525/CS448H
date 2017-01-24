
module main ( input clk, input [3:0] J1, output D5 );

reg [3:0] q;

// nonblocking assignments means that all assignments
// are done simultaneously, in parallel
always @(posedge clk) 
  begin
    q[0] <= J1[0]; // <= means nonblocking assignment
    q[1] <= q[0];
    q[2] <= q[1];
    q[3] <= q[2];
    // equivalent to q <= {q[2:0], J1[0]}
  end

assign D5 = q;

endmodule
