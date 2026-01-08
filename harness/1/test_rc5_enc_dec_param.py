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
    dut.dec_start.value = 0;
    dut.p_in.value = 0x1000;
    dut.lfsr_seed_enc.value = 0xFF;
    await Timer(15, units="ns")  #wait for reset
    dut.reset.value = 1;
    await Timer(200, units="ns")  
    dut._log.info("reset = %d, enc_start = %d, p_in = %x, c_out = %x, enc_done = %d",dut.reset.value,dut.enc_start.value,dut.p_in.value,dut.c_out.value,dut.enc_done.value)
    assert dut.c_out.value == 0x5460, "Ciphertext is not correct"   

@cocotb.test()
async def test_decryption_1(dut):
    """Try accessing the design."""
    await cocotb.start(generate_clock(dut))  # run the clock "in the background"
    print("RC5 decryption");
    await Timer(5, units="ns")  
    dut.reset.value = 0;
    dut.enc_start.value = 0;
    dut.dec_start.value = 1;
    dut.c_in.value = 0x5460;
    dut.lfsr_seed_dec.value = 0xFF;
    await Timer(15, units="ns")  #wait for reset
    dut.reset.value = 1;
    await Timer(250, units="ns")  
    dut._log.info("reset = %d, dec_start = %d, c_in = %x, p_out = %x, dec_done = %d",dut.reset.value,dut.dec_start.value,dut.c_in.value,dut.p_out.value,dut.dec_done.value)
    assert dut.p_out.value == 0x1000, "Plaintext is not correct"   
    
@cocotb.test()
async def test_encryption_2(dut):
    """Try accessing the design."""
    await cocotb.start(generate_clock(dut))  # run the clock "in the background"
    print("RC5 encryption");
    await Timer(5, units="ns")  
    dut.reset.value = 0;
    dut.enc_start.value = 1;
    dut.dec_start.value = 0;
    dut.p_in.value = 0xFFFF;
    dut.lfsr_seed_enc.value = 0xFF;
    await Timer(15, units="ns")  #wait for reset
    dut.reset.value = 1;
    await Timer(200, units="ns")  
    dut._log.info("reset = %d, enc_start = %d, p_in = %x, c_out = %x, enc_done = %d",dut.reset.value,dut.enc_start.value,dut.p_in.value,dut.c_out.value,dut.enc_done.value)
    assert dut.c_out.value == 0xA788, "Ciphertext is not correct"   
    
@cocotb.test()
async def test_decryption_2(dut):
    """Try accessing the design."""
    await cocotb.start(generate_clock(dut))  # run the clock "in the background"
    print("RC5 decryption");
    await Timer(5, units="ns")  
    dut.reset.value = 0;
    dut.enc_start.value = 0;
    dut.dec_start.value = 1;
    dut.c_in.value = 0xA788;
    dut.lfsr_seed_dec.value = 0xFF;
    await Timer(15, units="ns")  #wait for reset
    dut.reset.value = 1;
    await Timer(250, units="ns")  # wait a bit
    dut._log.info("reset = %d, dec_start = %d, c_in = %x, p_out = %x, dec_done = %d",dut.reset.value,dut.dec_start.value,dut.c_in.value,dut.p_out.value,dut.dec_done.value)
    assert dut.p_out.value == 0xFFFF, "Plaintext is not correct"   
    
@cocotb.test()
async def test_encryption_3(dut):
    """Try accessing the design."""
    await cocotb.start(generate_clock(dut))  # run the clock "in the background"
    print("RC5 encryption");
    await Timer(5, units="ns")  
    dut.reset.value = 0;
    dut.enc_start.value = 1;
    dut.dec_start.value = 0;
    dut.p_in.value = 0x0000;
    dut.lfsr_seed_enc.value = 0xFF;
    await Timer(15, units="ns")  #wait for reset
    dut.reset.value = 1;
    await Timer(200, units="ns")  
    dut._log.info("reset = %d, enc_start = %d, p_in = %x, c_out = %x, enc_done = %d",dut.reset.value,dut.enc_start.value,dut.p_in.value,dut.c_out.value,dut.enc_done.value)
    assert dut.c_out.value == 0xAD6D, "Ciphertext is not correct"   
    
@cocotb.test()
async def test_decryption_3(dut):
    """Try accessing the design."""
    await cocotb.start(generate_clock(dut))  # run the clock "in the background"
    print("RC5 decryption");
    await Timer(5, units="ns")  
    dut.reset.value = 0;
    dut.enc_start.value = 0;
    dut.dec_start.value = 1;
    dut.c_in.value = 0xAD6D;
    dut.lfsr_seed_dec.value = 0xFF;
    await Timer(15, units="ns")  #wait for reset
    dut.reset.value = 1;
    await Timer(250, units="ns") 
    dut._log.info("reset = %d, dec_start = %d, c_in = %x, p_out = %x, dec_done = %d",dut.reset.value,dut.dec_start.value,dut.c_in.value,dut.p_out.value,dut.dec_done.value)
    assert dut.p_out.value == 0x0000, "Plaintext is not correct"   
