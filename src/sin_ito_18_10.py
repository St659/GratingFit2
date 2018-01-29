import numpy as np
import os
import matplotlib.pyplot as plt
import numpy as np
from peakdetect import detect_peaks

def normalise_data_to_mirror(mirror, data_list, directory):
    wave, background = np.genfromtxt(os.path.join(directory, mirror), unpack=True, delimiter=',')
    normalised_data_list = list()
    for file in data_list:
        wave, reflectance = np.genfromtxt(os.path.join(directory, file), unpack=True, delimiter=',')
        normalised_reflectance = np.divide(reflectance,background)
        normalised_data_list.append(normalised_reflectance)
    return normalised_data_list



directory= '/Users/st659/Google Drive/ito_sin_18_10_17/photonics'
plt.style.use('seaborn-white')
files = os.listdir(directory)
print(files)



mirrors = [files[0], files[1]]
pre_ito = [files[3], files[5]]
post_ito = [files[2], files[4]]



wave = np.linspace(498.6174,1103.161,3648)
fig, (te_plot,tm_plot) = plt.subplots(1,2, sharey=True)
fig2,tm_only = plt.subplots()

print(files)

print(pre_ito)
normalised_pre_ito = normalise_data_to_mirror(mirrors[0], pre_ito, directory)
normalised_post_ito = normalise_data_to_mirror(mirrors[1], post_ito, directory)

for data in [normalised_pre_ito, normalised_post_ito]:
    te_plot.plot(wave, data[0])
    tm_plot.plot(wave, data[1])
    tm_only.plot(wave, data[1])




te_plot.set_ylabel('Normalised Reflectance')
tm_plot.set_xlabel('Wavelength (nm)')
te_plot.set_xlabel('Wavelength (nm)')

tm_only.set_xlabel('Wavelength (nm)')
tm_only.set_ylabel('Normalised Reflectance')
tm_only.set_xlim([750,900])
tm_only.legend(['Pre ITO', 'Post ITO'])
tm_only.set_ylim([0,1])

te_plot.set_ylim([0,1])
te_plot.set_xlim([700,900])
tm_plot.set_xlim([700,900])
te_plot.legend(['Pre ITO', 'Post ITO'])


plt.show()