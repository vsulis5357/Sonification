import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from skimage.io import imread
from astropy.table import Table
import random
from numpy import asarray
from astronify.series import SoniSeries

def load_image(image_path):
    """
    A simple function to load an image from a given file path and convert it to RGBA.

    Args:
        image_path (str): The path to the image file.
    """
    image = Image.open(image_path)
    img_width, img_height = image.size
    image = image.convert("RGBA")
    return image, img_width, img_height

def extract_pixels(image, img_width, img_height):
    """
    A simple function to extract pixel values and their positions from an image.

    Args:
        image (PIL.Image.Image): The image from which to extract pixels.
        img_width (int): The width of the image.
        img_height (int): The height of the image.
    """
    img_data = image.getdata()
    x_pos, y_pos = 0, 1
    pixel_values, x, y = [], [], []

    for item in img_data:
        if x_pos == img_width:
            x_pos = 1
            y_pos += 1
        else:
            x_pos += 1

        if item[3] != 0:  # Check for non-transparent pixels
            pixel_values.append(item[2])
            x.append(x_pos)
            y.append(y_pos)

    pixel_values, x, y = zip(*sorted(zip(pixel_values, x, y), reverse=True))
    return pixel_values, x, y

def convert_to_grayscale(image_path):
    """
    A simple function to convert an image to grayscale.

    Args:
        image_path (str): The path to the image file.
    """
    image = imread(image_path)
    gray_image = np.dot(image[..., :3], [0.299, 0.587, 0.114])
    return gray_image

def plot_image(image, cmap='gray'):
    """
    A simple function to plot an image using matplotlib.

    Args:
        image (np.ndarray): The image array to be plotted.
        cmap (str): The color map to be used for plotting.
    """
    plt.figure(figsize=(10, 10))
    plt.title('Grayscale Image')
    plt.xlabel('X pixels')
    plt.ylabel('Y pixels')
    plt.imshow(image, cmap=cmap)


def prepare_scatter_data(gray_pixels):
    """
    A simple function to prepare the scatter data from grayscale pixels.

    Args:
        gray_pixels (np.ndarray): The grayscale pixel array.
    """
    h, w = gray_pixels.shape[0], gray_pixels.shape[1]
    h1 = np.arange(h)
    w1 = np.arange(w)
    return h1, w1

def generate_scatter_data(gray_pixels, h1, w1):
    """
    A simple function to generate scatter plot data from grayscale pixels.

    Args:
        gray_pixels (np.ndarray): The grayscale pixel array.
        h1 (np.ndarray): Array of height values.
        w1 (np.ndarray): Array of width values.
    """
    N = np.array((gray_pixels / 25.0), dtype=int)
    xmin, xmax, ymin, ymax = h1[:-1], h1[1:], w1[:-1], w1[1:]

    imagex, imagey = [], []
    for i in range(len(xmin)):
        for k in range(len(xmin)):
            if N[i][k] > 1:
                imagex.append(np.random.uniform(low=xmin[i], high=xmax[i], size=N[i][k]))
                imagey.append(np.random.uniform(low=ymin[k], high=ymax[k], size=N[i][k]))

    return np.array(imagex, dtype=object), np.array(imagey, dtype=object)

def flatten_data(f, g):
    """
    A simple function to flatten 2D scatter data arrays.

    Args:
        f (list): List of x coordinates.
        g (list): List of y coordinates.
    """
    a = np.zeros([len(f), len(max(f, key=len))])
    for i, j in enumerate(f):
        a[i][0:len(j)] = j

    b = np.zeros([len(g), len(max(g, key=len))])
    for i, j in enumerate(g):
        b[i][0:len(j)] = j

    c = a.flatten()
    d = b.flatten()
    return list(filter(lambda x: x != 0, c)), list(filter(lambda x: x != 0, d))

def plot_scatter(f, g):
    """
    A simple function to plot the scatter plot of the image.

    Args:
        f (np.ndarray): The x coordinates for the scatter plot.
        g (np.ndarray): The y coordinates for the scatter plot.
    """
    plt.figure(figsize=(7, 7))
    for i in range(len(f)):
        plt.scatter(g[i][:], f[i][:], alpha=1, s=0.01, c='white')
    plt.title('Image reproduced with scatterplot')
    plt.xlabel('X pixels')
    plt.ylabel('Y pixels')
    plt.grid()
    ax = plt.gca()
    ax.set_facecolor('xkcd:black')


def create_soni_series(q, w, start, end):
    """
    A simple function to turn scatter point into sound

    Args:
        q (list): List of time values.
        w (list): List of flux values.
        start (int): Start index for slicing the data.
        end (int): End index for slicing the data.
    """
    data_table = Table({"time": q[start:end], "flux": w[start:end]})
    data_soni = SoniSeries(data_table)
    data_soni.note_spacing = 0.0007
    data_soni.sonify()
    return data_soni

if __name__ == '__main__':

    image_path = "hubble_deep_field.jpg"
    
    # Load the image
    image, img_width, img_height = load_image(image_path)
    
    # Extract pixel values and positions
    pixel_values, x, y = extract_pixels(image, img_width, img_height)

    # Convert the image to grayscale
    gray_image = convert_to_grayscale(image_path)
    plot_image(gray_image)


    # Prepare grayscale pixels for scatter plot
    gray_pixels = asarray(gray_image[0:350, 0:350])


    # Generate scatter data from grayscale pixels
    h1, w1 = prepare_scatter_data(gray_pixels)
    imagex, imagey = generate_scatter_data(gray_pixels, h1, w1)


    # Flatten the scatter data for plotting
    q, w = flatten_data(imagex, imagey)

    # Plot the scatter data
    plot_scatter(imagex, imagey)

    # Create and play a SoniSeries from the scatter data
    data_soni = create_soni_series(q, w, 2900, 6000)
    data_soni.play()