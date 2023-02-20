import numpy as np

def to_DD (ra_H, ra_M, ra_S, dec_D, dec_M, dec_S):
    '''
    Returns a 2D array of RA and Dec in decimal degrees.
   
         Parameters:
              ra_H (float): RA (hours)
              ra_M (float): RA (minutes)
              ra_S (float): RA (seconds)
              dec_D (float): Declination (degrees)
              dec_M (float): Declination (minutes)
              dec_S (float): Declination (seconds)

         Returns:
              ra_Dec_DD ([float,float]): array of RA and Dec in decimal degrees
    '''
    ra_DD = (ra_H)*15.+ra_M/4.+ra_S/240.
    dec_DD = (np.abs(dec_D)+dec_M/60.+dec_S/3600.)*np.sign(dec_D)
    ra_Dec_DD = [ra_DD,dec_DD]
    return ra_Dec_DD
