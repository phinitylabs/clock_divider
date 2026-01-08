#### 1. To execute the harness, MAKEFILE and python cocotb testbench (test_rc5_enc_dec_param.py) are needed
#### 2. The rtl (.sv) files will be interfaced with the cocotb testbench through the MAKEFILE 
#### 3. To run the cocotb testbench without dump file generation (.fst) for waveform view, execute the following command in Anaconda prompt:
   make
#### 4. To run the cocotb testbench with dump file generation (.fst) for waveform view, execute the following command in Anaconda prompt:
   make WAVES=1
#### 5. Waveform can be viewed with the following command
   gtkwave sim_build/rc5_enc_dec_param.fst
#### 6. Sample harness testbench output for make WAVES=1
rm -f results.xml\
"make" -f Makefile results.xml\
make[1]: Entering directory '/e/Phinity_labs/sundararaman_rajagopalan_RTL/harness'\
/c/iverilog/bin/iverilog -o sim_build/sim.vvp -D COCOTB_SIM=1 -s rc5_enc_dec_param -g2012 -f sim_build/cmds.f -I../rtl -s cocotb_iverilog_dump  ../rtl/rc5_enc_dec_param.sv sim_build/cocotb_iverilog_dump.v\
rm -f results.xml\
MODULE=test_rc5_enc_dec_param TESTCASE= TOPLEVEL=rc5_enc_dec_param TOPLEVEL_LANG=verilog \
         /c/iverilog/bin/vvp -M C:/Users/Admin/miniconda3/Lib/site-packages/cocotb/libs -m cocotbvpi_icarus   sim_build/sim.vvp -fst\
     -.--ns INFO     gpi                                ..mbed\gpi_embed.cpp:81   in set_program_name_in_venv        Did not detect Python virtual environment. Using system-wide Python interpreter\
     -.--ns INFO     gpi                                ..\gpi\GpiCommon.cpp:101  in gpi_print_registered_impl       VPI registered\
     0.00ns INFO     cocotb                             Running on Icarus Verilog version 12.0 (devel)\
     0.00ns INFO     cocotb                             Running tests with cocotb v1.9.2 from C:\Users\Admin\miniconda3\Lib\site-packages\cocotb\
     0.00ns INFO     cocotb                             Seeding Python random module with 1758477577\
     0.00ns INFO     cocotb.regression                  Found test test_rc5_enc_dec_param.test_encryption_1\
     0.00ns INFO     cocotb.regression                  Found test test_rc5_enc_dec_param.test_decryption_1\
     0.00ns INFO     cocotb.regression                  Found test test_rc5_enc_dec_param.test_encryption_2\
     0.00ns INFO     cocotb.regression                  Found test test_rc5_enc_dec_param.test_decryption_2\
     0.00ns INFO     cocotb.regression                  Found test test_rc5_enc_dec_param.test_encryption_3\
     0.00ns INFO     cocotb.regression                  Found test test_rc5_enc_dec_param.test_decryption_3\
     0.00ns INFO     cocotb.regression                  running test_encryption_1 (1/6)\
                                                          Try accessing the design.\
RC5 encryption\
FST info: dumpfile sim_build/rc5_enc_dec_param.fst opened for output.\
   220.00ns INFO     cocotb.rc5_enc_dec_param           reset = 1, enc_start = 1, p_in = 1000, c_out = 5460, enc_done = 1\
   220.00ns INFO     cocotb.regression                  test_encryption_1 passed\
   220.00ns INFO     cocotb.regression                  running test_decryption_1 (2/6)\
                                                          Try accessing the design.\
RC5 decryption\
   490.00ns INFO     cocotb.rc5_enc_dec_param           reset = 1, dec_start = 1, c_in = 5460, p_out = 1000, dec_done = 1\
   490.00ns INFO     cocotb.regression                  test_decryption_1 passed\
   490.00ns INFO     cocotb.regression                  running test_encryption_2 (3/6)\
                                                          Try accessing the design.\
RC5 encryption\
   710.00ns INFO     cocotb.rc5_enc_dec_param           reset = 1, enc_start = 1, p_in = ffff, c_out = a788, enc_done = 1\
   710.00ns INFO     cocotb.regression                  test_encryption_2 passed\
   710.00ns INFO     cocotb.regression                  running test_decryption_2 (4/6)\
                                                          Try accessing the design.\
RC5 decryption\
   980.00ns INFO     cocotb.rc5_enc_dec_param           reset = 1, dec_start = 1, c_in = a788, p_out = ffff, dec_done = 1\
   980.00ns INFO     cocotb.regression                  test_decryption_2 passed\
   980.00ns INFO     cocotb.regression                  running test_encryption_3 (5/6)\
                                                          Try accessing the design.\
RC5 encryption\
  1200.00ns INFO     cocotb.rc5_enc_dec_param           reset = 1, enc_start = 1, p_in = 0, c_out = ad6d, enc_done = 1\
  1200.01ns INFO     cocotb.regression                  test_encryption_3 passed\
  1200.01ns INFO     cocotb.regression                  running test_decryption_3 (6/6)\
                                                          Try accessing the design.\
RC5 decryption\
  1470.01ns INFO     cocotb.rc5_enc_dec_param           reset = 1, dec_start = 1, c_in = ad6d, p_out = 0, dec_done = 1\
  1470.01ns INFO     cocotb.regression                  test_decryption_3 passed\
  1470.01ns INFO     cocotb.regression\                  **************************************************************************************************\
                                                        ** TEST                                      STATUS  SIM TIME (ns)\  REAL TIME (s)  RATIO (ns/s) **\
                                                        **************************************************************************************************\
                                                        ** test_rc5_enc_dec_param.test_encryption_1   PASS         220.00           0.02      11232.10  **\
                                                        ** test_rc5_enc_dec_param.test_decryption_1   PASS         270.00           0.01      49853.24  **\
                                                        ** test_rc5_enc_dec_param.test_encryption_2   PASS         220.00           0.01      41020.27  **\
                                                        ** test_rc5_enc_dec_param.test_decryption_2   PASS         270.00           0.00      55712.42  **\
                                                        ** test_rc5_enc_dec_param.test_encryption_3   PASS         220.00           0.00      54613.58  **\
                                                        ** test_rc5_enc_dec_param.test_decryption_3   PASS         270.00           0.00      54600.37  **\
                                                        **************************************************************************************************\
                                                        ** TESTS=6 PASS=6 FAIL=0 SKIP=0                           1470.01           0.19       7936.60  **\
                                                        **************************************************************************************************\

make[1]: Leaving directory '/e/Phinity_labs/sundararaman_rajagopalan_RTL/harness'\

(base) E:\Phinity_labs\sundararaman_rajagopalan_RTL\harness>cd sim_build\

(base) E:\Phinity_labs\sundararaman_rajagopalan_RTL\harness\sim_build>gtkwave rc5_enc_dec_param.fst\

GTKWave Analyzer v3.3.100 (w)1999-2019 BSI\

FSTLOAD | Processing 42 facs.\
FSTLOAD | Built 38 signals and 4 aliases.\
FSTLOAD | Building facility hierarchy tree.\
FSTLOAD | Sorting facility hierarchy tree.\
WM Destroy\

