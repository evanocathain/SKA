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
from functions import *

h_over_k = 4.8e-11 # Planck's constant divided by Boltzmann's constant in s*K
nfreqs = 2000      # number of points at which to sample frequency for output plots etc.

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

# Get the effective collecting area
Aeff_SKA = get_aeff("SKA")
Aeff_MK  = get_aeff("MeerKAT")

# System Temperature
#get_tsys("SKA")
#get_tsys("MeerKAT")
Tsys_SKA, f = get_tsys("SKA",gal,pwv,zenith)
Tsys_MK, f  = get_tsys("MeerKAT",gal,pwv,zenith)

# Gain - single dish
f = np.logspace(np.log10(0.35),np.log10(50),200)
plt.grid(True)
plt.semilogx(f,Aeff_SKA(f)/Tsys_SKA(f)) #(Trcv(f)+Tspill(f)+Tsky(f)))
plt.semilogx(f,Aeff_MK(f)/Tsys_MK(f)) #(Trcv(f)+Tspill(f)+Tsky(f)))
plt.title("Gain - single Dish")
plt.ylabel("Aeff/Tsys")
plt.xlabel("Frequency (GHz)")
plt.show()

# Gain - user-requested sub-array
# need to read in the configs, for now just do whole array
# 
# Also compare some actually relevant telescopes, maybe a different flag for imaging- and NIP-relevant ones to show
f = np.logspace(np.log10(0.35),np.log10(50),200)
plt.grid(True)
plt.loglog(f,133.0*(Aeff_SKA(f)/Tsys_SKA(f))+64.0*(Aeff_MK(f)/Tsys_MK(f)))
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
