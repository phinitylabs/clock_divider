import cocotb
from cocotb.triggers import FallingEdge,RisingEdge,Timer


async def generate_clock(dut):
    """Generate clock pulses."""

    for cycle in range(1000):
        dut.clock.value = 0
        await Timer(5, units="ns")
        dut.clock.value = 1
        await Timer(5, units="ns")

@cocotb.test()
async def test_encryption_1(dut):
    """Try accessing the design."""

    await cocotb.start(generate_clock(dut))  # run the clock "in the background"
    print("RC5 encryption");
    await Timer(5, units="ns")  
    dut.reset.value = 0;
    dut.enc_start.value = 1;
    dut.p.value = 0x1000;
    await Timer(15, units="ns")  #wait for reset
    assert dut.c.value == 0,"Ciphertext is not reset to zero when reset is LOW"
    dut.reset.value = 1;
    for i in range(5):
        await FallingEdge(dut.clock)
        if (i == 4):
            assert dut.enc_done == 1, "enc_done is not HIGH after four clock cycles"
            assert dut.c.value != 0, "Ciphertext has not changed"
    await Timer(100, units="ns")  
    dut._log.info("reset = %d, enc_start = %d, p = %x, c = %x, enc_done = %d",dut.reset.value,dut.enc_start.value,dut.p.value,dut.c.value,dut.enc_done.value)
    assert dut.c.value == 0x1F86, "Ciphertext is not correct"   
   
@cocotb.test()
async def test_encryption_2(dut):
    """Try accessing the design."""

    await cocotb.start(generate_clock(dut))  # run the clock "in the background"
    print("RC5 encryption");
    await Timer(5, units="ns")  # wait a bit
    dut.reset.value = 0;
    dut.enc_start.value = 1;
    dut.p.value = 0xFFFF;
    await Timer(15, units="ns")  # wait for reset
    assert dut.c.value == 0,"Ciphertext is not reset to zero when reset is LOW"
    dut.reset.value = 1;
    for i in range(5):
        await FallingEdge(dut.clock)
        if (i == 4):
            assert dut.enc_done == 1, "enc_done is not HIGH after four clock cycles"
            assert dut.c.value != 0, "Ciphertext has not changed"
    await Timer(100, units="ns")  
    dut._log.info("reset = %d, enc_start = %d, p = %x, c = %x, enc_done = %d",dut.reset.value,dut.enc_start.value,dut.p.value,dut.c.value,dut.enc_done.value)
    assert dut.c.value == 0x0703, "Ciphertext is not correct"   
    
@cocotb.test()
async def test_encryption_3(dut):
    """Try accessing the design."""

    await cocotb.start(generate_clock(dut))  # run the clock "in the background"
    print("RC5 encryption");
    await Timer(5, units="ns")  
    dut.reset.value = 0;
    dut.enc_start.value = 1;
    dut.p.value = 0x00FF;
    await Timer(15, units="ns")  # wait for reset
    assert dut.c.value == 0,"Ciphertext is not reset to zero when reset is LOW"
    dut.reset.value = 1;
    for i in range(5):
        await FallingEdge(dut.clock)
        if (i == 4):
            assert dut.enc_done == 1, "enc_done is not HIGH after four clock cycles"
            assert dut.c.value != 0, "Ciphertext has not changed"
    await Timer(100, units="ns")  
    dut._log.info("reset = %d, enc_start = %d, p = %x, c = %x, enc_done = %d",dut.reset.value,dut.enc_start.value,dut.p.value,dut.c.value,dut.enc_done.value)
    assert dut.c.value == 0x9665, "Ciphertext is not correct"   
    
@cocotb.test()
async def test_encryption_4(dut):
    """Try accessing the design."""

    await cocotb.start(generate_clock(dut))  # run the clock "in the background"
    print("RC5 encryption");
    await Timer(5, units="ns")  
    dut.reset.value = 0;
    dut.enc_start.value = 1;
    dut.p.value = 0xFF00;
    await Timer(15, units="ns")  # wait for reset
    assert dut.c.value == 0,"Ciphertext is not reset to zero when reset is LOW"
    dut.reset.value = 1;
    for i in range(5):
        await FallingEdge(dut.clock)
        if (i == 4):
            assert dut.enc_done == 1, "enc_done is not HIGH after four clock cycles"
            assert dut.c.value != 0, "Ciphertext has not changed"
    await Timer(100, units="ns")  
    dut._log.info("reset = %d, enc_start = %d, p = %x, c = %x, enc_done = %d",dut.reset.value,dut.enc_start.value,dut.p.value,dut.c.value,dut.enc_done.value)
    assert dut.c.value == 0x0E86, "Ciphertext is not correct"   
    