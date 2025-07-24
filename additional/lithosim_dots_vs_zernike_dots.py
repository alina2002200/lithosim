import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('/content/t1_0_mask_ress.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('/content/lithosim/output/refine_litho_out/t1_0_mask.png', cv2.IMREAD_GRAYSCALE)

diff = cv2.absdiff(img1, img2)

plt.figure(figsize=(10, 5))
plt.subplot(131), plt.imshow(img1, cmap='gray'), plt.title('Маска 1')
plt.subplot(132), plt.imshow(img2, cmap='gray'), plt.title('Маска 2')
plt.subplot(133), plt.imshow(diff, cmap='gray'), plt.title('Разность')
