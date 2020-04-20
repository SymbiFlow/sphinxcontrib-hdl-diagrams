/*
 * Copyright (C) 2020  The SymbiFlow Authors.
 *
 * Use of this source code is governed by a ISC-style
 * license that can be found in the LICENSE file or at
 * https://opensource.org/licenses/ISC
 *
 * SPDX-License-Identifier:	ISC
 */

module top (
	input  clk,
	output o
);
	reg [2:0] counter = 0;
	always @(posedge clk)
		counter <= counter + 1;
	assign o = counter[2];
endmodule
