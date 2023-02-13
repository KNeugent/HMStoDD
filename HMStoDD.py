import numpy as np

# inputs ra in hms and dec in dms
# outputs array of [ra, dec] in decimal degrees
def toDD (raH, raM, raS, decD, decM, decS):
    raDD = (raH)*15.+raM/4.+raS/240.
    decDD = (np.abs(decD)+decM/60.+decS/3600.)*np.sign(decD)
    return [raDD,decDD]
