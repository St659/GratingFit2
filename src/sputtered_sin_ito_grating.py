import os
import numpy as np
import matplotlib.pyplot as plt

directory = '/Users/st659/Google Drive/Nanoimprint/SiN_ITO_1/Photonics/'


fig,ax = plt.subplots()

data_files = os.listdir(directory)[1:]
print(data_files)

background = data_files[0]

tm_file = data_files[5]
tm_eth = data_files[6]
print(tm_file)

wv,back = np.genfromtxt(os.path.join(directory,background),unpack=True, delimiter=',')
wv,reflectance = np.genfromtxt(os.path.join(directory,tm_file),unpack=True,delimiter=',')
wv,reflectance_eth = np.genfromtxt(os.path.join(directory,tm_eth),unpack=True,delimiter=',')
wave = np.linspace(498.6174,1103.161,len(background))
normalised_reflectance = np.divide(reflectance,back)
normalised_eth = np.divide(reflectance_eth,back)

ax.plot(wv, normalised_reflectance)
ax.plot(wv, normalised_eth)
ax.set_xlim([850,920])
ax.set_ylim([0,0.7])
ax.set_xlabel('Wavelength (nm)')
ax.set_ylabel('Normalised Reflectance')
ax.legend(['Water', 'Ethanol'])
qfactor = 882/(887-876)
print('Q Factor: ' + str(qfactor))
plt.show()