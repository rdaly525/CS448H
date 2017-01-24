`define N 8

module FA ( input I0, input I1, input CIN, output S, output COUT);

SB_LUT4 #(.LUT_INIT(16'hC33C)) lut4 (.I0(1'b0), .I1(I0), .I2(I1), .I3(CIN), .O(S));
SB_CARRY carry (.I0(I0), .I1(I1), .CI(CIN), .CO(COUT));

endmodule

module main ( input [`N-1:0] J1, input [`N-1:0] J3, output D5 );

wire [`N-1:0] fasum;
wire [`N-1:0] facout;

FA fa0(J1[0], J3[0], 1'b0, fasum[0], facout[0]);

FA fa1(J1[1], J3[1], facout[0], fasum[1], facout[1]);
FA fa2(J1[2], J3[2], facout[1], fasum[2], facout[2]);
FA fa3(J1[3], J3[3], facout[2], fasum[3], facout[3]);
FA fa4(J1[4], J3[4], facout[3], fasum[4], facout[4]);
FA fa5(J1[5], J3[5], facout[4], fasum[5], facout[5]);
FA fa6(J1[6], J3[6], facout[5], fasum[6], facout[6]);
FA fa7(J1[7], J3[7], facout[6], fasum[7], facout[7]);

assign D5 = facout[`N-1];

endmodule
