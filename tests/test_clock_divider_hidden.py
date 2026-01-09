# test_clock_divider_hidden.py
#
# Cocotb testbench for:
# module clock_divider(input reset, input clk, output reg out_clk);
#
# Note: DUT uses synchronous reset with *active-low* behavior (if (!reset) reset state),
# i.e. reset asserted when reset == 0.

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, ReadOnly


async def apply_sync_reset_active_low(dut, cycles: int = 2):
    """Assert active-low synchronous reset for N rising edges, then deassert."""
    dut.reset.value = 0  # assert reset (active-low in this DUT)
    for _ in range(cycles):
        await RisingEdge(dut.clk)
    dut.reset.value = 1  # deassert reset
    await RisingEdge(dut.clk)


def expected_out_from_old_count(old_count: int) -> int:
    """out_clk is assigned old clk_count[1] (since NBA in same always block)."""
    return (old_count >> 1) & 0x1


@cocotb.test()
async def test_clock_divider_basic(dut):
    """
    Verifies:
      - synchronous active-low reset behavior (reset=0 clears count/out on clock edge)
      - counter increments mod-4 when reset=1
      - out_clk follows MSB of *previous* count value each rising edge
    """
    # Start clock
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # Initialize inputs
    dut.reset.value = 1  # deasserted
    await RisingEdge(dut.clk)

    # Apply reset
    await apply_sync_reset_active_low(dut, cycles=2)

    # After reset deassertion, internal count should be 0 and out_clk 0 (from last reset edge)
    # We can't directly read clk_count (not a port), so we track expected behavior.
    exp_count = 0

    # Check a handful of cycles
    for cycle in range(12):
        old_count = exp_count
        exp_out = expected_out_from_old_count(old_count)
        exp_count = (exp_count + 1) & 0x3  # mod-4 increment

        await RisingEdge(dut.clk)
        await ReadOnly()

        got_out = int(dut.out_clk.value)
        assert got_out == exp_out, (
            f"Cycle {cycle}: out_clk mismatch. "
            f"Expected {exp_out} (from old_count={old_count:02b}), got {got_out}"
        )


@cocotb.test()
async def test_clock_divider_reset_midrun(dut):
    """
    Verifies reset behavior when asserted mid-run:
      - when reset is driven low, on the next rising edge out_clk becomes 0
      - counting restarts after reset is released
    """
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    dut.reset.value = 1
    await RisingEdge(dut.clk)

    # Run a few cycles to move away from zero state
    exp_count = 0
    for _ in range(5):
        old_count = exp_count
        exp_out = expected_out_from_old_count(old_count)
        exp_count = (exp_count + 1) & 0x3
        await RisingEdge(dut.clk)
        await ReadOnly()
        assert int(dut.out_clk.value) == exp_out

    # Assert reset (active-low) and check it takes effect synchronously
    dut.reset.value = 0  # assert
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert int(dut.out_clk.value) == 0, "out_clk should be 0 after synchronous reset edge"

    # Hold reset one more cycle
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert int(dut.out_clk.value) == 0, "out_clk should remain 0 while reset is asserted"

    # Release reset and ensure counting restarts from 0
    dut.reset.value = 1  # deassert
    exp_count = 0
    for cycle in range(8):
        old_count = exp_count
        exp_out = expected_out_from_old_count(old_count)
        exp_count = (exp_count + 1) & 0x3

        await RisingEdge(dut.clk)
        await ReadOnly()
        assert int(dut.out_clk.value) == exp_out, (
            f"Post-reset cycle {cycle}: expected {exp_out} from old_count={old_count:02b}, "
            f"got {int(dut.out_clk.value)}"
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

    # Adjust this path/name to match your repo layout.
    # Per your example: use sources/ not rtl/!
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