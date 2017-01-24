Notes

1. Combinational logic expressions

and4.v  - assign D5 = J1[0] & ...
andn4.v - assign D5 = &J1;

comb1.v - always

comb2.v - procedural assignment inside always 

2. Sequential logic

always @(posedge clk) 
begin
    ...
end

dff.v

always @(posedge clk) 
    q <= J1[0];

tff.v

always @(posedge clk)
    q <= ~q;

3. Procedural assignment

dffr.v // synchronous reset

always @(posedge clk)
    if(reset) q <= 1'b0; // synchronous reset 
    else      q <= &J1;

4. Combinational logic inside of always

// system verilog always_comb, always_ff, always_latch
always @(*) 
begin
    // combinational
end

always_comb1.v

always @(*) // execute if any variables change, in this case J1[0]
    q <= J1[0]; 

normally written as q = J1[0] - we'll come back to that

always @(*) // execute if any variables change, in this case J1[0]
    q <= J1[0]; 

5. Latch inference

latch.v 

inferred.v

6. Non-blocking vs. blocking

Blocking assignments block the execution of other assignments. This causes
them to be executed in order.

qqnonblocking.v

always @(*) 
  begin
     q1 <= J1[0];
     q2 <= q1; // q2 gets the old value of q1
  end

qqblocking.v
always @(*) 
  begin
     q1 = J1[0];
     q2 = q1; // q2 gets the new value of q1
  end

blockng.v - like sequential programming language

shift.v - concurrent assignment

5. Convention: Use blocking for combinational logic

always_comb2.v

always_comb3.v

// synopsis full_case, parallel_case, …

6. Race conditions


Klunky Semantics!

A register can only be assigned to in one always block.

Always blocks are 'analyzed' to see if they are combinational.
In this case, the reg is actually a wire.

If the sequential code in an always block doesn't always assign
to a reg (incomplete procedural assignment), than there will 
definitely be a register.

If the reg is not assigned in some statement, then it retains its old value.
Very temperamental and dangerous!

http://electronics.stackexchange.com/questions/29553/how-are-verilog-always-statements-implemented-in-hardware

http://stackoverflow.com/questions/22459413/what-is-inferred-latch-and-how-it-is-created-when-it-is-missing-else-statement-i
