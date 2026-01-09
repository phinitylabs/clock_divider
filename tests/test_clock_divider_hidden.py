import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

CLK_PERIOD_NS = 10


def exp_out_from_old_count(old_count: int) -> int:
    """Expected out_clk = old clk_count[1]."""
    return (old_count >> 1) & 0x1


def logic_to_int_01(sig) -> int:
    """Convert 1-bit signal to int, fail if X/Z (cocotb 2.x)."""
    s = str(sig.value).lower()  # "0", "1", "x", "z"
    assert s in ("0", "1"), f"{sig._name} is not 0/1, got {s}"
    return 1 if s == "1" else 0


async def sample_out_clk_after_nba(dut) -> int:
    """Wait a delta so NBAs apply, then sample."""
    await Timer(1, unit="step")
    return logic_to_int_01(dut.out_clk)


async def start_clock_in_reset(dut):
    """Start clock with reset asserted so regs don't stay X."""
    dut.clk.value = 0
    dut.reset.value = 0  # assert reset (active-low) before clock starts

    cocotb.start_soon(Clock(dut.clk, CLK_PERIOD_NS, unit="ns").start())

    # First posedge while in reset forces outputs to known values
    await RisingEdge(dut.clk)
    _ = await sample_out_clk_after_nba(dut)


async def apply_sync_reset_active_low(dut, cycles: int = 2):
    """
    Assert synchronous active-low reset for N rising edges, then deassert.
    Deassert between edges (on falling edge) so next rising sees reset=1.
    """
    await FallingEdge(dut.clk)
    dut.reset.value = 0
    for _ in range(cycles):
        await RisingEdge(dut.clk)
        _ = await sample_out_clk_after_nba(dut)

    await FallingEdge(dut.clk)
    dut.reset.value = 1  # deassert reset


@cocotb.test()
async def test_reset_behavior(dut):
    cocotb.log.info("Verify synchronous active-low reset behavior")
    await start_clock_in_reset(dut)

    # Hold reset asserted and verify out_clk forced low
    await FallingEdge(dut.clk)
    dut.reset.value = 0
    for i in range(4):
        await RisingEdge(dut.clk)
        got = await sample_out_clk_after_nba(dut)
        assert got == 0, f"Reset cycle {i}: out_clk should be 0, got {got}"

    # Deassert reset safely between edges
    await FallingEdge(dut.clk)
    dut.reset.value = 1

    # Now model expected behavior starting from cleared state (clk_count=0)
    exp_count = 0
    for cycle in range(6):
        old = exp_count
        exp_out = exp_out_from_old_count(old)
        exp_count = (exp_count + 1) & 0x3

        await RisingEdge(dut.clk)
        got = await sample_out_clk_after_nba(dut)
        assert got == exp_out, (
            f"Post-reset cycle {cycle}: expected out_clk={exp_out} "
            f"from old_count={old:02b}, got {got}"
        )


@cocotb.test()
async def test_divide_by_4_pattern(dut):
    cocotb.log.info("Check divide-by-4 out_clk pattern")
    await start_clock_in_reset(dut)
    await apply_sync_reset_active_low(dut, cycles=2)

    exp_count = 0
    observed = []
    expected = []

    for _ in range(16):
        old = exp_count
        expected.append(exp_out_from_old_count(old))
        exp_count = (exp_count + 1) & 0x3

        await RisingEdge(dut.clk)
        observed.append(await sample_out_clk_after_nba(dut))

    assert observed == expected, f"Pattern mismatch.\nExpected: {expected}\nObserved: {observed}"


@cocotb.test()
async def test_reset_midrun_restart(dut):
    cocotb.log.info("Verify reset mid-run restarts sequence")
    await start_clock_in_reset(dut)
    await apply_sync_reset_active_low(dut, cycles=2)

    # Run some cycles from known start
    exp_count = 0
    for _ in range(6):
        old = exp_count
        exp_out = exp_out_from_old_count(old)
        exp_count = (exp_count + 1) & 0x3

        await RisingEdge(dut.clk)
        got = await sample_out_clk_after_nba(dut)
        assert got == exp_out

    # Assert reset mid-run (active-low) between edges
    await FallingEdge(dut.clk)
    dut.reset.value = 0

    await RisingEdge(dut.clk)
    got = await sample_out_clk_after_nba(dut)
    assert got == 0, "out_clk must be 0 on reset edge"

    await RisingEdge(dut.clk)
    got = await sample_out_clk_after_nba(dut)
    assert got == 0, "out_clk must remain 0 while reset asserted"

    # Release reset between edges
    await FallingEdge(dut.clk)
    dut.reset.value = 1

    # Sequence should restart as if count=0
    exp_count = 0
    for cycle in range(8):
        old = exp_count
        exp_out = exp_out_from_old_count(old)
        exp_count = (exp_count + 1) & 0x3

        await RisingEdge(dut.clk)
        got = await sample_out_clk_after_nba(dut)
        assert got == exp_out, (
            f"Restart cycle {cycle}: expected out_clk={exp_out} "
            f"from old_count={old:02b}, got {got}"
        )
        
# ----------------------------
# Pytest wrapper (hidden runner)
# ----------------------------
def test_clock_divider_hidden_runner():
    import os
    from pathlib import Path
    from cocotb_tools.runner import get_runner

    sim = os.getenv("SIM", "icarus")
    proj_path = Path(__file__).resolve().parent.parent

    sources = [proj_path / "sources/clock_divider.sv"]

    runner = get_runner(sim)
    runner.build(
        sources=sources,
        hdl_toplevel="clock_divider",
        always=True,
    )
    runner.test(
        hdl_toplevel="clock_divider",
        test_module="test_clock_divider_hidden"  # runs tests in this file
    )