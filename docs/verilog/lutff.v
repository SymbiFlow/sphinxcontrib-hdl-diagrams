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
	input  [3:0] i,
	output reg o
);
	always @(posedge clk)
		o <= ^i;
endmodule
