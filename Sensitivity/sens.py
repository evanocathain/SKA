#!/usr/local/bin/python2.7

#
# Author: Evan Keane
# Date: 27/09/2017
# Description: Determines SKA sensitivity curves etc. for various 
#              user-defined input configurations
#
# TODO
# 1. tidy up, add opacity, zenith angle and temp transforms etc.
# 2. read in array configuration CSV files
# 3. read in Haslam map for specific and average gl,gb values and ranges
# 4. add a check that the zenith angle is possible for the given sky coords!
#

# Load some useful packages
import argparse
import sys
import math as m
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-radius', type=float, dest='radius', help='choose distance from the array centre, in km, for chosen sub-array (default: entire array)', default=150.0)
parser.add_argument('-glgb', nargs=2, type=float, dest='coord', help='enter specific Galactic coordinates to use (default: gl=180.0, gb=-90.0)', default=[180.0,-90.0])
parser.add_argument('-gallos', dest='gal', help='choose either 10th, 50th or 90th percentile value for the galaxy contribution to the sky temperature (low/medium/high, default: low)', default='low')
parser.add_argument('-pwv', dest='pwv', help='choose either 5mm, 10mm or 20mm for the PWV value for choosing (a) the zenith opacity, and (b) the atmospheric temperature contribution to the sky temperature (low/medium/high, default: low)', default="low")
parser.add_argument('-tel', dest='tel', help='choose telescope (SKA or MeerKAT, default: SKA)', default="SKA")
parser.add_argument('-nelements', type=int, dest='nelements', help='choose the inner nelements elements (default: entire array)', default=197)
#parser.add_argument('-pwv', type=float, dest='pwv', help='choose a precipitable water vapo(u)r value in mm (default: 5.0)', default=5.0)
parser.add_argument('-zenith', type=float, dest='zenith', help='choose a zenith angle in degrees (default: 0.0)', default=0.0)
parser.add_argument('--version', action='version', version='%(prog)s 0.0.1')
args = parser.parse_args()

# Set values from command line inputs
tel = args.tel
gl = args.coord[0]
gb = args.coord[1]
gal = args.gal
zenith = args.zenith
pwv = args.pwv
radius = args.radius
nelements = args.nelements

# Some basic stuff - could do this better with astropy!
speedoflight = 3.0e+8 # m/s 
wavelength = lambda freqGHz: 1.0e-9*speedoflight/freqGHz
h_over_k = 4.8e-11 # Planck's constant divided by Boltzmann's constant in s*K
nfreqs = 2000      # number of points at which to sample frequency for output plots etc.

if tel == "SKA":
    D = 15.0 # dish diameter in metres
    etaF  = lambda freqGHz: 0.92 - 0.04*np.abs(np.log10(freqGHz)) # feed illumination
    epsp  = 280.0e-6 # rms surface error in metres for the primary reflector surface
    epss  = 154.0e-6 # rms surface error in metres for the secondary reflector surface
    Ap    = 0.89     # unitless constant
    As    = 0.98     # unitless constant

if tel == "MeerKAT":
    D     = 13.5 # dish diameter in metres
    etaF  = lambda freqGHz: 0.80 - 0.04*np.abs(np.log10(freqGHz)) # feed illumination
    epsp = 480.0e-6 # rms surface error in metres for the primary reflector surface
    epss = 265.0e-6 # rms surface error in metres for the primary reflector surface
    Ap   = 0.89     #?? # unitless constant
    As   = 0.98     #?? # unitless constant

# Aperture efficiency
delta   = 2*(Ap*epsp*epsp + As*epss*epss)**0.5
DeltaPh = lambda freqGHz: 2*m.pi*delta/wavelength(freqGHz)
etaPh = lambda freqGHz: np.exp(-(DeltaPh(freqGHz))**2.0) # NB the square is missing in Robert's document
etaD  = lambda freqGHz: 1.0 - 20.0*(wavelength(freqGHz)/D)**(1.5)
etaA  = lambda freqGHz: etaF(freqGHz)*etaPh(freqGHz)*etaD(freqGHz)   # Aperture efficiency

freq = np.logspace(np.log10(0.35), np.log10(50.0), 200)
plt.figure()
plt.grid(True)
plt.title("Aperture efficiency - SKA1 dish")
plt.ylabel("Aperture efficiency")
plt.xlabel("Frequency (GHz)")
plt.semilogx(freq, etaA(freq), 'o')
plt.show()

# Collecting Area
Aphys = m.pi*D*D/4.0      # Physical collecting area
Aeff  = lambda freqGHz: Aphys*etaA(freqGHz)        # Effective collecting area

# System Temperature

# Receiver Temperature
Trcv = lambda freqGHz: (11.5 + 65*(freqGHz - 0.65)**2)*(np.heaviside((freqGHz-0.35),1.0)-np.heaviside((freqGHz-0.95),0.0)) + (7.5)*(np.heaviside((freqGHz-0.95),0.0)-np.heaviside((freqGHz-4.6),0.0)) + (4.4 + 0.69*freqGHz)* (np.heaviside((freqGHz-4.6),0.0)-np.heaviside((freqGHz-50.0),0.0))

# Spillover Temperature
Tspill = lambda freqGHz: 3.0 + freqGHz*0.0 # assumed to be this for all Bands but (a) is frequency dependent; (b) is zenith angle dependent - 3 K is thought to be appropriate for zenith < 45 deg; (c) the frequency dependence would actually be such that this should actually be a bit worse for Band 1 as it is not an octave feed.

# Sky Temperature
## Tgal
## At the minute can only do 10th, 50th and 90the percentile values for Tgal 
## Need to add any line of sight
## For now this is fine as it allows a direct comparison with Robert's calculations
if (gal == "low"):
    T408 = 17.1
elif (gal == "medium"):
    T408 = 25.2
elif (gal == "high"):
    T408 = 54.8
Tgal = lambda freqGHz: T408*(0.408/(freqGHz))**(2.75) # an off-plane approximation, need to do this more generally
## Tcmb
Tcmb = 2.73
## Tatm
freq_array = np.genfromtxt("SKA_Tatm.txt", usecols=0)
if (pwv == "low"):
    Tatm_array = np.genfromtxt("SKA_Tatm.txt", usecols=1)
elif (pwv == "medium"):
    Tatm_array = np.genfromtxt("SKA_Tatm.txt", usecols=2)
elif (pwv == "high"):
    Tatm_array = np.genfromtxt("SKA_Tatm.txt", usecols=2)
Tatm = interp1d(freq_array, Tatm_array, kind='cubic')
Tsky = lambda freqGHz: Tgal(freqGHz) + Tcmb + Tatm(freqGHz)
### Opacity
if (pwv == "low"):
    tau_array = np.genfromtxt("SKA_tau.txt", usecols=1)
elif (pwv == "medium"):
    tau_array = np.genfromtxt("SKA_tau.txt", usecols=2)
elif (pwv == "high"):
    tau_array = np.genfromtxt("SKA_tau.txt", usecols=2)
tau = interp1d(freq_array, tau_array, kind='cubic')

#tau      = 0.01    # just eye-balled a reasonable value until I have the full function
Tx = lambda freqGHz, temp: (((h_over_k*freqGHz*1.0e9)/(temp))/(np.exp((h_over_k*freqGHz*1.0e9)/(temp)) - 1.0 ))*temp*np.exp(tau(freqGHz)*zenith*m.pi/180.0)

Tsys = lambda f: Tx(f,(Trcv(f)+Tspill(f)+Tsky(f)))

f = np.logspace(np.log10(0.35),np.log10(50),nfreqs)
plt.grid(True)
plt.semilogx(f,Trcv(f),label='Receiver Temp.')
plt.semilogx(f,Tspill(f),label='Spillover Temp.')
plt.semilogx(f,Tsky(f),label='Sky Temp. (Gal+CMB+Atm)')
plt.semilogx(f,Tsys(f),label='Tsys')
plt.title("Temperature contributions")
plt.ylabel("Temperature (K)")
plt.xlabel("Frequency (GHz)")
plt.legend()
plt.show()

# Gain - single dish
f = np.logspace(np.log10(0.35),np.log10(50),200)
plt.grid(True)
plt.semilogx(f,Aeff(f)/(Trcv(f)+Tspill(f)+Tsky(f)))
plt.title("Gain - single SKA1-Mid Dish")
plt.ylabel("Aeff/Tsys")
plt.xlabel("Frequency (GHz)")
plt.show()

# Gain - user-requested sub-array
# need to read in the configs, for now just do whole array
# 
# Also compare some actually relevant telescopes, maybe a different flag for imaging- and NIP-relevant ones to show
f = np.logspace(np.log10(0.35),np.log10(50),200)
plt.grid(True)
plt.semilogx(f,133.0*Aeff(f)/(Trcv(f)+Tspill(f)+Tsky(f)))
plt.title("Gain - entire SKA1-Mid array (133 SKA1 + 64 MeerKAT)")
plt.ylabel("Aeff/Tsys")
plt.xlabel("Frequency (GHz)")
plt.show()

# Gain - sub-array size of choice
# work out config for radius of choice
# plot appropriately scaled gain curves
sys.exit()

# MeerKAT dish
#Trcv = 12 K                               # UHF band
#     = 6.5 + 6.8*|(nu/GHz) - 1.65|**1.5 K # L band
#     = 9 + (nu/GHz) K                     # S band
#Tspill = 5 K # again this should be zenith and frequency dependent
