import numpy as np
import os
import matplotlib.pyplot as plt
from src.GratingDataCollector import grating_fit
from scipy import optimize as sci
from scipy import stats as stat
from src.GratingDataCollector import chunker
from natsort import natsorted

directory= '/Users/st659/Google Drive/dep_man_2'
plt.style.use('seaborn-white')
files = os.listdir(directory)
print(files)



raw_background = os.path.join(directory, files[-1])
print(raw_background)
fig, (ax,ax2) = plt.subplots(1,2)
files.remove('background.csv')




background = np.genfromtxt(raw_background, unpack=True, delimiter=',')
print(background)
wave = np.linspace(498.6174,1103.161,len(background))
fit_initial = [0.5, 10, 4, 850, 0.14]


print(files)
peak = list()
current_time = 0
peak_wavelength = list()
time = list()
print("Sorted")
print(natsorted(files,key= lambda y: y.lower())[2000:])
for file in natsorted(files,key= lambda y: y.lower())[2500:]:
    fit_initial = [0.5, 10, 4, 850, 0.5235924622541]
    print(file)
    ri_data = os.path.join(directory,file)
    reflectance= np.genfromtxt(ri_data, unpack=True, delimiter=',')
    wave_min = np.argmax(wave >800)
    wave_max = np.argmax(wave > 900)

    result_obtained = False
    while not result_obtained:
        try:
            a = sci.curve_fit(grating_fit,wave[wave_min:wave_max], reflectance[wave_min:wave_max], p0 =fit_initial)

            if a[0][3] > 830:
                peak_wavelength.append(a[0][3])
                ax.plot(wave[wave_min:wave_max],reflectance[wave_min:wave_max])
                result_obtained = True

        except RuntimeError:
            print("fit failed increase starting wavelength")
            fit_initial[3] += 1

    time.append(current_time)
    current_time +=2
    #normalised_reflectance = np.divide(reflectance,background)
    #wave_normalised = wave[wave_min:wave_max]
    #peak.append(wave_normalised[detect_peaks.detect_peaks(reflectance[wave_min:wave_max], mph=0.1, mpd = 1000)[0]])


wavelength_mean = list()
wavelength_std = list()
time_mean = list()
for values, times in zip(chunker(peak_wavelength, 1), chunker(time, 1)):
    wavelength_mean.append(np.mean(values, axis=0))
    wavelength_std.append(stat.sem(values, axis=0))
    time_mean.append(float(times[0])/60)

ax2.plot(time_mean,wavelength_mean,'o')
print(peak)



ax.set_ylabel('Reflectance')
ax.set_xlabel('Wavelength (nm)')
ax2.set_ylabel('Peak Wavelength')


plt.show()