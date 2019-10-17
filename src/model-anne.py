
# The optimizable parameters are defined in this file
paramfile = 'parameters-anne.py'

exec(open(paramfile).read(), globals(),locals())

import model_paper  as mp

def aia2iia(aia):
    return aiaslope * aia + aiaintercept

def ckN2ck(ck):
    return ckslope * ck + ckintercept

def eval_model(aia, sugar, gr24 = 0, bap = 0):
    """ Main function of the model """
    auxin = aia2iia(aia)
    sl, ck, Sck, Ssl, I = mp.eval_model(auxin, sugar, gr24, bap)
    ck = ckN2ck(ck)
    return sl, ck, Sck, Ssl, I



