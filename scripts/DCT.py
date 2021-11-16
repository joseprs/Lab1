

from scipy.fftpack import dct, idct
from skimage.io import imread
from skimage.color import rgb2gray

im = rgb2gray(imread('images/Lenna.png'))
im_dct = dct(dct(im.T, norm='ortho').T, norm='ortho')
print(im_dct)