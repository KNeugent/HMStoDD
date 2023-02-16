import numpy as np

def toDD (raH, raM, raS, decD, decM, decS):
    '''
    Returns a 2D array of RA and Dec in decimal degrees.
   
         Parameters:
              raH (float): RA (hours)
              raM (float): RA (minutes)
              raS (float): RA (seconds)
              decD (float): Declination (degrees)
              decM (float): Declination (minutes)
              decS (float): Declination (seconds)

         Returns:
              raDecDD ([float,float]): array of RA and Dec in decimal degrees
    '''
    raDD = (raH)*15.+raM/4.+raS/240.
    decDD = (np.abs(decD)+decM/60.+decS/3600.)*np.sign(decD)
    raDecDD = [raDD,decDD]
    return raDecDD
