set term x11 font 'Times, 10'

# constants, functions etc.
pi      = 3.14159
Tsky(x) = 25.2*(0.408/x)**2.75   # x = freq in GHz

fullska(x) = 1.0e+6/(30.0+Tsky(x))

# Plot properties
set key bottom right box
unset key
set ylabel "190-MHz PSR Survey Speed FoM (arb. units)" font 'Times, 20'
set xlabel "Distance from array centre (m)" font 'Times, 20'
set logscale xy
set xrange [20:4000]
set yrange [1000:2.0e7]
set grid mxtics mytics #lt -1 lc rgb 'gray90'
set grid xtics ytics #lt -1 lc rgb 'gray70'
set xtics font "Times, 20"
set ytics font "Times, 20"

# Plot the non-SKA components
plot "<awk '{print $0,sqrt($3*$3+$4*$4)}' ../Configuration_2024/LOW_dist_metres.txt | sort -g -k5 | awk -v g=0.0 -v lowgain=424.7 '{g+=lowgain; fov=1.0/(20.0*20.0); if (500/($5*$5) < fov) fov=500/($5*$5); print $5,g*g*fov}'" w li lt -1, \
"<awk '{print $0,sqrt($3*$3+$4*$4)}' ../Configuration_2024/LOW_AAstar_dist_metres.txt | sort -g -k5 | awk -v g=0.0 -v lowgain=424.7 '{g+=lowgain; fov=1.0/(20.0*20.0); if (500/($5*$5) < fov) fov=500/($5*$5); print $5,g*g*fov}'" w li lt -1,


set arrow from 0.830,91 to 0.860,91 nohead lt 8 front

# Label the non-SKA single dish components

# Label the SKA-Mid components
set label "SKA1-Low AA4" front at 1000,8000000 #font "Times, 20"
set label "SKA1-Low AA*" front at 400,1200000 #font "Times, 20"
replot

set term postscript enhanced color solid font 'Times, 20'
set output "ss_low.ps
replot
