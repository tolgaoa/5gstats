import numpy as np
import scipy
import scipy.stats
import matplotlib.pyplot as plt


dataps5ncpu = np.loadtxt("ps5netflixcpu.txt", dtype=float)
dataps5nnet = np.loadtxt("ps5netflixnetw.txt", dtype=float)

for idx, i in enumerate(dataps5nnet):
    if dataps5nnet[idx] <= 5:
        dataps5nnet[idx] = i * 1024

x = np.arange(dataps5ncpu.size)
#-------------------------------------------------------------------------
dataamfcpu = np.loadtxt("statscpuamfp.txt", dtype=float)
dataamfmem = np.loadtxt("statsmemamfp.txt", dtype=float)

x1 = np.arange(dataamfcpu.size)
datasmfcpu = np.loadtxt("statscpusmfp.txt", dtype=float)
datasmfmem = np.loadtxt("statsmemsmfp.txt", dtype=float)

dataupfcpu = np.loadtxt("statscpuupfp.txt", dtype=float)
dataupfmem = np.loadtxt("statsmemupfp.txt", dtype=float)

dataausfcpu = np.loadtxt("statscpuausfp.txt", dtype=float)
dataausfmem = np.loadtxt("statsmemausfp.txt", dtype=float)

dataudmcpu = np.loadtxt("statscpuudmp.txt", dtype=float)
dataudmmem = np.loadtxt("statsmemudmp.txt", dtype=float)

dataudrcpu = np.loadtxt("statscpuudrp.txt", dtype=float)
dataudrmem = np.loadtxt("statsmemudrp.txt", dtype=float)

datanrfcpu = np.loadtxt("statscpunrfp.txt", dtype=float)
datanrfmem = np.loadtxt("statsmemnrfp.txt", dtype=float)

dataupfcpu = np.loadtxt("statscpuupfp.txt", dtype=float)
x2 = np.arange(dataupfcpu.size)
#-------------------------------------------------------------------------
dataps5gcpu = np.loadtxt("ps5gamecpup.txt", dtype=float)
dataps5gnet = np.loadtxt("ps5gamenetwp.txt", dtype=float)

datazoomcpu = np.loadtxt("zoomcpup.txt", dtype=float)
datazoomnet = np.loadtxt("zoomnetwp.txt", dtype=float)

dataoculuscpu = np.loadtxt("oculuscpup.txt", dtype=float)
dataoculusnet = np.loadtxt("oculusnetwp.txt", dtype=float)

datatiktokcpu = np.loadtxt("tiktokcpup.txt", dtype=float)
datatiktoknet = np.loadtxt("tiktoknetwp.txt", dtype=float)

datawhatsappcpu = np.loadtxt("whatsappcpup.txt", dtype=float)
datawhatsappnet = np.loadtxt("whatsappnetwp.txt", dtype=float)

ps5ps5gcpuactarr = np.zeros(shape=(dataps5ncpu.size, 1))
for idx, i in enumerate(dataps5ncpu):
    if dataps5ncpu[idx] > 10:
        ps5ps5gcpuactarr[idx] = 1
ps5gcpuact = np.count_nonzero(ps5ps5gcpuactarr)/ps5ps5gcpuactarr.size

print(np.mean(dataps5gcpu))
print(np.max(dataps5gcpu))
print(np.min(dataps5gcpu))

print(np.mean(dataps5ncpu))
print(np.max(dataps5ncpu))
print(np.min(dataps5ncpu))

print(np.mean(datazoomcpu))
print(np.max(datazoomcpu))
print(np.min(datazoomcpu))

print(np.mean(dataoculuscpu))
print(np.max(dataoculuscpu))
print(np.min(dataoculuscpu))

print(np.mean(datatiktokcpu))
print(np.max(datatiktokcpu))
print(np.min(datatiktokcpu))


print(np.mean(datawhatsappcpu))
print(np.max(datawhatsappcpu))
print(np.min(datawhatsappcpu))
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
ticksize = 35
fz = 35
ms = 10
plt.rc('xtick', labelsize=ticksize)
plt.rc('ytick', labelsize=ticksize)
lw = 5
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
fig1, ax1 = plt.subplots(figsize=(10,10))
ax2 = ax1.twinx()

ax1.plot(x,dataps5ncpu, 'r')
ax2.plot(x,dataps5nnet, 'k', linewidth=lw)

ax1.set_xlabel("Time (s)", fontsize=30)
ax1.set_ylabel("CPU utilization (%)", color="red", fontsize=fz)
ax1.tick_params(axis="y", labelcolor="red")

ax2.set_ylabel("Network I/O (MB)", color="black", fontsize=fz)
ax2.tick_params(axis="y", labelcolor="black")

ax1.grid()
ax2.grid()
plt.tight_layout()
plt.savefig('ps5ncpunetio.eps', format='eps')
plt.savefig('ps5ncpunetio.png')

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
fig2, ax3 = plt.subplots(figsize=(10,10))
ax4 = ax3.twinx()

ax3.plot(x,dataps5gcpu, 'r')
ax4.plot(x,dataps5gnet, 'k', linewidth=lw)

ax3.set_xlabel("Time (s)", fontsize=fz)
ax3.set_ylabel("CPU utilization (%)", color="red", fontsize=fz)
ax3.tick_params(axis="y", labelcolor="red")

ax4.set_ylabel("Network I/O (MB)", color="black", fontsize=fz)
ax4.tick_params(axis="y", labelcolor="black")

ax3.grid()
ax4.grid()
plt.tight_layout()
plt.savefig('ps5gcpunetio.eps', format='eps')
plt.savefig('ps5gcpunetio.png')
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
fig3, ax5 = plt.subplots(figsize=(10,10))
ax6 = ax5.twinx()

ax5.plot(x,datazoomcpu, 'r')
ax6.plot(x,datazoomnet, 'k', linewidth=lw)

ax5.set_xlabel("Time (s)", fontsize=fz)
ax5.set_ylabel("CPU utilization (%)", color="red", fontsize=fz)
ax5.tick_params(axis="y", labelcolor="red")

ax6.set_ylabel("Network I/O (MB)", color="black", fontsize=fz)
ax6.tick_params(axis="y", labelcolor="black")

ax5.grid()
ax6.grid()
plt.tight_layout()
plt.savefig('zoomcpunetio.eps', format='eps')
plt.savefig('zoomcpunetio.png')
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
fig4, ax7 = plt.subplots(figsize=(10,10))
ax8 = ax7.twinx()

ax7.plot(x,dataoculuscpu, 'r')
ax8.plot(x,dataoculusnet, 'k', linewidth=lw)

ax7.set_xlabel("Time (s)", fontsize=fz)
ax7.set_ylabel("CPU utilization (%)", color="red", fontsize=fz)
ax7.tick_params(axis="y", labelcolor="red")

ax8.set_ylabel("Network I/O (MB)", color="black", fontsize=fz)
ax8.tick_params(axis="y", labelcolor="black")

ax7.grid()
ax8.grid()
plt.tight_layout()
plt.savefig('oculuscpunetio.eps', format='eps')
plt.savefig('oculuscpunetio.png')
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
fig5, ax9 = plt.subplots(figsize=(10,10))
ax10 = ax9.twinx()

ax9.plot(x,datatiktokcpu, 'r')
ax10.plot(x,datatiktoknet, 'k', linewidth=lw)

ax9.set_xlabel("Time (s)", fontsize=fz)
ax9.set_ylabel("CPU utilization (%)", color="red", fontsize=fz)
ax9.tick_params(axis="y", labelcolor="red")

ax10.set_ylabel("Network I/O (MB)", color="black", fontsize=fz)
ax10.tick_params(axis="y", labelcolor="black")

ax9.grid()
ax10.grid()
plt.tight_layout()
plt.savefig('tiktokcpunetio.eps', format='eps')
plt.savefig('tiktokcpunetio.png')
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
fig6, ax11 = plt.subplots(figsize=(10,10))
ax12 = ax11.twinx()

ax11.plot(x,datawhatsappcpu, 'r')
ax12.plot(x,datawhatsappnet, 'k', linewidth=lw)

ax11.set_xlabel("Time (s)", fontsize=fz)
ax11.set_ylabel("CPU utilization (%)", color="red", fontsize=fz)
ax11.tick_params(axis="y", labelcolor="red")

ax12.set_ylabel("Network I/O (MB)", color="black", fontsize=fz)
ax12.tick_params(axis="y", labelcolor="black")

ax11.grid()
ax12.grid()
plt.tight_layout()
plt.savefig('whatsappcpunetio.eps', format='eps')
plt.savefig('whatsappcpunetio.png')



#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
plt.figure(figsize=(5, 5), dpi=80)
plt.xlabel('Time (sec)', fontsize='20')
plt.ylabel('CPU Utilization (%)', fontsize='20')
plt.plot(x,dataps5ncpu, 'r')
plt.grid()
plt.tight_layout()
plt.savefig('cpuutil.eps', format='eps')
plt.savefig('cpuutil.png')


plt.figure(figsize=(5, 5), dpi=80)
plt.xlabel('Time (sec)', fontsize='20')
plt.ylabel('Network (I/O)', fontsize='20')
plt.plot(x,dataps5nnet, 'g')
plt.grid()
plt.tight_layout()
plt.savefig('dataio.eps', format='eps')
plt.savefig('dataio.png')
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
b=15
count, bins_count = np.histogram(dataps5ncpu, bins=b)
pdf = count / sum(count)
cdfps5n = np.cumsum(pdf)

count, bins_count = np.histogram(dataps5gcpu, bins=b)
pdf = count / sum(count)
cdfps5g = np.cumsum(pdf)

count, bins_count = np.histogram(datazoomcpu, bins=b)
pdf = count / sum(count)
cdfzoom = np.cumsum(pdf)

count, bins_count = np.histogram(dataoculuscpu, bins=b)
pdf = count / sum(count)
cdfoculus = np.cumsum(pdf)

count, bins_count = np.histogram(datatiktokcpu, bins=b)
pdf = count / sum(count)
cdftiktok = np.cumsum(pdf)

count, bins_count = np.histogram(datawhatsappcpu, bins=b)
pdf = count / sum(count)
cdfwhatsapp = np.cumsum(pdf)

plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)

plt.figure(figsize=(6, 6))
plt.xlabel('CPU Utilization (%)', fontsize=fz-15)
plt.ylabel('', fontsize=fz-15)
plt.grid()
plt.plot(bins_count[1:], cdfps5n, color='green', marker='o', markersize=ms, linestyle='dashed', linewidth=2, label="PS5 Streaming - Netflix")
plt.plot(bins_count[1:], cdfps5g, color='blue', marker='x', markersize=ms, linestyle='dashed', linewidth=2, label="PS5 Gaming - Fortnite")
plt.plot(bins_count[1:], cdfzoom, color='red', marker='^', markersize=ms, linestyle='dashed', linewidth=2, label="VoIP - Zoom Video")
plt.plot(bins_count[1:], cdfoculus, color='magenta', marker='.', markersize=ms, linestyle='dashed', linewidth=2, label="Oculus - Horizon Venues")
plt.plot(bins_count[1:], cdftiktok, color='cyan', marker='+', markersize=ms, linestyle='dashed', linewidth=2, label="Social Media -- Tiktok")
plt.plot(bins_count[1:], cdfwhatsapp, color='black', marker='>', markersize=ms, linestyle='dashed', linewidth=2, label="VoIP -- WhatsApp Voice")

plt.tight_layout()
plt.legend(fontsize=15)
plt.savefig('cpuactcdf.eps', format='eps')
plt.savefig('cpuactcdf.png')


fz=45
lz=3
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
fig20, ax201 = plt.subplots(figsize=(10,10))
ax202 = ax201.twinx()

ax201.plot(x1,dataamfcpu, 'r', linewidth=lw)
ax202.plot(x1,dataamfmem, 'g', linewidth=lw)

ax201.set_xlabel("Time (s)", fontsize=30)
ax201.set_ylabel("CPU utilization (%)", color="red", fontsize=fz)
ax201.tick_params(axis="y", labelcolor="red")

ax202.set_ylabel("Memory Used (MiB)", color="green", fontsize=fz)
ax202.tick_params(axis="y", labelcolor="green")

ax201.grid()
ax202.grid()
plt.tight_layout()
plt.savefig('cpuutilamf.eps', format='eps')
plt.savefig('cpuutilamf.png')

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
fig21, ax211 = plt.subplots(figsize=(10,10))
ax212 = ax211.twinx()

ax211.plot(x1,datasmfcpu, 'r', linewidth=lw)
ax212.plot(x1,datasmfmem, 'g', linewidth=lw)

ax211.set_xlabel("Time (s)", fontsize=30)
ax211.set_ylabel("CPU utilization (%)", color="red", fontsize=fz)
ax211.tick_params(axis="y", labelcolor="red")

ax212.set_ylabel("Memory Used (MiB)", color="green", fontsize=fz)
ax212.tick_params(axis="y", labelcolor="green")

ax211.grid()
ax212.grid()
plt.tight_layout()
plt.savefig('cpuutilsmf.eps', format='eps')
plt.savefig('cpuutilsmf.png')
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
fig22, ax221 = plt.subplots(figsize=(10,10))
ax222 = ax221.twinx()

ax221.plot(x1,dataausfcpu, 'r', linewidth=lw)
ax222.plot(x1,dataausfmem, 'g', linewidth=lw)

ax221.set_xlabel("Time (s)", fontsize=30)
ax221.set_ylabel("CPU utilization (%)", color="red", fontsize=fz)
ax221.tick_params(axis="y", labelcolor="red")

ax222.set_ylabel("Memory Used (MiB)", color="green", fontsize=fz)
ax222.tick_params(axis="y", labelcolor="green")

ax221.grid()
ax222.grid()
plt.tight_layout()
plt.savefig('cpuutilausf.eps', format='eps')
plt.savefig('cpuutilausf.png')

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
fig23, ax231 = plt.subplots(figsize=(10,10))
ax232 = ax231.twinx()

ax231.plot(x1,dataudmcpu, 'r', linewidth=lw)
ax232.plot(x1,dataudmmem, 'g', linewidth=lw)

ax231.set_xlabel("Time (s)", fontsize=30)
ax231.set_ylabel("CPU utilization (%)", color="red", fontsize=fz)
ax231.tick_params(axis="y", labelcolor="red")

ax232.set_ylabel("Memory Used (MiB)", color="green", fontsize=fz)
ax232.tick_params(axis="y", labelcolor="green")

ax231.grid()
ax232.grid()
plt.tight_layout()
plt.savefig('cpuutiludm.eps', format='eps')
plt.savefig('cpuutiludm.png')


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
fig24, ax241 = plt.subplots(figsize=(10,10))
ax242 = ax241.twinx()

ax241.plot(x1,datasmfcpu, 'r', linewidth=lw)
ax242.plot(x1,datasmfmem, 'g', linewidth=lw)

ax241.set_xlabel("Time (s)", fontsize=30)
ax241.set_ylabel("CPU utilization (%)", color="red", fontsize=fz)
ax241.tick_params(axis="y", labelcolor="red")

ax242.set_ylabel("Memory Used (MiB)", color="green", fontsize=fz)
ax242.tick_params(axis="y", labelcolor="green")

ax241.grid()
ax242.grid()
plt.tight_layout()
plt.savefig('cpuutiludr.eps', format='eps')
plt.savefig('cpuutiludr.png')


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
fig25, ax251 = plt.subplots(figsize=(10,10))
ax252 = ax251.twinx()

ax251.plot(x1,datanrfcpu, 'r', linewidth=lw)
ax252.plot(x1,datanrfmem, 'g', linewidth=lw)

ax251.set_xlabel("Time (s)", fontsize=30)
ax251.set_ylabel("CPU utilization (%)", color="red", fontsize=fz)
ax251.tick_params(axis="y", labelcolor="red")

ax252.set_ylabel("Memory Used (MiB)", color="green", fontsize=fz)
ax252.tick_params(axis="y", labelcolor="green")

ax251.grid()
ax252.grid()
plt.tight_layout()
plt.savefig('cpuutilnrf.eps', format='eps')
plt.savefig('cpuutilnrf.png')

plt.figure(figsize=(10, 10), dpi=80)
plt.xlabel('Time (sec)', fontsize='20')
plt.ylabel('CPU Utilization (%)', fontsize='20')
plt.plot(x2,dataupfcpu, 'r')
plt.grid()
plt.tight_layout()
plt.text(7, 1, "P = 1", fontsize=20)
plt.text(25, 5.1, "P = 5", fontsize=20)
plt.text(46, 7.7, "P = 10", fontsize=20)
plt.text(68, 9, "P = 15", fontsize=20)
plt.text(86, 17, "P = 20", fontsize=20)
plt.text(106, 23, "P = 25", fontsize=20)
plt.text(124, 25.5, "P = 30", fontsize=20)

plt.savefig('cpuutilupf.eps', format='eps')
plt.savefig('cpuutilupf.png')

