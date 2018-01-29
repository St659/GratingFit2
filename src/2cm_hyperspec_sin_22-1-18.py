from src.hyperspectral_imaging import get_hyperspectral_image
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np

pre_photoresist_directory = '../Data/Pre_resist_22_1_18/image'
post_photoresist_directory = '../Data/Nanoimp2cm_22-01-18_postdevelop/image'
post_photoresist_directory_opt1 = '../Data/PostDevelop_7secondexposure_1_30develop/image'
post_photoresist_directory_opt2 = '../Data/PostDevelop_7secondexposure_1_30develop_2/image'


fig, ax = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()

wavelengths = np.arange(850, 920.5, 0.5)

pre_resist_image = get_hyperspectral_image('pre_resist.npy',pre_photoresist_directory)
post_resist_image = get_hyperspectral_image('post_resist.npy',post_photoresist_directory)
post_resist_image_optimised = get_hyperspectral_image('post_resist_opt1.npy', post_photoresist_directory_opt1)
post_resist_image_optimised_2 = get_hyperspectral_image('post_resist_opt2.npy', post_photoresist_directory_opt2)


pre_resist_wavelengths = wavelengths[pre_resist_image]
post_resist_wavelengths = wavelengths[post_resist_image]
post_resist_wavelengths_optimised = wavelengths[post_resist_image_optimised]
post_resist_wavelengths_optimised_2 =  wavelengths[post_resist_image_optimised_2]
colorbar = ax.imshow(pre_resist_wavelengths, cmap='hot', interpolation='nearest')
colorbar2 = ax2.imshow(post_resist_wavelengths,cmap='hot', interpolation='nearest')

colorbar3= ax3.imshow(post_resist_wavelengths_optimised, cmap='hot', interpolation='nearest')
colorbar4=ax4.imshow(post_resist_wavelengths_optimised_2, cmap='hot', interpolation='nearest')
colorbar.set_label('Resonant Wavelength')
cbar = fig.colorbar(colorbar)

cbar2 = fig2.colorbar(colorbar2)
cbar3 = fig3.colorbar(colorbar3)
cbar4 = fig4.colorbar(colorbar4)
cbar.set_label('Resonant Wavelength (nm)')
cbar2.set_label('Resonant Wavelength (nm)')
cbar3.set_label('Resonant Wavelength (nm)')
cbar4.set_label('Resonant Wavelength (nm)')
pre_mean_resonance = np.mean(pre_resist_wavelengths)
pre_std_resonance = np.std(pre_resist_wavelengths)

post_mean_resonance = np.mean(post_resist_wavelengths)
post_std_resonance = np.std(post_resist_wavelengths)

post_mean_opt_resonance = np.mean(post_resist_wavelengths_optimised)
post_std_opt_resonance = np.std(post_resist_wavelengths_optimised)

print('Pre Mean resonance: ' + str(pre_mean_resonance))
print('Pre Std resonance: ' + str(pre_std_resonance))

print('Post Mean resonance: ' + str(post_mean_resonance))
print('Post Std resonance: ' + str(post_std_resonance))

print("Post optimised Mean resonance: " + str(post_mean_opt_resonance))
print('Post optimised Std resonance: ' + str(post_std_opt_resonance))

print(pre_resist_wavelengths.shape)

plt.show()