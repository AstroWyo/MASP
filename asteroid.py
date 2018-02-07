def asteroid(astNm,obsCode)
	print ('Checking Packages...')
	from astropy.io import fits
	from astropy.wcs import WCS
	from astropy.time import Time
	from astropy import units as u
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


	home = expanduser('~')
	fileDir = '%s/Desktop/Wy_Analysis_Files/*.fits'%(home)
	asteroidPics = sorted(glob.glob(fileDir))

	#Replacing Spaces with Underscores in Filenames
	print ('Fixing File Names...')
	picList = []

	for i in range (0,len(asteroidPics)):
		pic = asteroidPics[i]
		picFixed = asteroidPics[i].replace(' ','_')
		os.rename(pic, picFixed)
		time.sleep(.01)
		picList.append(picFixed)
		print (picFixed)

	f = fits.open(picList[0])
	h = f[0].header
	f.close()

	print ('All files formated correctly')
	print ('Reading Headers')

	time.sleep(.1)

	expTime = h['EXPTIME']
	fTime = h['DATE-OBS']

	fOne = fits.open(picList[-1])
	hOne = fOne[-1].header
	fOne.close()

	fOneTime = hOne['DATE-OBS']

	time.sleep(.5)
	print ('Gathering Time Info...')
	f = fits.open(picList[0])
	h = f[0].header
	f.close()

	#Making a Time Obs List and julian dates
	unTime = []
	timeList = []
	for k in range(0, len(picList)):
		f = fits.open(picList[k])
		h = f[0].header
		f.close()
		timeg = h['DATE-OBS']
		unTime.append(timeg)
		parse = parser.parse(timeg)
		ti1 = parse.strftime("%Y-%m-%d %H:%M:%S")
		timeList.append(ti1)
		print ('Time ' + ti1 + ' Read')
		time.sleep(.01)
	print ('Made Time List')

	#making julian dates
	t = Time(unTime, format='isot', scale='utc')
	julianList = []
	for j in range(0, len(picList)):
		julian = t[j].jd
		julianList.append(julian)
		print (julian)
	print ('Created Julian Dates')
	time.sleep(.5)
	print ('Parsing Times')
	parsed = parser.parse(fTime)
	parsed1 = parser.parse(fOneTime)

	#un-parsing
	time.sleep(.5)
	startTime = parsed.strftime('%Y-%m-%d %H:%M:%S')
	endTime = parsed1.strftime('%Y-%m-%d %H:%M:%S')
	print ('Start Observation Time : '+ startTime)
	print ('End Observation Time : '+ endTime)

	print ('Talking to Solar System Dynamics Group, Jet Propulsion Laboratory Pasadena CA 91109 USA')
	elements = callhorizons.query(asteroidName)
	elements.set_discreteepochs(julianList)
	elements.get_ephemerides(obsCode)

	#uncomment the next line if you are having a problem with this part of the code and go to the link printed in the command line or terminal
	#print (elements.query)

	time.sleep(1)
	RA = elements['RA']
	DEC = elements['DEC']
	time.sleep(1)
	print ('Generating Epheris')
	print ('-------Epheris-------')
	print (RA)
	print (DEC)
	print ('-------Epheris-------')
	time.sleep(1)
	print ('Finding WCS')
	time.sleep(1)
	W3 = []
	for w in range(0,len(asteroidPics)):
		W2 = WCS('%s'%(asteroidPics[w]))
		W3.append(W2)
		print ('Found WCS for file:' + (asteroidPics[w]))
		time.sleep(.01)

	print ('Starting photometry')
	time.sleep(1)
	xlist = []
	ylist = []

	'''
	for f in range (0, len(picList)):

	'''
	for w in range(0,len(picList)):
		x,y=W2.all_world2pix(RA[w],DEC[w],0)
		print (x)
		print (y)
		xlist.append(x)
		ylist.append(y)
		time.sleep(.01)
		return;
