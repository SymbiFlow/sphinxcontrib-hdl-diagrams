/*
 * Copyright (C) 2020  The SymbiFlow Authors.
 *
 * Use of this source code is governed by a ISC-style
 * license that can be found in the LICENSE file or at
 * https://opensource.org/licenses/ISC
 *
 * SPDX-License-Identifier:	ISC
 */

// 4-input LUT test.
module top(input [3:0] I, output O);
    always @(I)
    case(I)
        4'b0000 : O = 1;
        4'b1000 : O = 1;
        4'b1100 : O = 1;
        4'b1010 : O = 1;
        4'b1001 : O = 1;
        4'b1111 : O = 1;
        default : O = 0;
    endcase
endmodule // top
