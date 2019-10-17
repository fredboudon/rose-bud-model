
def get_param_file(modelfile):
    lnamespace = {}
    exec(open(modelfile).read(), lnamespace)
    paramfile = lnamespace['paramfile']
    return paramfile

#modelfile = 'model-anne.py'
modelfile = 'model_paper.py'
paramfile = get_param_file(modelfile)


def set_model(fname):
    global modelfile, paramfile
    modelfile = fname
    paramfile = get_param_file(modelfile)

def runmodel(auxin, sugar, gr24 = 0, bap = 0, values = None):
    
    namespace = {}
    if not values is None : namespace.update(values)

    # Execution of the model
    exec(open(modelfile).read(), namespace)
    eval_model = namespace['eval_model']
    sl, ck, ckresponse, slresponse, I = eval_model(auxin, sugar, gr24, bap)

    # retrieval of the values as a dict
    resvalues = { 'SL' : sl , 'CK' : ck, 'CKRESPONSE': ckresponse, 'SLRESPONSE': slresponse, 'I' : I }
    return resvalues