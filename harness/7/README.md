#### 1. To execute the harness, MAKEFILE and python cocotb testbench (test_rc5_enc_16bit.py) are needed
#### 2. The rtl (.sv) files will be interfaced with the cocotb testbench through the MAKEFILE 
#### 3. To run the cocotb testbench without dump file generation (.fst) for waveform view, execute the following command in Anaconda prompt:
   make
#### 4. To run the cocotb testbench with dump file generation (.fst) for waveform view, execute the following command in Anaconda prompt:
   make WAVES=1
#### 5. Waveform can be viewed with the following command
   gtkwave sim_build/rc5_enc_16bit.fst
#### 6. Sample cocotb testbench output
rm -f results.xml\
"make" -f Makefile results.xml\
make[1]: Entering directory '/e/Phinity_labs/sundararaman_rajagopalan_RTL/harness'\
/c/iverilog/bin/iverilog -o sim_build/sim.vvp -D COCOTB_SIM=1 -s rc5_enc_16bit -g2012 -f sim_build/cmds.f -s cocotb_iverilog_dump  ../rtl/rc5_enc_16bit.sv  sim_build/cocotb_iverilog_dump.v\
rm -f results.xml\
MODULE=test_rc5_enc_16bit TESTCASE= TOPLEVEL=rc5_enc_16bit TOPLEVEL_LANG=verilog \
         /c/iverilog/bin/vvp -M C:/Users/Admin/miniconda3/Lib/site-packages/cocotb/libs -m cocotbvpi_icarus   sim_build/sim.vvp -fst\
     -.--ns INFO     gpi                                ..mbed\gpi_embed.cpp:81   in set_program_name_in_venv        Did not detect Python virtual environment. Using system-wide Python interpreter\
     -.--ns INFO     gpi                                ..\gpi\GpiCommon.cpp:101  in gpi_print_registered_impl       VPI registered\
     0.00ns INFO     cocotb                             Running on Icarus Verilog version 12.0 (devel)\
     0.00ns INFO     cocotb                             Running tests with cocotb v1.9.2 from C:\Users\Admin\miniconda3\Lib\site-packages\cocotb\
     0.00ns INFO     cocotb                             Seeding Python random module with 1758560419\
     0.00ns INFO     cocotb.regression                  Found test test_rc5_enc_16bit.test_encryption_1\
     0.00ns INFO     cocotb.regression                  Found test test_rc5_enc_16bit.test_encryption_2\
     0.00ns INFO     cocotb.regression                  Found test test_rc5_enc_16bit.test_encryption_3\
     0.00ns INFO     cocotb.regression                  Found test test_rc5_enc_16bit.test_encryption_4\
     0.00ns INFO     cocotb.regression                  running test_encryption_1 (1/4)\
                                                          Try accessing the design.\
RC5 encryption\
FST info: dumpfile sim_build/rc5_enc_16bit.fst opened for output.\
   170.00ns INFO     cocotb.rc5_enc_16bit               reset = 1, enc_start = 1, p = 1000, c = 1f86, enc_done = 1\
   170.00ns INFO     cocotb.regression                  test_encryption_1 passed\
   170.00ns INFO     cocotb.regression                  running test_encryption_2 (2/4)\
                                                          Try accessing the design.\
RC5 encryption\
   340.00ns INFO     cocotb.rc5_enc_16bit               reset = 1, enc_start = 1, p = ffff, c = 703, enc_done = 1\
   340.00ns INFO     cocotb.regression                  test_encryption_2 passed\
   340.00ns INFO     cocotb.regression                  running test_encryption_3 (3/4)\
                                                          Try accessing the design.\
RC5 encryption\
   510.00ns INFO     cocotb.rc5_enc_16bit               reset = 1, enc_start = 1, p = ff, c = 9665, enc_done = 1\
   510.00ns INFO     cocotb.regression                  test_encryption_3 passed\
   510.00ns INFO     cocotb.regression                  running test_encryption_4 (4/4)\
                                                          Try accessing the design.\
RC5 encryption\
   680.00ns INFO     cocotb.rc5_enc_16bit               reset = 1, enc_start = 1, p = ff00, c = e86, enc_done = 1\
   680.00ns INFO     cocotb.regression                  test_encryption_4 passed\
   680.00ns INFO     cocotb.regression\                  **********************************************************************************************\
                                                        ** TEST                                  STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **\
                                                        **********************************************************************************************\
                                                        ** test_rc5_enc_16bit.test_encryption_1   PASS         170.00           0.03       6249.05  **\
                                                        ** test_rc5_enc_16bit.test_encryption_2   PASS         170.00           0.01      22113.07  **\
                                                        ** test_rc5_enc_16bit.test_encryption_3   PASS         170.00           0.01      22917.62  **\
                                                        ** test_rc5_enc_16bit.test_encryption_4   PASS         170.00           0.01      16743.04  **\
                                                        **********************************************************************************************\
                                                        ** TESTS=4 PASS=4 FAIL=0 SKIP=0                        680.00           0.38       1810.79  **\
                                                        **********************************************************************************************\

make[1]: Leaving directory '/e/Phinity_labs/sundararaman_rajagopalan_RTL/harness'
