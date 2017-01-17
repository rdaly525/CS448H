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

module main ( input [2:0] J1, output D1, D2 );

FA fa1 (J1[0], J1[1], J1[2], D1, D2);

endmodule
