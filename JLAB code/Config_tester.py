# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 09:27:24 2021

@author: mayne
"""
import configparser
config = configparser.ConfigParser()

config['DEFAULT'] = {'Monte-Carlo trials' : '100000',
                     'Spectrometer (1=HMS, 2=SHMS, 3=..)' : '1',
                     'Sectrometer momentum (in MeV/c)' : '1560.0',
                     'Spectrometer angle (in degrees)' : '40.0',
         	         'M.C. DP/P  down limit' : '-15.0',
                     'M.C. DP/P  up   limit' : '15.0', 
    	             'M.C. Theta down limit (mr)' : '-50.0',
     	             'M.C. Theta down limit (mr)_2' : '50.0',
    	             'M.C. Phi   down limit (mr)' : '-100.0',
     	             'M.C. Phi   down limit (mr)_2' : '100.0',
     	             'Horiz beam spot size in cm (Full width of +/- 1 sigma)' : '0.01',
     	             'Vert  beam spot size in cm (Full width of +/- 1 sigma)' : '0.01',
     	             'Thickness of target (Full width, cm)' : '0.294',
                     'Raster full-width x (cm)' : '0.1',
                     'Raster full-width y (cm)' : '0.1',
     	             'DP/P  reconstruction cut (half width in % )' : '50.0',
     	             'Theta reconstruction cut (half width in mr)' : '100.0',
     	             'Phi   reconstruction cut (half width in mr)' : '100.0',
     	             'ZTGT  reconstruction cut (Half width in cm)' : '50.0',
     	             'one radiation length of target material (in cm)' : '18.80',
                     'Beam x offset (cm)  (+x = beam left)' : '0.0',
     	             'Beam y offset (cm)  (+y = up)' : '0.0',
                     'Target z offset (cm) (+z = downstream (0.25))' : '0.0',
                     'Spectrometer x offset (cm) (+x = down)' : '0.0',
                     'Spectrometer y offset (cm)' : '0.143',
                     'Spectrometer z offset (cm)' : '0.0',
                     'Spectrometer xp offset (mr)' : '1.1',
                     'Spectrometer yp offset (mr)' : '0.0',
     		         'particle identification :(e=0, p=1, d=2, pi=3, ka=4)' : '0',
     		         'flag for multiple scattering' : '1',
     		         'flag for wire chamber smearing' : '1',
     	             'flag for storing all events (including failed events with stop_id > 0)' : '1',
                     'flag for beam energy, if >0 then calculate for C elastic' : '0',
                     'flag to use sieve' : '0' }


with open('Input_Values_MC_HMS_SINGLE.ini', 'w') as configfile:
    config.write(configfile)


