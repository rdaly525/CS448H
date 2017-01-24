module main ( input clk, input [3:0] J1, output D5 );

reg q1, q2;

// allows multiple assignments to q1 and q2!

always @(*) 
  begin
      q1 <= 1'b0;
      q2 <= q1;
  end

always @(*) 
  begin
      q1 <= 1'b1;
      q2 <= q1;
  end

assign D5 = q2;

endmodule
