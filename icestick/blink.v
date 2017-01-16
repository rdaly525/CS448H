// This should blink at a rate of ~ second

module main (output  D5, input  CLKIN);
  
  parameter N = 24;
  
  reg [N-1:0] cnt;
  
  always @(posedge CLKIN) begin
    cnt <= cnt+1;
  end
  assign D5 = cnt[N-1];


endmodule
