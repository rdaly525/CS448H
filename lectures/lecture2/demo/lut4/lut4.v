module main ( input [3:0] J1, output D5 );

SB_LUT4 #(.LUT_INIT(16'hfffe)) lut4 (.I0(J1[0]), .I1(J1[1]), .I2(J1[2]), .I3(J1[3]), .O(D5));

endmodule
