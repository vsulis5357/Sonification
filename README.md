# Sonification of Muon Images
This is an extension to the Astronify* software (https://astronify.readthedocs.io/en/latest/) to allow the sonification of a spatially distributed dataset. In particular, this code was developed as a master project from Durham University to sonify muon images from the VERITAS Array. 

Below you can find an example of how the two parts of the program work: the first one reproduces any image into a scatterplot, the second takes this new array and converts it into an audible map.

*Copyright (c) 2020, Clara Brasseur, Scott Fleming, Jennifer Kotler, Kate Meredith All rights reserved.

Hubble Deep Field Reproduced with Scatterplot
![scatterplot](https://user-images.githubusercontent.com/124456367/219119184-79512fcf-3a87-433d-a4b8-f44fa02bfb0a.png)

Sonogram of a Sonified Muon Image 
![scatterplot](https://user-images.githubusercontent.com/124456367/219119146-1c6934f1-8680-4a2f-98e5-94b563e82737.png)








ABOUT THIS REPOSITORY 


You can read more about the scientific work carried out through this repository on https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4891458#paper-references-widget or my linkedIn https://www.linkedin.com/in/valentina-s-0627a9242/


This repository contains scripts for converting images into scatterplots and sonifications. The files are split into:

- reproduce_image.py: A Python file that reproduces an image as a scatterplot.
- sonifications.py: A Python file that takes scatterplot data and creates a sonification series.

Reproduce Image Script
  The reproduce_image.py script takes an image file and reproduces it as a scatterplot. The script does the following:

  - Converts the input image to grayscale.
  - Extracts pixel values and generates scatter data based on these values.
  - Plots the scatter data to create a visual representation of the image.

Sonifications Script
  The sonifications.py script creates the data sonification itself. This script does the following:

  - Converts the scatterplot data into an audio series.
  - Allows for adjusting note spacing and sonification range to customize the auditory representation.

These are independent scripts.

To run the scripts, use the following commands:
- python reproduce_image.py
- python sonifications.py

The repository also contains two sample images. The accepted image format is either .png or .jpeg.
Depending on the size of the picture the processing time can be quite long. 
Please change the processing parameters to suit your needs. 


The noise threshold (in def generate_scatter_data(gray_pixels, threshold=35)) is currently set to 35. It a higher value will result in less image noise and higher processing times but potentially some data loss. 








WHAT ARE SONIFICATIONS?

  All sciences are by nature highly visual. In Maths, Physics, Biology, right from primary education, we are taught to plot graphs to represent information. This approach is undoubtedly effective but excludes the possibility to use our natural capabilities to their full extent. Naturally, one question arises: is it possible to do research using different sensory abilities?
In this project, we explore communication using sound, using a data display method called sonification.

  Sonification is the process of converting numerical data – such as the incoming light from a star, the transit of an exoplanet, etc. – into sounds, effectively replacing a visual graph with an auditory chart that conveys the same information.
These sounds are not already existing in nature, they are a construct used for communication only, just like visual representation but using a different sense.

WHY USE SOUND?

There are several factors that make sound a worthy opponent for traditional data display methods:

  Distinguish particular streams in complex waves:
  
Think about being on a busy street in a big city. It is very crowded, therefore you are subject to a variety of different sounds coming from anywhere around you. Despite the huge amount of information you can decide to listen to all of these sounds together or focus on the drilling from the construction site across the street, on the businessman talking on the phone about the stock market, or even on the lazy buzzing of a bee in the flower shop you are about to walk into.
The ability to isolate particular streams in complex soundwaves is a unique characteristic of this sense, which can be very useful in science to discern hidden patterns in traditionally visually crowded datasets.

  Sensitivity to rapid changes:
  
Sound is much more suitable to detect rapid information variations than sight. In fact, where sight can detect changes lasting milliseconds, our auditory system can detect them even if they are only a few microseconds long. This means that when highly variable information is being displayed, it is possible to hear information that cannot be processed by our eyes.

  A wider field of perception:

Our eyes are limited in their field of perception, allowing us to process information from an area around 190 degrees wide. Our ears, however, do not have that restriction. They are able to perceive information from anywhere as long as the sound source is not too far away from the listener. Future sonifications could take full advantage of this by creating 3D sound charts, which provide information about the position and direction of the data points considered.

  Effects on memory:

It has been shown that the use of images and sounds simultaneously has a positive effect on memory. Using both data displays can help us understand information better and retain them for a longer period of time.

  Inclusivity:
  
Finally, the most important reason for exploring alternative ways of displaying information and doing data analysis is inclusivity. All sciences represent data using traditional visualization tools, making it extremely challenging for visually impaired individuals to approach research. Using audio can open the doors to a world of opportunities through which to cultivate their interests.



![](https://komarev.com/ghpvc/?username=your-github-username)
