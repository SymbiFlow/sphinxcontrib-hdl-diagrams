attribute \generator "nMigen"
attribute \top 1
attribute \nmigen.hierarchy "top"
module \top
  attribute \src "counter.py:9"
  wire width 1 output 0 \o
  attribute \src "/usr/local/lib/python3.7/site-packages/nmigen/hdl/ir.py:526"
  wire width 1 input 1 \clk
  attribute \src "/usr/local/lib/python3.7/site-packages/nmigen/hdl/ir.py:526"
  wire width 1 input 2 \rst
  attribute \src "counter.py:8"
  wire width 16 \v
  attribute \src "counter.py:8"
  wire width 16 \v$next
  attribute \src "counter.py:13"
  wire width 17 $1
  attribute \src "counter.py:13"
  wire width 17 $2
  attribute \src "counter.py:13"
  cell $add $3
    parameter \A_SIGNED 1'0
    parameter \A_WIDTH 5'10000
    parameter \B_SIGNED 1'0
    parameter \B_WIDTH 1'1
    parameter \Y_WIDTH 5'10001
    connect \A \v
    connect \B 1'1
    connect \Y $2
  end
  connect $1 $2
  process $group_0
    assign \v$next \v
    assign \v$next $1 [15:0]
    attribute \src "/usr/local/lib/python3.7/site-packages/nmigen/hdl/xfrm.py:530"
    switch \rst
      case 1'1
        assign \v$next 16'1111111111111111
    end
    sync init
      update \v 16'1111111111111111
    sync posedge \clk
      update \v \v$next
  end
  process $group_1
    assign \o 1'0
    assign \o \v [15]
    sync init
  end
end
