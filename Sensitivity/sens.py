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
#

# Load some useful packages
import argparse
import sys
import math as m
import numpy as np
import matplotlib.pyplot as plt

# Parse command line arguments
parser = argparse.ArgumentParser()
#parser.add_argument('-i', dest='input_file', help='set the input file name (default: file)', default="file")
#parser.add_argument('-p1', type=float, dest='p1', help='set the lowest period (default: 0.1 seconds)', default=0.100)
parser.add_argument('-radius', type=float, dest='radius', help='choose distance from the array centre, in km, for chosen sub-array (default: entire array)', default=150.0)
parser.add_argument('-glgb', nargs=2, type=float, dest='coord', help='enter specific Galactic coordinates to use (default: gl=180.0, gb=-90.0)', default=[180.0,-90.0])
parser.add_argument('-tel', dest='tel', help='choose telescope (SKA or MeerKAT, default: SKA)', default="SKA")
#parser.add_argument('-update', dest='update', help='update to current FRBCAT sources (default: false)', action="store_true",default=False)
parser.add_argument('--version', action='version', version='%(prog)s 0.0.1')
args = parser.parse_args()

tel = args.tel
gl = args.coord[0]
gb = args.coord[1]

speedoflight = 3.0e+8 # m/s - need to do this properly with astropy
wavelength = lambda freqGHz: 1.0e-9*speedoflight/freqGHz # need to do this properly with astropy

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

delta   = 2*(Ap*epsp*epsp + As*epss*epss)**0.5
DeltaPh = lambda freqGHz: 2*m.pi*delta/wavelength(freqGHz)
etaPh = lambda freqGHz: np.exp(-(DeltaPh(freqGHz))**2.0) # NB the square is missing in Robert's document
etaD  = lambda freqGHz: 1.0 - 20.0*(wavelength(freqGHz)/D)**(1.5)

# Collecting Area
Aphys = m.pi*D*D/4.0      # Physical collecting area
etaA  = lambda freqGHz: etaF(freqGHz)*etaPh(freqGHz)*etaD(freqGHz)   # Aperture efficiency
Aeff  = lambda freqGHz: Aphys*etaA(freqGHz)        # Effective collecting area

## Print out a few things to check values
#print "freqGHz etaPh etaD etaF etaA Aphys Aeff"
#for i in range(1,10):
#    f = i*1.0
#    print i, etaPh(f), etaD(f), etaF(f), etaA(f), Aphys, Aeff(i*1.0)
#f = 0.7
#print f, etaPh(f), etaD(f), etaF(f), etaA(f), Aphys, Aeff(i*1.0)
#f = 1.4
#print f, etaPh(f), etaD(f), etaF(f), etaA(f), Aphys, Aeff(i*1.0)
#f = 2.4
#print f, etaPh(f), etaD(f), etaF(f), etaA(f), Aphys, Aeff(i*1.0)
#f = 4.0
#print f, etaPh(f), etaD(f), etaF(f), etaA(f), Aphys, Aeff(i*1.0)
#f = 6.6
#print f, etaPh(f), etaD(f), etaF(f), etaA(f), Aphys, Aeff(i*1.0)
#f = 12.0
#print f, etaPh(f), etaD(f), etaF(f), etaA(f), Aphys, Aeff(i*1.0)
#f = 18.0
#print f, etaPh(f), etaD(f), etaF(f), etaA(f), Aphys, Aeff(i*1.0)

# Plot eta as a func of freq
#freq = np.linspace(0.35, 50.0, 200)
freq = np.logspace(np.log10(0.35), np.log10(50.0), 200) # Makes more space to plot in log10(frequency)
plt.figure()
#plt.subplot(111, projection="aitoff")
plt.title("Various stuff")
plt.ylabel("Aperture efficiency")
plt.xlabel("Frequency (GHz)")
#plt.grid(True)
plt.semilogx(freq, etaA(freq), 'o')
#plt.plot(freq,etaA(freq))
plt.show()

# System Temperature

# System Temperature
#Tsys = x(Trcv + Tspill + Tsky)*exp(tau*sec(zenith)) # function of freq and zenith angle
# x(T) = ((h*nu)/(k*T))/(exp(h*nu/k*T)-1)
#tau  = ?
#     = 0.005 # eye-ball this off Robert's plot, this is obviously frequency dependent. Add proper function when I get the vals

Trcv = lambda freqGHz: (11.5 + 65*(freqGHz - 0.65)**2)*(np.heaviside((freqGHz-0.35),1.0)-np.heaviside((freqGHz-0.95),0.0)) + (7.5)*(np.heaviside((freqGHz-0.95),0.0)-np.heaviside((freqGHz-4.6),0.0)) + (4.4 + 0.69*freqGHz)* (np.heaviside((freqGHz-4.6),0.0)-np.heaviside((freqGHz-50.0),0.0))
f = np.logspace(np.log10(0.35),np.log10(50),200)
plt.semilogx(f,Trcv(f))
plt.title("Various stuff")
plt.ylabel("Receiver Temperature")
plt.xlabel("Frequency (GHz)")
#for i in range(0,3,100):
#    f = i*1.0
#    print i,Trcv(f)
plt.show()

Tspill = 3.0 # assumed to be this for all Bands but (a) is frequency dependent; (b) is zenith angle dependent - 3 K is thought to be appropriate for zenith < 45 deg; (c) the frequency dependence would actually be such that this should actually be a bit worse for Band 1 as it is not an octave feed.
Tsky = 1.0
T408 = 17.1
Tgal = lambda freqGHz: T408*(0.408/(freqGHz))**(2.75) # an off-plane approximation, best 10% line-of-sight
Tcmb = 2.73
Tatm = 1.0 # need to add the correct freq dependence
Tsky = lambda freqGHz: Tgal(freqGHz) + Tcmb + Tatm

# Gain - single dish
f = np.logspace(np.log10(0.35),np.log10(50),200)
plt.semilogx(f,Aeff(f)/(Trcv(f)+Tspill+Tsky(f)))
plt.title("Various stuff")
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

# Common
#Tsky = Tgal*exp(-tau*sec(zenith)) + Tcmb*exp(-tau*sec(zenith)) + Tatm
# Tgal = ?     # This is actually gl and gb dependent, and basically taken from the Haslam map scaled by the Press et al. spectral index. 
#  Tgal = T408*(0.408/(nu/GHz))**2.75 K # an off-plane approximation
#   T408 = 17.1 K # 10th percentile
#   T408 = 25.2 K # 50th percentile
#   T408 = 54.8 K # 90th percentile
# Tcmb = 2.73 K
# Tatm = ?
#      = 1 K # assume some value, obviously this is frequency dependent and rises at high freq. Add proper function when I get the vals

# Gain
