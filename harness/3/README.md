#### 1. To execute the harness, MAKEFILE and python cocotb testbench (test_rc5_enc_16bit.py) are needed
#### 2. The rtl (.sv) files will be interfaced with the cocotb testbench through the MAKEFILE 
#### 3. To run the cocotb testbench without dump file generation (.fst) for waveform view, execute the following command in Anaconda prompt:
   make
#### 4. To run the cocotb testbench with dump file generation (.fst) for waveform view, execute the following command in Anaconda prompt:
   make WAVES=1
#### 5. Waveform can be viewed with the following command
   gtkwave sim_build/rc5_enc_16bit.fst
