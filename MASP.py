print ('Checking Packages...')
from astropy.io import fits
from astropy.wcs import WCS
from astropy.time import Time
from astropy import units as u
from astropy.coordinates import EarthLocation, SkyCoord, ICRS
from astropy.coordinates import solar_system_ephemeris, EarthLocation
from astropy.coordinates import get_body_barycentric, get_body, get_moon
from astropy.io import fits
from astropy.wcs import WCS
from dateutil import parser
from os import *
from os.path import expanduser
from os.path import expanduser
from photutils import aperture_photometry
from PyClasses.batch_functions import functions
from pyds9 import *
print ('Importing Packages')
import callhorizons
import datetime
import glob
import math
import matplotlib.pyplot as plt
import numpy
import os
import pyds9
import re
import sys
import time

va = input("Are you doing variable star (V) or asteroid (A) photometry (type V or A respectivly)")
if va=='A':
	starNm = input("Target Star Name : ")
	variable(starNm)
	elif va=='V':
		astNm = input('Asteroid Name : ')
		obsCode = input('Observatory Code : ')
		asteroid(astNm, obsCode)
		astPhot(xlist, ylist)

	else :
		print('Not a valid code try again type V or A repectivley')










