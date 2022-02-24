from skimage import io
from scipy import misc
import imageio
# from libtiff import TIFF
# import gdal
# from osgeo import gdal
import cv2

label = 'dataset/CD_Data_GZ/labels_change/P_GZ_test1_2013_2018.png'


# img = imageio.imread(label)
# img = readTiff(label)
img = cv2.imread(label, cv2.IMREAD_GRAYSCALE)
# img = TIFF.open(label, mode='r')
print(img.shape, type(img))