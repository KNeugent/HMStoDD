# HMStoDD
Convert a list of sexagesimal coordinates to a list of decimal degree coordinates.

Input: a txt file with each line in the form of HH MM SS +DD MM SS
Output: a numpy array of decimal degree RA and Dec values

Note: Yes, this can be done in astropy, but it is needlessly slow.

