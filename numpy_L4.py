import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

''' ---Saving and Loading Files--- '''


array1 = np.array([1,2,3,4,5])
array2 = np.random.rand(3,3)
array3 = np.zeros((4,4))

np.save('array1.npy', array1)
np.save('array2.npy', array2)
np.save('array3.npy', array3)
# It will save the array in files 
# we can perform operation on those files

loaded_array1 = np.load('array1.npy')
print(loaded_array1)
# [1 2 3 4 5]


'''  ------Converting Image into Npy format------  '''


img = Image.open("numpylogo.jpg")
print(type(img))
print(img)

# summarize some details about the image
print(img.format)
print(img.size)
print(img.mode)

img_array = np.array(img)
print(img_array.shape)

np.save('numpylogo.npy', img_array)




''' --- Loading an Image and performing operations on it --- '''

try:
    logo = np.load('numpylogo.npy', allow_pickle=True) #Loads a saved NumPy array from the file numpylogo.npy.
    #allow_pickle=True allows loading objects saved using Python pickling (used when saving complex objects).
   
   
    #Display
    plt.figure(figsize=(5,5)) # Creates a new figure for plotting using Matplotlib.
                              # figsize=(5,5) sets the size of the figure window to 5 inches by 5 inches.


    plt.subplot(121) # Creates a subplot layout with 1 row and 2 columns, and activates the 1st subplot (i.e., left side).
                     # Syntax: plt.subplot(nrows, ncols, index) → This is equivalent to plt.subplot(1, 2, 1).

    plt.imshow(logo) # Displays the image stored in the logo array.
                     # imshow() is used to show image data in a 2D plot
    plt.title("Numpy Logo")

    plt.grid(False)  # Turns off the gridlines on the plot for a cleaner image display.

    

    dark_logo = 1 - logo # Creates a "dark version" of the logo by inverting the image colors.
                         # Assuming pixel values are in the range [0, 1], subtracting from 1 inverts each pixel's brightness.


    plt.subplot(122)
    plt.imshow(dark_logo)
    plt.title("Numpy Dark Logo")
    plt.grid(False)
    plt.show()

    # this will show same image in 2 different colour



except FileNotFoundError:
    print("numpy logo file not found")