from skimage import io
from scipy import misc
import imageio
# from libtiff import TIFF
# import gdal
# from osgeo import gdal
import cv2

label = './dataset/aerialimage/val/label/val_0.tif'


# img = imageio.imread(label)
# img = readTiff(label)
img = cv2.imread(label)
# img = TIFF.open(label, mode='r')
print(img.shape, type(img))