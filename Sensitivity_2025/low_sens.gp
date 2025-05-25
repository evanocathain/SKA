# Plot lambda^2/2 for reference
f(x)=256.0*512.0*(300.0/x)**2/2.0            # x is frequency in MHz

set ylabel "A_{eff} (m^2)"
set xlabel "Frequency (MHz)"
set key spacing 2
plot [45:355][:700000]"SKA_Low_L1v12_Aeff_derived" u 1:2 title "SKA specifications", "AAVS2_database_snippet_zen0_Freq_Pol_Aeff" u 1:(512*$3) title "AAVS2", f(x) title "512 x 256 x {/Symbol l}^2/2"

set term postscript enhanced color solid
set output "Low_Aeff.ps"
replot

set term postscript enhanced color solid
set output "Low_K_Jy.ps"
set ylabel "Gain (K/Jy)"
plot [45:355][:300]"SKA_Low_L1v12_Aeff_derived" u 1:($2/(2*1380)) title "SKA specifications", "AAVS2_database_snippet_zen0_Freq_Pol_Aeff" u 1:(512*$3/(2*1380)) title "AAVS2", f(x)/(2.0*1380.0) title "(512 x 256 x {/Symbol l}^2/2)/(2 x k_{B})"

