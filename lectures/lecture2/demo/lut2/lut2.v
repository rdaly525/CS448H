module main ( input [1:0] J1, output D5 );

SB_LUT4 #(.LUT_INIT(16'h8888)) lut4 (.I0(J1[0]), .I1(J1[1]), .I2(1'b0), .I3(1'b0), .O(D5));

endmodule
