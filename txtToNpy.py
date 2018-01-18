
import numpy as np

#  LOAD TXT AND SAVE AS NPY
data = np.loadtxt("labels.txt", delimiter=",")

bigNpy = []
for i in range(0, 1200):
    thisLabel1 = str(data[i][0])
    thisLabel2 = str(data[i][1])
    thisLabel3 = str(data[i][2])

    bigNpy.append(thisLabel)

    a =4

np.save("labelsNpy.npy", bigNpy)


# # LOAD NPY FIRST
# aa = np.load("labelsNpy.npy")
# ab = aa[0]
#
#
# a = 4