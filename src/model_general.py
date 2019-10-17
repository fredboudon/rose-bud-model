#### Not optimized but part of the model

I_threshold = 3.
slope = 0.281857451404
intercept = 0.630237580994

def burst_delay_law(I):
    if I < I_threshold : return  (I - intercept)/ slope 
    return None

def I_law(duration):
    if not duration is None : return  duration * slope + intercept 
    return None


SugSlope = 0.461594288378552*100
SugIntercept = 10.3772508030731

def agar2nodesugar(agarcontent):
    return SugSlope * agarcontent + SugIntercept


def node2agarsugar(nodesugar):
    return (nodesugar - SugIntercept)/SugSlope

def ckIPR2IP(IPR):
    return 0.0162365776626706*IPR + 0.319291823937939
