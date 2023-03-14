import numpy as np
import scipy
import scipy.stats
import matplotlib.pyplot as plt

datacpu = np.loadtxt("cpu.txt", dtype=float)
datanet = np.loadtxt("netw.txt", dtype=float)

cpuactarr = np.zeros(shape=(datacpu.size, 1))


for idx, x in enumerate(datacpu):
    if datacpu[idx] > 4:
        cpuactarr[idx] = 1

cpuact = np.count_nonzero(cpuactarr)/cpuactarr.size
print(cpuact)


for idx, x in enumerate(datanet):
    if datanet[idx] <= 5:
        datanet[idx] = x * 1024

x = np.arange(datacpu.size)


ticksize = 25
plt.rc('xtick', labelsize=ticksize)
plt.rc('ytick', labelsize=ticksize)

fig, ax1 = plt.subplots(figsize=(10,10))
ax2 = ax1.twinx()

ax1.plot(x,datacpu, 'r')
ax2.plot(x,datanet, 'b')

ax1.set_xlabel("Time (s)", fontsize=30)
ax1.set_ylabel("CPU utilization (%)", color="red", fontsize=30)
ax1.tick_params(axis="y", labelcolor="red")

ax2.set_ylabel("Network (I/O)", color="blue", fontsize=30)
ax2.tick_params(axis="y", labelcolor="blue")

ax1.grid()
ax2.grid()
plt.tight_layout()
plt.savefig('cpunetio.eps', format='eps')
plt.savefig('cpunetio.png')

plt.figure(figsize=(5, 5), dpi=80)
plt.xlabel('Time (sec)', fontsize='20')
plt.ylabel('CPU Utilization (%)', fontsize='20')
plt.plot(x,datacpu, 'r')
plt.grid()
plt.tight_layout()
plt.savefig('cpuutil.eps', format='eps')
plt.savefig('cpuutil.png')


plt.figure(figsize=(5, 5), dpi=80)
plt.xlabel('Time (sec)', fontsize='20')
plt.ylabel('Network (I/O)', fontsize='20')
plt.plot(x,datanet, 'g')
plt.grid()
plt.tight_layout()
plt.savefig('dataio.eps', format='eps')
plt.savefig('dataio.png')


plt.figure(figsize=(10, 10), dpi=80)
count, bins_count = np.histogram(datacpu, bins=10)
pdf = count / sum(count)
cdf = np.cumsum(pdf)
plt.xlabel('CPU Utilization (%)', fontsize='30')
plt.ylabel('CDF', fontsize='30')
plt.grid()
plt.plot(bins_count[1:], cdf, color='green', marker='o', linestyle='dashed',
     linewidth=2, label="PS5 Netflix stream")
plt.legend(fontsize=30)
plt.savefig('cpuactcdf.eps', format='eps')
plt.savefig('cpuactcdf.png')
