module FA ( input I0, input I1, input CIN, output S, output COUT); 

SB_LUT4 #(.LUT_INIT(16'hC33C)) lut4 (.I0(1'b0), .I1(I0), .I2(I1), .I3(CIN), .O(S));
SB_CARRY carry (.I0(I0), .I1(I1), .CI(CIN), .CO(COUT));

endmodule

module main ( input [4:0] J1, output D1, output D2, output D3 );

wire [1:0] A = J1[1:0];
wire [1:0] B = J1[3:2];
wire CIN = J1[4];

wire fa1_COUT;

FA fa1 (A[0], B[0], CIN, D1, fa1_COUT);
FA fa2 (A[1], B[1], fa1_COUT, D2, D3);

endmodule
