from src.hyperspectral_imaging import get_hyperspectral_image
import os
import matplotlib.pyplot as plt
import numpy as np

import scipy.stats as sts

white_directory= '../Data/Xylene_Diluted_PDMS/white_light'
image_directory = '../Data/Xylene_Diluted_PDMS/image'

white_files = os.listdir(white_directory)
print(white_files)

wavelengths = np.arange(810,940.5,0.5)
print(wavelengths)
image = get_hyperspectral_image('xylene_diluted_pdms_hyperspectral.npy',image_directory)



wave = np.linspace(498.6174,1103.161,3648)
raw_background = os.path.join(white_directory, white_files[0])
white_water = os.path.join(white_directory,white_files[-1])
fig, ax = plt.subplots()
fig2, ax2 = plt.subplots()
wavelength,mirror = np.genfromtxt(raw_background,unpack=True, delimiter=',')
wavelength,grating_water = np.genfromtxt(white_water, unpack=True, delimiter=',')

normalised_grating_reflectance = np.divide(grating_water,mirror)
ax.plot(wave,normalised_grating_reflectance)
ax.set_xlim([500,1000])
ax.set_ylim([0,1])

colorbar = ax2.imshow(wavelengths[image], cmap='hot', interpolation='nearest')
cbar = fig2.colorbar(colorbar)

half_maximum = (0.79 - 0.3)
ax.set_ylabel('Reflectance')
ax.set_xlabel('Wavelength (nm)')

qfactor = 843.75/(848 - 840)
print('QFactor: ' + str(qfactor))
mean_resonance = np.mean(wavelengths[image])
std_resonance = np.std(wavelengths[image])

print('Mean Resonance: ' + str(mean_resonance))
print('Std Resonance: ' + str(std_resonance))



plt.show()