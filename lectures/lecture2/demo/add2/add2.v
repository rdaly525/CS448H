module FA ( input I0, input I1, input CIN, output S, output COUT); 

wire and1_O;
wire and2_O;
wire and3_O;

and and1 (and1_O, I0, I1);
and and2 (and2_O, I1, CIN);
and and3 (and3_O, CIN, I0);

or or1 (COUT, and1_O, and2_O, and3_O);
xor(S, I0, I1, CIN);

endmodule

module main ( input [4:0] J1, output D1, output D2, output D3 );

wire [1:0] A = J1[1:0];
wire [1:0] B = J1[3:2];
wire CIN = J1[4];

wire fa1_COUT;

FA fa1 (A[0], B[0], CIN, D1, fa1_COUT);
FA fa2 (A[1], B[1], fa1_COUT, D2, D3);

endmodule
