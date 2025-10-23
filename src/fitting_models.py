"""
Created on Mon Jan 29 15:34:44 2024

@author: Edouard Quérel
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def TLMZ_cc (L,A,w, ri,qct,nct,Rcc,Qcc,ncc):
    #All TLM expressions are derived from Siroma et al. Electrochimica Acta 2015, https://doi.org/10.1016/j.electacta.2015.02.065 
    #Ztotal expressed in [Ohms] - needs area normalization compared to publication Siroma
    #A current collector contact impedance Zcc is added in series to the TLMZ expression
    za=ri #effective resistivity of electrolyte in Ohm cm
    zb=1/(qct*(1j*w)**nct)
    alpha=np.sqrt((za)/zb)*L
    Zcc= Rcc/(1 + Rcc * Qcc * (1j * w) ** ncc) #expressed in Ohms
    Ztotal= Zcc+A**(-1)*(
                np.sqrt(za*zb)*np.cosh(alpha)/np.sinh(alpha)
                ) 
    return Ztotal

def R0_TLMZ_cc_fit (L,A,w, ri,qct,nct,Rcc,Qcc,ncc,R0):
    Ztot= R0+2*TLMZ_cc(L,A,w, ri,qct,nct,Rcc,Qcc,ncc)   # adds series resistance R0
    return np.hstack((np.real(Ztot), np.imag(Ztot)))   # for curve_fit
