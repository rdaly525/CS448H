<%
N = 8
%>\
`define N ${N}

module FA ( input I0, input I1, input CIN, output S, output COUT);

SB_LUT4 #(.LUT_INIT(16'hC33C)) lut4 (.I0(1'b0), .I1(I0), .I2(I1), .I3(CIN), .O(S));
SB_CARRY carry (.I0(I0), .I1(I1), .CI(CIN), .CO(COUT));

endmodule

module main ( input [`N-1:0] J1, input [`N-1:0] J3, output D5 );

wire [`N-1:0] fasum;
wire [`N-1:0] facout;

FA fa0(J1[0], J3[0], 1'b0, fasum[0], facout[0]);

% for i in range(1,N):
FA fa${i}(J1[${i}], J3[${i}], facout[${i-1}], fasum[${i}], facout[${i}]);
% endfor

assign D5 = facout[`N-1];

endmodule
