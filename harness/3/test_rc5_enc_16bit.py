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
    dut.reset.value = 1;
    await Timer(150, units="ns")  
    dut._log.info("reset = %d, enc_start = %d, p = %x, c = %x, enc_done = %d",dut.reset.value,dut.enc_start.value,dut.p.value,dut.c.value,dut.enc_done.value)
    assert dut.c.value == 0x9530, "Ciphertext is not correct"   
   
@cocotb.test()
async def test_encryption_2(dut):
    """Try accessing the design."""

    await cocotb.start(generate_clock(dut))  # run the clock "in the background"
    print("RC5 encryption");
    await Timer(5, units="ns")  
    dut.reset.value = 0;
    dut.enc_start.value = 1;
    dut.p.value = 0xFFFF;
    await Timer(15, units="ns")  #wait for reset
    dut.reset.value = 1;
    await Timer(150, units="ns")  
    dut._log.info("reset = %d, enc_start = %d, p = %x, c = %x, enc_done = %d",dut.reset.value,dut.enc_start.value,dut.p.value,dut.c.value,dut.enc_done.value)
    assert dut.c.value == 0x58CB, "Ciphertext is not correct"   
    
@cocotb.test()
async def test_encryption_3(dut):
    """Try accessing the design."""

    await cocotb.start(generate_clock(dut))  # run the clock "in the background"
    print("RC5 encryption");
    await Timer(5, units="ns")  
    dut.reset.value = 0;
    dut.enc_start.value = 1;
    dut.p.value = 0x00FF;
    await Timer(15, units="ns")  #wait for reset
    dut.reset.value = 1;
    await Timer(150, units="ns")  
    dut._log.info("reset = %d, enc_start = %d, p = %x, c = %x, enc_done = %d",dut.reset.value,dut.enc_start.value,dut.p.value,dut.c.value,dut.enc_done.value)
    assert dut.c.value == 0xAFE8, "Ciphertext is not correct"   
    
@cocotb.test()
async def test_encryption_4(dut):
    """Try accessing the design."""

    await cocotb.start(generate_clock(dut))  # run the clock "in the background"
    print("RC5 encryption");
    await Timer(5, units="ns")  
    dut.reset.value = 0;
    dut.enc_start.value = 1;
    dut.p.value = 0xFF00;
    await Timer(15, units="ns")  #wait for reset
    dut.reset.value = 1;
    await Timer(150, units="ns")  
    dut._log.info("reset = %d, enc_start = %d, p = %x, c = %x, enc_done = %d",dut.reset.value,dut.enc_start.value,dut.p.value,dut.c.value,dut.enc_done.value)
    assert dut.c.value == 0x86CF, "Ciphertext is not correct"   
    
