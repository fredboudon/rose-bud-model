
from targets import *
from model_general import *
################ Anne thesis experiment


CkAtargets = [8.96, 10.12, 12.67, 5.78, 6.87]
CkAtargets = list(map(ckIPR2IP, CkAtargets))

CKAAIAconditions = [0.83, 1.58, 1.55, 0.95, 0.95]

CKASugconditions = [54.07, 209.48, 173.79, 120.40, 115.20]
CKASugconditions = list(map(node2agarsugar, CKASugconditions))


# aIa, sugar, gr24, bap
CKAconditions = list(zip(CKAAIAconditions, CKASugconditions, [0 for i in range(len(CKAAIAconditions))], [0 for i in range(len(CKAAIAconditions))]))

order = list(range(len(CKASugconditions)))
order.sort(key=lambda i : CKASugconditions[i])

CKAconditions = [CKAconditions[i] for i in order]
CkAtargets = [CkAtargets[i] for i in order]