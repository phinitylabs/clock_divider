module tb_rc5_enc();
  
	//Parameter to declare number of tests
	parameter test_num = 700;
	
	reg clk,rst;
	logic [15:0] enc_c;
	logic [15:0] enc_p;
	logic enc_done,enc_start;

	//Module instantiation
	
	rc5_enc_16bit DUT (.clock(clk),
	                   .reset(rst),
					   .enc_start(enc_start),
					   .p(enc_p),
					   .c(enc_c),
					   .enc_done(enc_done)
					   );

	//Stimulus generation (clock generation for TB)
	initial begin
		clk = 0;
		repeat(test_num)
		begin
			#5 clk = 1'b1;
			#5 clk = 1'b0;
		end
	end

	initial begin 
	    //Test 1
		rst = 1'b0;enc_start <= 1'b1; enc_p <= 16'h1000;
		#20 rst <= 1'b1; 
		#100 rst = 1'b0;
		
		//Test 2
		rst = 1'b0;enc_start <= 1'b1; enc_p <= 16'hFFFF;
		#20 rst <= 1'b1; 
		#100 rst = 1'b0;
		
	    //Test 3
		rst = 1'b0;enc_start <= 1'b1; enc_p <= 16'h00FF;
		#20 rst <= 1'b1; 
		#100 rst = 1'b0;
		
		//Test 4
		rst = 1'b0;enc_start <= 1'b1; enc_p <= 16'hFF00;
		#20 rst <= 1'b1; 
		#100 rst = 1'b0;
	end

	initial begin
		$dumpvars;
		$dumpfile("dump.vcd");
	end  

	//Monitor to display the stimulus output of DUT
	always@(posedge clk)
		$monitor($time,"reset = %b, enc_start =  %d, enc_p = %x enc_c = %x enc_done = %d",rst,enc_start,enc_p,enc_c,enc_done);

	//TB run time based on number of tests to be executed
	initial begin
		#(test_num*1);
		$finish;
	end
  
endmodule

