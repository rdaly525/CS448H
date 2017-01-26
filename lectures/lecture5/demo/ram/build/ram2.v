module Register8CE (input [7:0] I, output [7:0] O, input  CLK, input  CE);
wire  inst0_Q;
wire  inst1_Q;
wire  inst2_Q;
wire  inst3_Q;
wire  inst4_Q;
wire  inst5_Q;
wire  inst6_Q;
wire  inst7_Q;
SB_DFFE inst0 (.C(CLK), .E(CE), .D(I[0]), .Q(inst0_Q));
SB_DFFE inst1 (.C(CLK), .E(CE), .D(I[1]), .Q(inst1_Q));
SB_DFFE inst2 (.C(CLK), .E(CE), .D(I[2]), .Q(inst2_Q));
SB_DFFE inst3 (.C(CLK), .E(CE), .D(I[3]), .Q(inst3_Q));
SB_DFFE inst4 (.C(CLK), .E(CE), .D(I[4]), .Q(inst4_Q));
SB_DFFE inst5 (.C(CLK), .E(CE), .D(I[5]), .Q(inst5_Q));
SB_DFFE inst6 (.C(CLK), .E(CE), .D(I[6]), .Q(inst6_Q));
SB_DFFE inst7 (.C(CLK), .E(CE), .D(I[7]), .Q(inst7_Q));
assign O = {inst7_Q,inst6_Q,inst5_Q,inst4_Q,inst3_Q,inst2_Q,inst1_Q,inst0_Q};
endmodule

module Decoder2 (input [1:0] I, output [3:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
SB_LUT4 #(.LUT_INIT(16'h0001)) inst0 (.I0(I[0]), .I1(I[1]), .I2(1'b0), .I3(1'b0), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'h0002)) inst1 (.I0(I[0]), .I1(I[1]), .I2(1'b0), .I3(1'b0), .O(inst1_O));
SB_LUT4 #(.LUT_INIT(16'h0004)) inst2 (.I0(I[0]), .I1(I[1]), .I2(1'b0), .I3(1'b0), .O(inst2_O));
SB_LUT4 #(.LUT_INIT(16'h0008)) inst3 (.I0(I[0]), .I1(I[1]), .I2(1'b0), .I3(1'b0), .O(inst3_O));
assign O = {inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module And2x4 (input [3:0] I0, input [3:0] I1, output [3:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
SB_LUT4 #(.LUT_INIT(16'h8888)) inst0 (.I0(I0[0]), .I1(I1[0]), .I2(1'b0), .I3(1'b0), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'h8888)) inst1 (.I0(I0[1]), .I1(I1[1]), .I2(1'b0), .I3(1'b0), .O(inst1_O));
SB_LUT4 #(.LUT_INIT(16'h8888)) inst2 (.I0(I0[2]), .I1(I1[2]), .I2(1'b0), .I3(1'b0), .O(inst2_O));
SB_LUT4 #(.LUT_INIT(16'h8888)) inst3 (.I0(I0[3]), .I1(I1[3]), .I2(1'b0), .I3(1'b0), .O(inst3_O));
assign O = {inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module Mux2x8 (input [7:0] I0, input [7:0] I1, input  S, output [7:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst0 (.I0(I0[0]), .I1(I1[0]), .I2(S), .I3(1'b0), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst1 (.I0(I0[1]), .I1(I1[1]), .I2(S), .I3(1'b0), .O(inst1_O));
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst2 (.I0(I0[2]), .I1(I1[2]), .I2(S), .I3(1'b0), .O(inst2_O));
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst3 (.I0(I0[3]), .I1(I1[3]), .I2(S), .I3(1'b0), .O(inst3_O));
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst4 (.I0(I0[4]), .I1(I1[4]), .I2(S), .I3(1'b0), .O(inst4_O));
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst5 (.I0(I0[5]), .I1(I1[5]), .I2(S), .I3(1'b0), .O(inst5_O));
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst6 (.I0(I0[6]), .I1(I1[6]), .I2(S), .I3(1'b0), .O(inst6_O));
SB_LUT4 #(.LUT_INIT(16'hCACA)) inst7 (.I0(I0[7]), .I1(I1[7]), .I2(S), .I3(1'b0), .O(inst7_O));
assign O = {inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module main (input [1:0] RADDR, input [1:0] WADDR, input  I0, input  I1, input  WE, output [7:0] J3, input  CLKIN);
wire [7:0] inst0_O;
wire [7:0] inst1_O;
wire [7:0] inst2_O;
wire [7:0] inst3_O;
wire [3:0] inst4_O;
wire [3:0] inst5_O;
wire [7:0] inst6_O;
wire [7:0] inst7_O;
wire [7:0] inst8_O;
Register8CE inst0 (.I({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,I1,I0}), .O(inst0_O), .CLK(CLKIN), .CE(inst5_O[0]));
Register8CE inst1 (.I({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,I1,I0}), .O(inst1_O), .CLK(CLKIN), .CE(inst5_O[1]));
Register8CE inst2 (.I({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,I1,I0}), .O(inst2_O), .CLK(CLKIN), .CE(inst5_O[2]));
Register8CE inst3 (.I({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,I1,I0}), .O(inst3_O), .CLK(CLKIN), .CE(inst5_O[3]));
Decoder2 inst4 (.I(WADDR), .O(inst4_O));
And2x4 inst5 (.I0(inst4_O), .I1({WE,WE,WE,WE}), .O(inst5_O));
Mux2x8 inst6 (.I0(inst0_O), .I1(inst1_O), .S(RADDR[0]), .O(inst6_O));
Mux2x8 inst7 (.I0(inst2_O), .I1(inst3_O), .S(RADDR[0]), .O(inst7_O));
Mux2x8 inst8 (.I0(inst6_O), .I1(inst7_O), .S(RADDR[1]), .O(inst8_O));
assign J3 = inst8_O;
endmodule

