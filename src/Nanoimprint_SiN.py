import numpy as np
import os
import matplotlib.pyplot as plt
import numpy as np
from peakdetect import detect_peaks

directory = '/Users/st659/Google Drive/Nanoimprint/3rd Attempt'

plt.style.use('seaborn-white')
files = os.listdir(directory)
print(files)



raw_background = os.path.join(directory, files[0])
file = os.path.join(directory, files[1])
fig, ax = plt.subplots()
files.remove('background.csv')

ri_data = os.path.join(directory,file)
wave, reflectance= np.genfromtxt(ri_data, unpack=True, delimiter=',')
wave, background = np.genfromtxt(raw_background, unpack=True, delimiter=',')
wave_min = np.argmax(wave >800)
wave_max = np.argmax(wave > 950)
normalised_reflectance = np.divide(reflectance,background)
wave_normalised = wave[wave_min:wave_max]
#peak.append(wave_normalised[detect_peaks.detect_peaks(normalised_reflectance[wave_min:wave_max], mph=1, mpd = 1000)[0]])
ax.plot(wave, normalised_reflectance)


ax.set_ylabel('Reflectance')
ax.set_xlabel('Wavelength (nm)')
ax.set_ylim([0,0.3])
ax.set_xlim([800,900])

plt.show()
