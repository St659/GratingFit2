import os
import numpy as np
import fnmatch
import matplotlib.pyplot as plt

def get_hyperspectral_image(result_file, data_directory):
    working_directory = os.getcwd()
    results = os.path.join('../Results', result_file)

    try:
        max_values = np.load(results)
    except OSError:
        data_directory_path = os.path.join(working_directory, data_directory)

        data_list = list()
        for file in os.listdir(data_directory):
            if fnmatch.fnmatch(file, '*.csv'):
                print(file)
                data_list.append(np.genfromtxt(os.path.join(data_directory, file), delimiter=','))

        data = np.asarray(data_list)
        max_values = np.argmax(data, axis=0)
        np.save(results, max_values)

    return max_values


def plot_spectra(data_directory, wavelength, ax):

    for file in os.listdir(data_directory):
        if fnmatch.fnmatch(file, '*.csv'):
            data = np.genfromtxt(os.path.join(data_directory, file), delimiter=',')
            ax.plot(data)
    return ax


if __name__ == "__main__":
    fig, (ax,ax2) = plt.subplots(1,2)
    fig2, ax3 = plt.subplots()


    water_directory = '../Data/image_3_hyperspectral/image'
    ethanol_directory = '../Data/image_3_ethanol/image'
    post_anneal_directory = '../Data/PostAnneal_notoptimised/image'

    water_hyperspectral = get_hyperspectral_image('image_3_hyperspectral.npy',water_directory)
    ethanol_hyperspectral = get_hyperspectral_image('image_3_ethanol.npy',ethanol_directory)
    post_anneal = get_hyperspectral_image('post_anneal_not_optimised.npy', post_anneal_directory)


    wavelengths = np.arange(830, 940.5, 0.5)
    post_anneal_wavelengths = np.arange(830,920.5,0.5)
    spectra_plot = plot_spectra('../Data/image_3_hyperspectral/spectra', wavelengths, ax3)
    colorbar = ax.imshow(wavelengths[water_hyperspectral],interpolation='nearest', cmap ='hot')
    ax2.imshow(wavelengths[ethanol_hyperspectral], interpolation='nearest', cmap='hot')
    ax3.imshow(post_anneal_wavelengths[post_anneal],interpolation='nearest', cmap='hot')

    cbar = fig.colorbar(colorbar)

    plt.show()


