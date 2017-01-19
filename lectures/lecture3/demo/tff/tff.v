module main (input clk, output [1:0] J3);
wire  dff_O;
wire lut4_O;
SB_DFF dff (.C(clk), .D(lut4_O), .Q(dff_O));
SB_LUT4 #(.LUT_INIT(16'h5555)) lut4 (.I0(dff_O), .I1(1'b0), .I2(1'b0), .I3(1'b0), .O(lut4_O));
assign J3 = {dff_O, clk};
endmodule

