/*
 * Copyright (C) 2020  The SymbiFlow Authors.
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

`include "muxcy.v"
`include "xorcy.v"

module CARRY4(output [3:0] CO, O, input CI, CYINIT, input [3:0] DI, S);
   wire CIN = CI | CYINIT;

   MUXCY muxcy0 (.O(CO[0]), .CI(CIN),   .DI(DI[0]), .S(S[0]));
   MUXCY muxcy1 (.O(CO[1]), .CI(CO[0]), .DI(DI[1]), .S(S[1]));
   MUXCY muxcy2 (.O(CO[2]), .CI(CO[1]), .DI(DI[2]), .S(S[2]));
   MUXCY muxcy3 (.O(CO[3]), .CI(CO[2]), .DI(DI[3]), .S(S[3]));

   XORCY xorcy0 (.O(O[0]), .CI(CIN),   .LI(S[0]));
   XORCY xorcy1 (.O(O[1]), .CI(CO[0]), .LI(S[1]));
   XORCY xorcy2 (.O(O[2]), .CI(CO[1]), .LI(S[2]));
   XORCY xorcy3 (.O(O[3]), .CI(CO[2]), .LI(S[3]));
endmodule
