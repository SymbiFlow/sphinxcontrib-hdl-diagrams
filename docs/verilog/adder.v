module ADDER (
	a, b, cin,
	sum, cout
);
	input wire a;
	input wire b;
	input wire cin;

	output wire sum;
	output wire cout;

	// Full adder combinational logic
	assign sum = a ^ b ^ cin;
	assign cout = ((a ^ b) & cin) | (a & b);
endmodule
