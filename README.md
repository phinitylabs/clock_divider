# RC5 Encryption Core — Design, Completion & Debugging
This environment is built around an RTL implementation of the RC5 block cipher (16‑bit variant). The provided testbench drives a start/done handshake and compares ciphertext against golden outputs:
- Spec → RTL: Implement a 16‑bit RC5 decryption module and integrate it with the existing interface.
- Code Completion (Round Update): Complete the per‑round update logic
- Code Completion (Round Counter & Handshake): Finish the round counter and done assertion
- Debugging (Algorithmic Correctness): Fix operator/ordering errors
- Debugging (Rotations & Boundaries): Correct rotation direction/width
- Code Comprehension (Verification/Testbench): Explain the testbench’s verification strategy

## Industry Relevance of RC5
RC5 is a symmetric-key block cipher, notable for its simplicity, efficiency, and parameterizable architecture. Its design allows variable block sizes (32, 64, or 128 bits), flexible key lengths (up to 2040 bits), and adjustable encryption rounds (up to 255), making it highly adaptable to different security requirements and resource constraints.

In real-world applications, RC5 has been deployed across multiple security-critical domains including disk encryption for storage devices, secure messaging applications, Virtual Private Networks (VPNs), and medical data protection systems. The cipher was integrated into major cryptographic libraries such as RSA Security's BSAFE and JSAFE, and became the subject of the RSA Secret-Key Challenge (1997-2007). Its simplicity and efficiency makes it an attractive choice for hardware implementations in FPGAs and ASICs, where its minimal logic requirements and parameterizable nature allow for optimized area-power-performance trade-offs. While more advanced standards have increased in industry adoption, RC5 remains relevant for specific and/or legacy use-cases.

In RTL design development scenarios, the above categories of tasks have to be incorporated on various occasions during the hardware architecture development stage.
- Spec → RTL is a very first step towards any RTL realization from the specification. Here, the textual form of hardware description is translated into a HDL form using VHDL/Verilog/Systemverilog programming languages. Understanding the specification carefully and converting the functionality specified into a synthesizable RTL format is a critical skill needed for RTL design engineers.
- Code Completion category is based on completing a partially written RTL code with some guidance comments to complete the remaining sections. In an industrial scenario, the code completed partially by an engineer may need to be completed by another engineer based on project needs. On such events, specification with paritial RTL code will be handled by the required to ensure the completion of RTL design
- Debugging examples are based on reading the logs from the testbench to identify the presence of bug(s) in the RTL and providing a fix. Functional bugs are captured during testing and verification phase and the subsequent fix has to be applied for proper functional follow-up with the specification.
- Code Comprehension in this scenario refers to understanding the purpose of test(s) incorporated in the testbench. The necessity of a particular testcase has to be properly justified to understand its role in improving the coverage.
  
To keep environments cleanly organized and self-contained, we have implemented the following organization scheme:
The environment consists of a single github repository with several different commits in main, issues, and PRs that are of interest. Within the environment, each task consists of a tuple:
(hash of “context” code [broken/unsolved] on main, id of closed issue that represents prompt to agent, hash of solution branch, hash of main with solution branch merged in)
Most tasks involve adding or fixing some SystemVerilog code within the rtl directory. Solution branches may usually include the fixed code within the rtl directory, but they may also include some code inside of a tb or verif directory. Furthermore, we provide a harness directory within each solution branch. This harness provides the building blocks of the reward function, that could be further customized and tweaked. As such, we hold out the harness so the agent does not observe it. tb/verif code may or may not be present for the agent—it may choose to verify the answer itself by writing code there and testing it before submission. In this set of tasks, there is no requirement to write a testbench, so the harness never checks the correctness of testbench code.

We list the tuples for the tasks so you can explore them:\
Spec-to-rtl: `(233cbdcb2a833812d5c9254d4f0d82b51b1a744b, 1, eb80c87c3bee50415edf1fa4aa4f4f1dce0d72a5, 07dc08f72a82b647177b292b2e16c6466bb9c728)`
  - Industry context: Feature bring-up in crypto/security IPs during RTL, before SoC integration.
  - Real-life failure modes: Wrong round order/keys, rotation direction/width errors, endianness mismatches, handshake/reset misuse.
  - Human ETA: 0.5–2 days.

Code completion 1: `(464b81613b39bf3cfe86c6c45ae0b59f7c11fcf8, 3, 0abf6c71621b2c28b3cee142017d2e7727fb1023, a71538b22dccfc027e8c0beb245f461dc74497a0)`
  - Industry context: Complete datapath arithmetic/bit-manipulation during micro-architecture closure.
  - Real-life failure modes: Operator precedence, missing mod 2<sup>w</sup>, incorrect rotate amount, truncation/bit-growth, stale register use.
  - Human ETA: 0.5-1 day

Code completion 2: `(de918c42da3deaa79ec7a78e7486eafeb6a517e2, 5, dff9df38a382a74c9c8742135b98c29f4df925e3, ee14a9eded468dee63f1811b5fae9b1078a6a77a)`
  - Industry context: Control/FSM finalization and latency signaling before block-level verification.
  - Real-life failure modes: Off-by-one rounds, premature/late done, counter not reset, start re-trigger, pulse vs sticky done.
  - Human ETA: 0.5–1 hours.

Debugging 1: `(bf53a9d3b44dd2629108272b0ece771bc846f41f, 7, 5d969d0826b3ad0d55bb3425c957573c8471165b, 79a750177bab8d4f098f9b7853e5995fa98d87d3)`
  - Industry context: Post-simulation debug when vectors mismatch golden models in block verification.
  - Real-life failure modes: XOR vs OR, add vs sub, A/B operand swap, blocking/nonblocking sequencing bugs.
  - Human ETA: 1–4 hours.

Debugging 2: `(51671aaab94b48f44b740d7431022a8e52a505ba, 9, 74f955ec2cdb9439867e61646d483dd8291d3904, 398037515c386373ad960b8500fb791bfa78bb1c)`
  - Industry context: Bit-ops correctness and corner-case handling during RTL stabilization.
  - Real-life failure modes: Shift instead of rotate, missing modulo on shift amount, shift-by-width undefined behavior, endianness mistakes.
  - Human ETA: 1–3 hours.

Code Comprehension: `(5d0fac6732ce44cfb5b0e35fee9a02144547fb53, 11, 3ba99c292329e9928c4d7af59691e74a449c2bf0, 64b0d9cc1c62a8555d68aab2b17dadb1266b8ce7)`
  - Industry context: DV/testbench review to ensure stimulus, latency checks, coverage align with spec before sign-off.
  - Real-life failure modes: Misread handshake/latency, reset sequencing issues, misinterpreting expected outputs, overlooking coverage gaps.
  - Human ETA: 30–90 minutes.
