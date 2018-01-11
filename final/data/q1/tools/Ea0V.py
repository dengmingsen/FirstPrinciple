#import matplotlib.pyplot as plt
import os,sys
import numpy as np 


def Fit_getMin(x,y):
	coef_2 = np.polyfit(x,y,3)
	xmin   = (-2*coef_2[1] + np.sqrt(4*coef_2[1]**2-12*coef_2[0]*coef_2[2]) )/(6*coef_2[0])
	return xmin, coef_2


def Bulk_mod(xipt,E,is_x_vol=False,verbose=False):

	"""
		@E:
			energy in unit of eV

		@xpit : 
			if is_x_vol == True , xipt is the volumn in unit of (\AA^3)
		            	== False, xipt is the cubic length in unit of (\AA)
		
		@details : 
			using 3rd polyfit with V-E 
	"""

	V = None
	if is_x_vol :
		V = xipt
	else:
		V = xipt**3

	#fitting with 3rd poly and get V_min
	V_min , coef_2  = Fit_getMin(V,E) 
	
	# calc Bulk modulus
	B_eva = (6*coef_2[0]*V_min+2*coef_2[1])*V_min # unit = eV/A^3
	B_pa  = B_eva * 1.6E+11 # J/m^3 = Pa
	B_gpa = B_pa * 10**-9  # GPa

	if verbose:
		print ("=========================")
		print ("Bulk modulus calculation :")
		print ("fit: ax^3 + bx^2 + cx + d")
		print ("a: %10.10f"%(coef_2[0]))
		print ("b: %10.10f"%(coef_2[1]))
		print ("c: %10.10f"%(coef_2[2]))
		print ("d: %10.10f"%(coef_2[3]))
		print ("Minimum: ")
		print ("min_x : %10.10f"%(V_min))
		print ("Bulk Modulo:")
		print ("[eV/A^3] %10.10f"%(B_eva))
		print ("[Pa    ] %10.10f"%(B_pa ))
		print ("[GPa   ] %10.10f"%(B_gpa))
		print ("=========================")
	return V_min , B_gpa , coef_2


