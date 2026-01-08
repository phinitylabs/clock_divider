import os
import cocotb_test.simulator
import pytest

@pytest.mark.parametrize("toplevel_lang", ["verilog"])
def test_rc5(toplevel_lang):
    sim_build = os.path.join("sim_build", "rc5")

    cocotb_test.simulator.run(
        verilog_sources=["../../rtl/rc5_enc_16bit.sv"],  # adjust path to your RTL
        toplevel="rc5_enc_16bit",                   # your Verilog top module name
        module="test_rc5_enc_16bit",                # name of this Python file (without .py)
        toplevel_lang=toplevel_lang,
        sim="icarus",                         # or "verilator", "modelsim", etc.
        sim_build=sim_build,
        WAVES=True
    )
