from optimize import *
from targets_anne import *
import runmodel as rml

rml.set_model('model-anne.py')

######  CK #########

def optimize_AIA(generate = True, randomseedenabled = False, seeds = 100, view = True):
    optimize_group(generate, 'CK', CKAconditions, CkAtargets, randomseedenabled, seeds, view = view)
	



#########  MAIN ########

def print_help():
    print('help of script optimize.py')
    print('-h : this help')
    print('-m : set the model to optimize')
    print('-r : with random seed')
    print('-v : characterize random seed')
    print('-w : characterize variability of random seed')
    print('CK,SL,I,ALL : optimize the parameters of the specified compound')
    print('default : optimize I with all conditions (including burst delay inference)')

def main_optimize():
    #estimate_volumes_CK()
    #exit()
    import sys
    generate = True
    randomseedenabled = False
    target = 'optimize_'
    def targetfunc(tag):
        if target == 'optimize_':
            func = target+tag
            def mfunc(view = True): 
                return globals()[func](generate, randomseedenabled, view=view)
        else:
            def mfunc(view = True): 
                return globals()[target](tag)
        return mfunc

    if len(sys.argv) > 1:
        i = 1
        done = False
        while  i < len(sys.argv) and not done:
            current = sys.argv[i].upper()
            print(current)
            if current == '-H':
                print_help()
            elif current == '-M':
                from runmodel import set_model
                set_model(sys.argv[i+1])
                i += 1
            elif current == '-R':
                randomseedenabled = True
            #elif current == '-W':
            #    target = 'estimate_variability'
            #elif current == 'ALL':
            #    targetfunc('CK')(view = False)
            #    targetfunc('SL')(view = False)
            #    targetfunc('I')(view = False)
            #    done = True
            elif target+current in globals() or target in globals():
                targetfunc(current)()
                done = True
            else:
                print('Unknow option : ', sys.argv[i])
                print_help()
                done = True
            i += 1
        if not done:
            targetfunc('AIA')()
    else: 
        optimize_AIA(generate, randomseedenabled)


if __name__ == '__main__':
    #test_volume()
    main_optimize()

