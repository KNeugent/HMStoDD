import numpy as np

def toDD (raH, raM, raS, decD, decM, decS):
    '''
    Returns a 2D array of RA and Dec in decimal degrees.
   
         Parameters:
              raH (int): RA (hours)
              raM (int): RA (minutes)
              raS (int): RA (seconds)
              decD (int): Declination (degrees)
              decM (int): Declination (minutes)
              decS (int): Declination (seconds)

         Returns:
              raDecDD ([int,int]): array of RA and Dec in decimal degrees
    '''
    raDD = (raH)*15.+raM/4.+raS/240.
    decDD = (np.abs(decD)+decM/60.+decS/3600.)*np.sign(decD)
    raDecDD = [raDD,decDD]
    return raDecDD
