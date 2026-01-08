#### 1. To execute the harness, following packages have to be installed
- pip install cocotb
- pip install pytest
- pip install cocotb-test
#### 2. Following files are require to execute the harness
- test_rc5_enc_16bit.py
- pytest_rc5.py
#### 3. The rtl (.sv) files will be interfaced with the cocotb testbench through the pytest_rc5.py file
#### 4. To run the cocotb testbench, execute the following command in cmd prompt, powershell, git bash or anaconda prompt
python -m pytest pytest_rc5.py --log-cli-level=INFO
