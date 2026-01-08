module clock_divider(
                  reset,   // input
                  clk,     // input
                  out_clk  // output
                  );

//port declaration
input             reset, clk;
output reg        out_clk;
reg         [1:0] clk_count;

always @ (posedge clk)
   begin
      if (!reset)
         begin
            clk_count <= 0;
            out_clk   <= 0;
         end
      else
         begin
            clk_count <= clk_count + 1;
            out_clk   <= clk_count[1];
         end
   end
endmodule