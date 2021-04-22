--
-- Copyright (C) 2020  The SymbiFlow Authors.
--
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may obtain a copy of the License at
--
--     https://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.
--
-- SPDX-License-Identifier: Apache-2.0

library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity alu is
    port(
        a : in unsigned(3 downto 0);
        b : in unsigned(3 downto 0);
        s : in unsigned(1 downto 0);
        y : out unsigned(3 downto 0)
    );
end alu;

architecture rtl of alu is

begin

    y <= a when s="00" else
        b when s="01" else
        "0000" when s="10" else
        a + b when s="11" else (others => '0');

end;
