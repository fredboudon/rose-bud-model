from defaultparameters import *

# defining parameters as paramname = value, lowerlimit, upperlimit

@defaultparameters
def CK():
    aiaslope     = 0.019124308011997004, 0, 1000
    aiaintercept = -1.061788165497787, -1000,1000
    ckslope    = 0.0001365800967321439, 0, 1000
    ckintercept    = 0.4933334133411975, -1000, 1000