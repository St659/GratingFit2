from src.hyperspectral_imaging import get_hyperspectral_image
import matplotlib.pyplot as plt
import numpy as np

water_directory = '../Data/NanoImpITO_Hyperspec/image'
ipa_directory = '../Data/NanoImpITO_IPA_Hyperspec/image'

fig, (ax,ax2) = plt.subplots(1, 2)

wavelengths = np.arange(840, 910.5, 0.5)

water_image = get_hyperspectral_image('sputtered_ito_water_hyperspec.npy',water_directory)
ipa_image = get_hyperspectral_image('sputtered_ito_ipa_hyperspec.npy',ipa_directory)

ax.imshow(wavelengths[water_image], cmap='hot', interpolation='nearest')
ax2.imshow(wavelengths[ipa_image],cmap='hot', interpolation='nearest')

plt.show()