#!/bin/env dls-python2.6
from pkg_resources import require
require("dls_serial_sim")

from dls_serial_sim import serial_device, CreateSimulation

class agilent33220A_sim(serial_device):

    Terminator = "\n"    

    def __init__(self):
        # place your initialisation code here
        serial_device.__init__(self)
        self.values = {
        	"FUNC": "SIN",
        	"FREQ": 1000.0,
        	"VOLT": 10.0,
        	"VOLT:OFFS": 5.0,
        	"OUTP": 0,
        	"FUNC:SQU:DCYC": 50.0,
        	"FUNC:RAMP:SYMM": 50.0,
        	"FUNC:PULS:WIDT": 0.000001,
        	"FUNC:PULS:TRAN": 0.000000005,
        	"TRIG:SOUR": "IMM",
        	"BURS:MODE": "TRIG",
        	"BURS:NCYC": 1.0,
        	"BURS:STAT": 0
        }        	

    def reply(self,command):
        # reply to commands here
        if command.endswith("?"):
        	key = command.rstrip("?")
        	value = None
        else:
        	key, value = command.split(" ",1)
        if key in self.values:
        	typ = type(self.values[key])
        else:
        	return
        if value is None:
        	if typ == str:
        		return self.values[key]
        	elif typ == int:
        		return "%d" % self.values[key]
        	elif typ == float:
        		return "%+.11E" % self.values[key]
        else:
        	self.values[key] = typ(value)

if __name__=="__main__":
    # run our simulation on the command line. Run this file with -h for help
    CreateSimulation(agilent33220A_sim)
    raw_input()
