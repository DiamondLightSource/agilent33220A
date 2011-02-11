from pkg_resources import require
require("dls_serial_sim==1.15")

from dls_serial_sim import serial_device

class agilent33220A_sim(serial_device):

    Terminator = "\\n"

    def __init__(self):
        # place your initialisation code here
        serial_device.__init__(self)

    def reply(self,command):
        # reply to commands here
        return command

if __name__=="__main__":
    # run our simulation on the command line. Run this file with -h for help
    CreateSimulation(agilent33220A_sim)
    raw_input()
