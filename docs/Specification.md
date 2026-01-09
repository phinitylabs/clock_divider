## Specification: `clock_divider`

Generate a slower clock output (`out_clk`) from an input clock (`clk`) using a small counter-based divider.

### Interface

**Inputs**

* `clk`: reference clock; all state updates occur on the rising edge.
* `reset`: synchronous, **active-low** reset.

**Output**

* `out_clk`: divided clock output.

---

### Reset behavior

On the rising edge of `clk`, if **`reset` is low (0)** (reset asserted):

* `out_clk` shall be driven low.
* The internal divider state (`clk_count`) shall be cleared to zero.

---

### Normal operation

On each rising edge of `clk` when **`reset` is high (1)** (reset deasserted):

* The internal 2-bit counter `clk_count` shall increment by 1 (modulo 4).
* `out_clk` shall be assigned the **most significant bit (MSB) of the counter value *before* increment** (i.e., `out_clk <= old_clk_count[1]`).

> Note: Because the RTL uses nonblocking assignments for both `clk_count` and `out_clk`, the output reflects the *previous* counter MSB, not the newly incremented counter MSB in the same cycle.

---

### Output characteristics

* `out_clk` shall be a periodic waveform derived from the counter MSB (with a one-cycle latency relative to the updated counter value).
* The output shall have a nominal divide ratio of **4** relative to `clk` (i.e., `out_clk` frequency ≈ `clk/4`) with a repeating 4-cycle pattern.
* The duty cycle shall be approximately **50%** (two input cycles high, two input cycles low) under continuous operation.

---

### Expected per-posedge `out_clk` sequence (after reset release)

Assuming reset drives `clk_count=0`, the `out_clk` values observed immediately after each rising edge follow:

`0, 0, 1, 1, 0, 0, 1, 1, ...`

(repeats every 4 rising edges).