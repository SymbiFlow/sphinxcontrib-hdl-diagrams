/*
 * Copyright (C) 2020  The SymbiFlow Authors.
 *
 * Use of this source code is governed by a ISC-style
 * license that can be found in the LICENSE file or at
 * https://opensource.org/licenses/ISC
 *
 * SPDX-License-Identifier:	ISC
 */

// Single flip-flip test.
module top(input clk, input di, output do);
  always @( posedge clk )
    do <= di;
endmodule // top
