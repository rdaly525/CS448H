module main ( input [3:0] J1, output D5 );

// and and1 (D5, J1[0], J1[1], J1[2], J1[3]);

assign D5 = J1[0] & J1[1] & J1[2] & J1[3];

endmodule
