#!/bin/csh

# This script takes the L1v12 Aeff/Tsys requirement and backs out the
# Aeff(freq) using the L1v12 definition of Tsky along with LNA and RX temperature
# contributions of 35 K and 12 K respectively, obtained from the following 
# papers on SKALA4.1 antennas
#

# Bolli et al. (2020), "Test-Driven Design of an Active Dual-Polarized Log-Periodic Antenna for the Square Kilometre Array"

# Bolli et al. (2022), "Computational electromagnetics for the SKA-Low prototype station AAVS2"

awk -v tsys=1 -v tLNA=35.0 -v tRX=12.0 'NR>1{tsky=(2.73+20.0*(0.408/($1*0.001))^(2.75)+288.0*(0.005+0.1314*exp((log($1*0.001)/log(10)-log(22.23)/log(10))*8.0))); print $1,$2*(tsky+tLNA+tRX)}' SKA_Low_L1v12 > SKA_Low_L1v12_Aeff_derived
