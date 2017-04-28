#!/bin/csh

# pi*radius of earth = 20 037.3921 kilometers
set degtokm = `echo 20037.3921 180.0 | awk '{print $1/$2}'`
#echo $degtokm
awk -v fac=$degtokm 'NR==2{clong=$3;clat=$4}''NR>2{print $1,$2,cos(clat*3.14159/180.0)*($3-clong)*1000*fac,($4-clat)*1000*fac}' coords_LOW.txt > LOW_dist_metres.txt
awk -v fac=$degtokm 'NR==2{clong=$3;clat=$4}''NR>2{print $1,$2,cos(clat*3.14159/180.0)*($3-clong)*1000*fac,($4-clat)*1000*fac}' coords_MID.txt > MID_dist_metres.txt
