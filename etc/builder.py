from iocbuilder import AutoSubstitution
from iocbuilder.modules.streamDevice import AutoProtocol
from iocbuilder.modules.busy import Busy

class agilent33220A(AutoSubstitution, AutoProtocol):
    '''Controls an agilent 33220A function generator'''

    Dependencies = (Busy, )

    ## Parse this template file for macros
    TemplateFile = 'agilent33220A.template'

    ## This is the streamDevice protocol file to use
    ProtocolFiles = ['agilent33220A.proto']


