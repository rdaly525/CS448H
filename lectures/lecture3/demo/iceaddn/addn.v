module FA ( input I0, input I1, input CIN, output S, output COUT); 

SB_LUT4 #(.LUT_INIT(16'hC33C)) lut4 (.I0(1'b0), .I1(I0), .I2(I1), .I3(CIN), .O(S));
SB_CARRY carry (.I0(I0), .I1(I1), .CI(CIN), .CO(COUT));

endmodule

module main ( input [7:0] J1, input [7:0] J3, output D5 );

// `include "add4"
// `include "add8"
`include "add64"

endmodule
