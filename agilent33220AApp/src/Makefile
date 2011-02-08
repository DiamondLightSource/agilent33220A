TOP=../..

include $(TOP)/configure/CONFIG

# -------------------------------
# Build an Diamond Support Module
# -------------------------------

#LIBRARY_IOC += xxx

# xxxRecord.h will be created from xxxRecord.dbd
#DBDINC += xxx.h

# xxxRecord.dbd will be installed into <top>/dbd
#DBD += xxx.dbd

# The following are compiled and added to the support library
#xxx_SRCS += xxxCodeA.c
#xxx_SRCS += xxxCodeB.c

# We need to link against the EPICS Base libraries
#xxx_LIBS += $(EPICS_BASE_IOC_LIBS)


# ------------------------
# Build an IOC Application
# ------------------------

PROD_IOC = agilent33220A

# agilent33220A.dbd will be installed into <top>/dbd
DBD += agilent33220A.dbd

# agilent33220A.dbd will be created from these files
agilent33220A_DBD += base.dbd
#agilent33220A_DBD += xxx.dbd

# agilent33220A_registerRecordDeviceDriver.cpp will be created
# agilent33220A.dbd
agilent33220A_SRCS += agilent33220A_registerRecordDeviceDriver.cpp

# These two lines are needed for non-vxWorks builds, such as Linux
agilent33220A_SRCS_DEFAULT += agilent33220AMain.cpp
agilent33220A_SRCS_vxWorks += -nil-

# Add locally compiled object code
#agilent33220A_SRCS +=

# The following adds object code from base/src/vxWorks
agilent33220A_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# This line says that this IOC Application depends on the
# xxx Support Module
#agilent33220A_LIBS += xxx

# We need to link this IOC Application against the EPICS Base libraries
agilent33220A_LIBS += $(EPICS_BASE_IOC_LIBS)

# ---------------------------------------------------

# NOTE: To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
#
# The difference between a file with an "st" extension
# and one with an "stt" extension is:
# The "st" extension files get passed through the C preprocessor
# whereas the "stt" files do not.

#ifneq ($(SNCSEQ),)
    # This builds sncExample as a component of agilent33220A
#    agilent33220A_SNCFLAGS += +r
#    agilent33220A_DBD      += sncExample.dbd
#    agilent33220A_SRCS     += sncExample.stt
#    agilent33220A_LIBS     += seq pv

    # The following builds sncExample as a standalone application
#    PROD_HOST           += sncExample
#    sncExample_SNCFLAGS += +m
#    sncExample_SRCS     += sncExample.stt
#    sncExample_LIBS     += seq pv
    # Here, we need to specify the dependency on EPICS Base libraries
    # again because this is a standalone application and
    # not part of agilent33220A
#    sncExample_LIBS     += $(EPICS_BASE_HOST_LIBS)
#endif

include $(TOP)/configure/RULES
