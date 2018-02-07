''' batch photometry functions
'''

from astropy.io import fits
from astropy import wcs
from photutils import CircularAperture
from photutils import aperture_photometry
from photutils import CircularAnnulus
from astropy.table import hstack
from pyds9 import *
from os.path import expanduser
home=expanduser("~")

ds=DS9()

class functions:
	def getPhotometry(self,x,y,data,rphot,rin,rout,plot_on_ds9,image_name): #function to retrieve photometry of a target
		#rphot=5.
		#rin=10.
		#rout=20.
		#rin=rphot+2 #give dead zone outside of the rphot value
		#rout=rin+4 #provide plenty of room for background measurment
		#pos=[(30.,30.),(40.,40.)] #positions of photometry
		pos=[(x,y)]
		apertures=CircularAperture(pos,r=rphot)
		annulus_apertures=CircularAnnulus(pos,r_in=rin,r_out=rout)

		rawflux_table=aperture_photometry(data,apertures, method='exact') #subpixel divides pixels up to determine aperature in or out
		bkgflux_table=aperture_photometry(data,annulus_apertures, method='exact')
		phot_table=hstack([rawflux_table,bkgflux_table],table_names=['raw','bkg'])
		bkg_mean=phot_table['aperture_sum_bkg']/annulus_apertures.area()
		bkg_sum=bkg_mean*apertures.area()
		final_sum=phot_table['aperture_sum_raw']-bkg_sum
		phot_table['residual_aperture_sum']=final_sum

		#print bkg_mean
		#print bkg_sum
		#print phot_table
		

		a=phot_table['residual_aperture_sum'][0]
		#print a
		#stop
		
		
		
		if plot_on_ds9==True:
			ds=DS9()
			ds.set('file %s'%(image_name))
			reg1='regions command "annulus %s %s %s %s #color=blue"'%(x,y,rin,rout)
			reg2='regions command "circle %s %s %s #color=yellow"'%(x,y,rphot)
			ds.set('%s'%(reg1))
			ds.set('%s'%(reg2))


		return round(a,3)


