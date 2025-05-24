# Evan Keane
# 08/05/2017
# 24/05/2025 - updated for updated configs and to show AA* and AA4
#
# A very simple gnuplot script to plot the cumulative number 
# of dishes/stations, collecting area etc. for SKA1 Mid and Low.

# Plot formatting
set key top left box
set logscale x
set mxtics 10
set mytics 2
set grid
set grid mxtics
set grid mytics

# MID
set ylabel "Number of dishes"
set xlabel "Distance from array centre (km)"
plot "< awk '{print 0.001*sqrt($3*$3+$4*$4)|\"sort -g -k1\"}' MID_dist_metres.txt | cat -n" u 2:1 wi li title "SKA1-Mid AA4"
replot "< awk '{print 0.001*sqrt($3*$3+$4*$4)|\"sort -g -k1\"}' MID_AAstar_dist_metres.txt | cat -n" u 2:1 wi li title "SKA1-Mid AA*"
replot "< awk '{if (substr($2,0,1)==\"M\") print 0.001*sqrt($3*$3+$4*$4)|\"sort -g -k1\"}' MID_dist_metres.txt | cat -n" u 2:1 wi li title "MeerKAT"
#replot "< awk '{if (substr($2,0,1)==\"S\") print 0.001*sqrt($3*$3+$4*$4)|\"sort -g -k1\"}' MID_dist_metres.txt | cat -n" u 2:1 wi li title "SKA1 Dishes"

set terminal postscript enhanced color solid
set output "Mid_dishes_vs_radius.ps"
replot
pause mouse

# LOW
set term x11
set ylabel "Number of stations"
set xlabel "Distance from array centre (km)"
plot "< awk '{print 0.001*sqrt($3*$3+$4*$4)|\"sort -g -k1\"}' LOW_dist_metres.txt | cat -n" u 2:1 wi li title "SKA1-Low AA4"
replot "< awk '{print 0.001*sqrt($3*$3+$4*$4)|\"sort -g -k1\"}' LOW_AAstar_dist_metres.txt | cat -n" u 2:1 wi li title "SKA1-Low AA*"

set terminal postscript enhanced color solid
set output "Low_stations_vs_radius.ps"
replot
