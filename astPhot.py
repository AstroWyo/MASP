def astPhot(xlist, ylist)
	from astropy.io import fits
	from astropy.wcs import WCS
	from photutils import aperture_photometry
	from PyClasses.batch_functions import functions
	import math
	import pyds9
	from pyds9 import *
	import matplotlib.pyplot as plt
	import os 
	import glob
	from os.path import expanduser
	from astropy.time import Time
	home=expanduser("~")
	functions = functions()
	#image_name='/Users/teaghensweckard/Wy_Analysis/RVdel'
	#im2 = fits.open('%s/Wy_Analysis/RVdel.fit'%(home))
	os.system('launchctl setenv XPA_METHOD local')
	os.system('export XPA_METHOD=local')
	ds = DS9()
	ds.set('zscale')

	#returns path name of file
	#im1 = glob.glob('%s/Wy_Analysis_Files/1663933-rv_del/*.fit'%(home))
	im1 = glob.glob('%s/Desktop/Wy_Analysis_Files/*.fits'%(home))

	#ref stars x and y and target
	#num7 file
	ref1x = 249
	ref1y = 968
	ref2x = 256
	ref2y = 731
	ref3x = 702
	ref3y = 291

	t1x = xlist
	t1y = ylist

	#magnitudes of ref stars to find naturalized mags.
	ref1m = 12.19
	ref2m = 9.93
	ref3m = 11.37
	t1m = 13.64


	refm = [ref1m, ref2m, ref3m, t1m]
	refx = [ref1x, ref2x, ref3x, t1x]
	refy = [ref1y, ref2y, ref3y, t1y]
	ra = []
	dec = []
	pho = []
	ins = []
	nmags = []
	s = []

	dp_hold = []
	#stop
	im=fits.open('%s'%im1[0])
	data = im[0].data
	try:
		t=im[0].header['MJD-OBS']
	except:
		t=im[0].header['JD']
	im.close()
	for f in range(0, len(im1)):
		im = fits.open('%s'%(im1[f]),'update')
		im[0].header['CD1_1']=float(im[0].header['CD1_1'])
		im[0].header['CD1_2']=float(im[0].header['CD1_2'])
		im[0].header['CD2_1']=float(im[0].header['CD2_1'])
		im[0].header['CD2_2']=float(im[0].header['CD2_2'])
		im.flush()
		im = fits.open('%s'%(im1[f]))
		w2 = WCS('%s'%(im1[f]))
		print (im1[f])
		
	#	for x in range(0, len(im)):
			#data = im[0].data
			#t = im[0].header['date-obs']
			#date, time = t.split("T")
			#hr, mt, sd = time.split(":")
			#mt = int(mt)
			#hr = int(hr)
			#mt = mt/60
			#ft = hr + mt
		data=im[0].data
			#t2 = im[x].header['date-obs']	
		try:
			t2=im[0].header['MJD-OBS']
		except:
			t2=im[0].header['JD']
			#date2, time2 = t2.split("T")
			#hr2, mt2, sd2 = time2.split(":")
			#mt2 = int(mt2)
			#hr2 = int(hr2)
			#mt2 = mt2/60
			#ft2 = hr2 + mt2

			#dt = ft2 - ft
			#dp = dt%11.9553
			#dp = str(dp)
			#dp_hold.append(dp)
			#print dp
		dt=(t2-t)*24

		dp=dt/100
		dp1=int(dp)
		if dp1<0:
			dp2=1-(dp1-dp)

		else:
			dp2=dp-dp1

		dp_hold.append(dp2)
		#print t, t2
		#print dt,dp
		#print dp1,dp2
		#print dp2
		
		#return dp
		im.close()
		s.append([])

		for i in range(0, len(refx)):
			

			if f==0:
				ra1, dec1 = w2.all_pix2world(refx[i], refy[i], 0)
				ra.append(ra1)
				dec.append(dec1)
				x = refx[i]
				y = refy[i]

			else:

				#stop
				x,y = w2.all_world2pix(ra[i],dec[i],0)


			if i==3:
				print (xlist[i],ylist[i])

			if i<3:
				phot = functions.getPhotometry(x,y,data,5, 10,15,True,im1[f])
			else:
				phot = functions.getPhotometry(xlist[f],ylist[f],data,5, 10,15,True,im1[f])
			#getPhotometry(self,x,y,data,rphot,rin,rout,plot_on_ds9,image_name)
			print (phot)

			if phot<=0:
				print ('error error error, source photon count is negative')

			else:
				#print 'Phot',phot
				#print 'X,Y', x,y
				inst = -2.5*math.log(phot)

			#ins[i] = insm
			#nmag = ins[i] + refm[i]
			#nmags.append(nmag)

			#targetnm = nmags[3]
			#nmags.remove(targetnm)

				s[f].append(inst)
			#s[f].append(nmags)
			
	#print s

	ploty = []


	#print len(s)
	#print s

	for i in range(0,len(s)):
		print (s[i])
		ploty.append(s[i][3])

	#dp[f]
	plt.plot(dp_hold,ploty, 'ro')
	plt.ylabel('Magnitude')
	plt.xlabel('Time')
	#plt.xlim(0.0, 1.0)
	plt.show()
	return;
