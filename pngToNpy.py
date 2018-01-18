import glob
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt


## CONVERT IMAGES IN FOLDER TO NPY ARRAYS
# open('imagesAs_npy', 'wb')
# for filename in os.listdir('imagesConv'):
   # sameName = filename[:-3] #this removes the fileEnding
   # # os.rename('imagedata/' + , '')
   #
   # img = cv2.imread('imagedata/' + filename)
   #
   # data = np.array(img, dtype='uint8')
   # np.save('imagesConv/' + sameName + 'npy', data)
   # print(filename)

   # dataArray = np.load(filename)
   # print(dataArray)



# # #CONVERT NPY FOLDER TO ONE BIG NPY FILE https://stackoverflow.com/questions/42160582/append-multiple-numpy-files-to-one-big-numpy-file-in-python
# os.chdir("imagesConv")
# npfiles= glob.glob("*.npy")
# bigNpy = []
# for npfile in glob.glob("*.npy"):
#    print(npfile)
#    thisNpy = np.load(npfile)
#    bigNpy.append(thisNpy)
#
# np.save("bigNpyFile", bigNpy)



# # LOAD AND SAVE 1 NPY IMAGE ***************************************88888***
# thisNpy = np.load("imagesConv/train_0001.npy")
# print(thisNpy)
# np.save("testP", thisNpy)


# #IMSHOW 1 NPY IMAGE *********************************************8
# img_array = np.load('imagesConv/train_0001.npy')
# plt.imshow(img_array, cmap='gray')
# plt.show()


# # EXTRACT FIRST NPY FROM BIG NPY **********************************************8
# bigNpy = np.load('imagesConv/bigNpyFile.npy')
# oneImg = bigNpy[0]
# plt.imshow(oneImg, cmap='gray')
# plt.show(











