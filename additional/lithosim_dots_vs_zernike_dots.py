import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

img1_path = '/content/lithosim/t1_0_mask_ress.png'
img2_path = '/content/lithosim/output/refine_litho_out/t1_0_mask.png'

if not os.path.exists(img1_path):
    raise FileNotFoundError(f"Файл {img1_path} не найден!")
if not os.path.exists(img2_path):
    raise FileNotFoundError(f"Файл {img2_path} не найден!")

img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

if img1 is None:
    raise ValueError(f"Не удалось загрузить изображение {img1_path}!")
if img2 is None:
    raise ValueError(f"Не удалось загрузить изображение {img2_path}!")

diff = cv2.absdiff(img1, img2)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img1, cmap='gray', vmin=0, vmax=255)
plt.title('Исходная маска')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(img2, cmap='gray', vmin=0, vmax=255)
plt.title('Симулированная маска')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(diff, cmap='gray', vmin=0, vmax=255)
plt.title('Разность масок')
plt.axis('off')

plt.tight_layout()
plt.show()

output_dir = '/content/sample_data'
os.makedirs(output_dir, exist_ok=True)
cv2.imwrite(f'{output_dir}/diff_results_zernike.png', diff)
print(f"Разность сохранена в {output_dir}/diff_results_zernike.png")
