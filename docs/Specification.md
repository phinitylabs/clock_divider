## Specification: `clock_divider`

### Purpose

Generate a slower clock output (`out_clk`) from an input clock (`clk`) using a small counter-based divider.

### Interface

* **Inputs**

  * `clk`: reference clock; all state updates occur on the rising edge.
  * `reset`: synchronous, active-high reset.
* **Output**

  * `out_clk`: divided clock output.

### Reset behavior

On the rising edge of `clk`, if `reset` is high:

* `out_clk` shall be driven low.
* The internal divider state shall be cleared to zero.

### Normal operation

On each rising edge of `clk` when `reset` is low:

* The internal 2-bit counter shall increment by 1 (modulo 4).
* `out_clk` shall follow the most significant bit (MSB) of the internal counter.

### Output characteristics

* `out_clk` shall be a periodic waveform derived from the counter MSB.
* The output shall have a nominal divide ratio of **4** relative to `clk` (i.e., `out_clk` frequency ≈ `clk/4`) with a repeating 4-cycle pattern.
* The duty cycle shall be approximately **50%** (two input cycles high, two input cycles low) under continuous operation.