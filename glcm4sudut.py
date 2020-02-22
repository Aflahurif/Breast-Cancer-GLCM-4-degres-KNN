from skimage import feature, img_as_ubyte
import os
import pandas as pd
import numpy as np
import cv2

path = '.\\Data Test\\Malignant\\1.bmp'
# path = '.\\Data Test1\\Benign\\b1.png'
class glcm4s(object):
    data = []

    def __init__(self, pict):
        self.pict = pict
        self.data = []

    def glcm(self):
        hasil = {
            "energy": 0,
            "homogeneity": 0,
            "contrast": 0,
            "correlation": 0
        }
        degrees = [0,45,90,135]
        img_read = cv2.imread(self.pict, 0)
        img_conv = img_as_ubyte(img_read)
        for degree in degrees:
            glcm = feature.greycomatrix(img_conv, [1], [degree], symmetric=True, normed=True)
            for prop in hasil.keys():
                self.data.append(float(feature.greycoprops(glcm, prop)))


# pict = []

# for jenis in os.listdir(path):
#     folder = path+jenis
#     for isi in os.listdir(folder):
#         data = []
#         gambar = path+jenis+'\\'+isi
#         img = glcm4s(gambar)
#         img.glcm()
#         if jenis == "Benign":
#             data.append("Benign")
#         elif jenis == "Malignant":
#             data.append("Malignant")
#         pict.append(data)

# print(img.data)
# pd.DataFrame(pict).to_csv('./file.csv', index=False, header=False)


img = glcm4s(path)
img.glcm()
print(img.data)
