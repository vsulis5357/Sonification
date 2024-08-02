import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from skimage.io import imread
from numpy import asarray
import imageio
import random

def load_image(image_path):
    """
    A simple function to load an image from a given file path and convert it to RGBA.

    Args:
        image_path (str): The path to the image file.
    """
    im = Image.open(image_path)
    im = im.convert("RGBA")
    return im, im.size

def extract_pixels(im, img_width, img_height):
    """
    A simple function to extract pixel values and their positions from an image.

    Args:
        im (PIL.Image.Image): The image from which to extract pixels.
        img_width (int): The width of the image.
        img_height (int): The height of the image.
    """
    img_data = im.getdata()
    x_pos = 0
    y_pos = 1
    pixel_value, x, y = [], [], []

    for item in img_data:
        if x_pos == img_width:
            x_pos = 1
            y_pos += 1
        else:
            x_pos += 1

        if item[3] != 0:  # Check for non-transparent pixels
            pixel_value.append(item[2])
            x.append(x_pos)
            y.append(y_pos)

    return zip(*sorted(zip(pixel_value, x, y), reverse=True))

def convert_to_grayscale(image_path):
    """
    A simple function to convert an image to grayscale.

    Args:
        image_path (str): The path to the image file.
    """
    pic = imageio.imread(image_path)
    gray = np.dot(pic[..., :3], [0.299, 0.587, 0.114])
    return gray

def prepare_gray_pixels(gray, size=300):
    """
    A simple function to prepare grayscale pixels by resizing to a specified size.

    Args:
        gray (np.ndarray): The grayscale image array.
        size (int): The size to which the grayscale image is resized.
    """
    return asarray(gray[:size, :size])


# Change threshold data to reduce image noise (higher threshold). The higher the value the higher the data loss
def generate_scatter_data(gray_pixels, threshold=35):
    """
    A simple function to generate scatter plot data from grayscale pixels.

    Args:
        gray_pixels (np.ndarray): The grayscale pixel array.
        threshold (int): The threshold for pixel intensity.
    """
    h, w = gray_pixels.shape
    h1 = np.arange(h)
    w1 = np.arange(w)
    N = np.array(gray_pixels, dtype=int)
    
    xmin, xmax = h1[:-1], h1[1:]
    ymin, ymax = w1[:-1], w1[1:]
    
    imagex, imagey = [], []
    for i in range(len(xmin)):
        for k in range(len(xmin)):
            if N[i][k] > threshold:
                imagex.append(np.random.uniform(low=xmin[i], high=xmax[i], size=N[i][k]))
                imagey.append(np.random.uniform(low=ymin[k], high=ymax[k], size=N[i][k]))
    
    return np.array(imagex, dtype=object), np.array(imagey, dtype=object)

def plot_images(gray_pixels, imagex, imagey):
    """
    A simple function to plot the scatter plot of the image.

    Args:
        gray_pixels (np.ndarray): The grayscale pixel array.
        imagex (np.ndarray): The x coordinates for the scatter plot.
        imagey (np.ndarray): The y coordinates for the scatter plot.
    """
    plt.figure(figsize=(7, 7))
    for i in range(len(imagex)):
        plt.scatter(imagey[i][:], imagex[i][:], alpha=0.05, s=0.007, c='white')
    
    plt.title('Image reproduced with scatterplot')
    plt.xlabel('X pixels')
    plt.ylabel('Y pixels')
    plt.grid()
    ax = plt.gca()
    ax.set_facecolor('xkcd:black')
    plt.show()

if __name__ == '__main__':
    # Load and extract pixel data from the image - change depending on need
    image_path = "hubble_deep_field.jpg"
    im, (img_width, img_height) = load_image(image_path)
    pixel_value, x, y = extract_pixels(im, img_width, img_height)
    
    # Convert the image to grayscale
    gray = convert_to_grayscale(image_path)
    plt.figure(figsize=(10, 10))
    plt.title('Converted Grayscale Image')
    plt.xlabel('X pixels')
    plt.ylabel('Y pixels')
    plt.imshow(gray, cmap='gray')
    plt.show()
    
    # Prepare grayscale pixels
    gray_pixels = prepare_gray_pixels(gray)
    plt.figure(figsize=(10, 10))
    plt.imshow(gray_pixels, cmap='gray')
    plt.title('Prepared Grayscale Pixels')
    plt.xlabel('X pixels')
    plt.ylabel('Y pixels')
    plt.show()
    
    # Generate scatter plot data and plot the image
    imagex, imagey = generate_scatter_data(gray_pixels)
    plot_images(gray_pixels, imagex, imagey)