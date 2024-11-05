import numpy as np
import imageio
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

def histogram_equalization(image):
    hist, bins = np.histogram(image.flatten(), bins=256, range=[0,256])
    cdf = hist.cumsum()
    cdf_normalized = cdf / cdf[-1]  
    mapped_values = np.floor(255 * cdf_normalized).astype('uint8')
    equalized_image = mapped_values[image]
    return equalized_image

path = "C:\\Users\\Administrator\\Downloads\\Pemandangan aesthetic.jpg"
image = imageio.imread(path)  
if image.ndim == 3:
    image = image.mean(axis=2).astype(np.uint8)

equalized_image = histogram_equalization(image)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Citra Awal')
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('Citra yang Ditingkatkan')
plt.imshow(equalized_image, cmap='gray')
plt.show()
