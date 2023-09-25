/*
 * Copyright (C) 2020-2021  The SymbiFlow Authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

module ADDER (
	a, b, cin,
	sum, cout
);

syntax error here;

	input wire a;
	input wire b;
	input wire cin;

	output wire sum;
	output wire cout;

	// Full adder combinational logic
	assign sum = a ^ b ^ cin;
	assign cout = ((a ^ b) & cin) | (a & b);
endmodule
