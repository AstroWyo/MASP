# MASP

The Moving and Static Photometry tool was created to do accurate and quick photometry easily used by both students and long time astronomers. This is verstion 1 IT IS VERY BARE BONES. More features will be added in the future. This is the version for mac. 

## Download
To download the software follow instructions below for your Operating System. Make sure you have python 2.7 and python 3 installed.
### Mac
1. ```python -m pip install --user --no-deps numpy matplotlib photutils pyds9 callhorizons python-dateutil```

2. Move the MASP folder (the files from downloaded from github) to /Users/YourUserName/MASP for MAC or root\Users\YourUserName\MASP for Windows

3. Make a file in your Desktop called MASP this is where you will put your pictures for processing.

4. Install [DS9](http://ds9.si.edu/site/Home.html).

5. Install [X-Code](https://developer.apple.com/xcode/downloads/).
	1. ```xcode-select --install```
	2. Click install and follow on screen prompts

6. Go to the MASP folder and click on setup.py


## Use
1.	Mac
First put your pictures in the MASPpics folder
	1.	Open up a new terminal
	2.	```launchctl setenv XPA_METHOD local```
	3.	```export XPA_METHOD=local```
	4.	```cd MASP```
	5.	Asteroids
		1.	Put images to be processed in the MASPimages folder on your desktop
		2.	Click on MASP.py on your desktop
		3.	Follow on screen prompts and enter the correct information for your asteroid.
		4.	The information for reference stars and asteroids will be outputted into the MASP folder.
	6.	Variable Stars
		1.	Put images to be processed in the MASPimages folder on your desktop
		2.	Click on MASP.py on your desktop
		3.	Follow on screen prompts and enter the correct information for your star.
		4.	The information for reference stars and asteroids will be outputted into the MASP folder.

###### Congratulations

