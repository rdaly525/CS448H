module main ( input [1:0] J1, output D5 );

wire not1_O;
wire not2_O;
wire and1_O;
wire and2_O;

not not1 (not1_O, J1[0]);
and and1 (and1_O, not1_O, J1[1]);

not not2 (not2_O, J1[1]);
and and2 (and2_O, J1[0], not2_O);

or or1 (D5, and1_O, and2_O);

endmodule
