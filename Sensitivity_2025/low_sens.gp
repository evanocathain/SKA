# Plot lambda^2/2 for reference
f(x)=256.0*512.0*(300.0/x)**2*(a/(4.0*3.14159))            # x is frequency in MHz
g(x)=256.0*512.0*(300.0/x)**2*(b/(4.0*3.14159))            # x is frequency in MHz

fit [120:]f(x) "SKA_Low_L1v12_Aeff_derived" u 1:2 via a
print a

fit [120:]g(x) "AAVS2_database_snippet_zen0_Freq_Pol_Aeff" u 1:(512.0*$2) via b
print b

set ylabel "A_{eff} (m^2)"
set xlabel "Frequency (MHz)"
set key spacing 2
plot [45:355][:900000]"SKA_Low_L1v12_Aeff_derived" u 1:2 title "SKA specifications", "AAVS2_database_snippet_zen0_Freq_Pol_Aeff" u 1:(512*$2) title "AAVS2", f(x) title "{/Symbol l}^2, G=8.8", g(x) title "{/Symbol l}^2, G=5.3"

set term postscript enhanced color solid
set output "Low_Aeff.ps"
replot

set term postscript enhanced color solid
set output "Low_K_Jy.ps"
set ylabel "Gain (K/Jy)"
plot [45:355][:400]"SKA_Low_L1v12_Aeff_derived" u 1:($2/(2*1380)) title "SKA specifications", "AAVS2_database_snippet_zen0_Freq_Pol_Aeff" u 1:(512*$2/(2*1380)) title "AAVS2", f(x)/(2.0*1380.0) title "{/Symbol l}^2, G=8.8", g(x)/(2.0*1380) title "{/Symbol l}^2, G=5.3"

