# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

# Makefile

# defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog
RTL_DIR ?= ../../rtl

VERILOG_INCLUDE_DIRS = $(RTL_DIR)

VERILOG_SOURCES += ../../rtl/rc5_enc_dec_param.sv ../../rtl/lfsr_8bit.sv
# use VHDL_SOURCES for VHDL files

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = rc5_enc_dec_param

# MODULE is the basename of the Python test file
MODULE = test_rc5_enc_dec_param

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim

