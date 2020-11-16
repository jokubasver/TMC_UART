'''
Registers from the TMC2209 datasheet: https://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC2209_Datasheet_V103.pdf
'''
# ===== TMC2209 register set =====


# -----General registers-----
GCONF          =    0x00
GSTAT          =    0x01
IFCNT          =    0x02
SLAVECONF      =    0x03
OTP_PROG       =    0x04
OTP_READ       =    0x05
IOIN           =    0x06
FACTORY_CONF   =    0x07

# -----Velocity Dependent Control------
IHOLD_IRUN     =    0x10
TPOWERDOWN     =    0x11
TSTEP          =    0x12
TPWMTHRS       =    0x13
VACTUAL        =    0x22

# -----StallGuard Control------
TCOOLTHRS      =    0x14
SGTHRS         =    0x40
SG_RESULT      =    0x41
COOLCONF       =    0x42

# -----Sequencer Registers------
MSCNT          =    0x6A
MSCURACT       =    0x6B

# -----Chopper Control Registers------
CHOPCONF       =    0x6C
DRVSTATUS      =    0x6F
PWMCONF        =    0x70
PWMSCALE       =    0x71
PWM_AUTO       =    0x72
