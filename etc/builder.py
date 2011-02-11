from iocbuilder import AutoSubstitution
from iocbuilder.modules.streamDevice import AutoProtocol

class agilent33220A(AutoSubstitution, AutoProtocol):
    '''Controls an agilent 33220A function generator'''

    ## Parse this template file for macros
    TemplateFile = 'agilent33220A.template'

    ## This is the streamDevice protocol file to use
    ProtocolFiles = ['agilent33220A.proto']


