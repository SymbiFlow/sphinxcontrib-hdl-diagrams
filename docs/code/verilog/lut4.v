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
