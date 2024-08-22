import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
try:
    SrcImage = cv2.imread("210113L_SrcImage.jpg")
    grey_image = np.dot(SrcImage[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
except:
    print('Image not found')
    exit()

# Create a 3x2 subplot
fig, axs = plt.subplots(2, 3, figsize=(12,8))

# Display the unprocessed grayscale image
axs[0, 0].imshow(grey_image, cmap='gray',vmin=0,vmax=255)
axs[0, 0].set_title('1x1 - Unprocessed Grayscale')
cv2.imwrite('210113L_OPImage_1x1.jpg', grey_image)
axs[0, 0].set_visible(True)

# Negative image
negative_image = 255 - grey_image
axs[0, 1].imshow(negative_image, cmap='gray',vmin=0,vmax=255)
axs[0, 1].set_title('1x2 - Negative Image')
cv2.imwrite('210113L_OPImage_1x2.jpg', negative_image)
axs[0, 1].set_visible(True)

# Increased brightness
bright_image = grey_image + 0.2 * 255
bright_image = np.clip(bright_image, 0, 255).astype(np.uint8)
axs[0, 2].imshow(bright_image,cmap='gray',vmin=0,vmax=255)
axs[0, 2].set_title('1x3 - Increased Brightness')
cv2.imwrite('210113L_OPImage_1x3.jpg', bright_image)
axs[0, 2].set_visible(True)

# Reduced contrast
normalized_image = grey_image / 255.0
# Scale the normalized values to the range 125-175
low_contrast_image = (normalized_image * 50) + 125
# Convert the scaled values back to 8-bit format
low_contrast_image = np.clip(low_contrast_image, 125, 175).astype(np.uint8)
axs[1, 0].imshow(low_contrast_image,cmap='gray',vmin=0,vmax=255)
axs[1, 0].set_title('2x1 - Reduced Contrast')
cv2.imwrite('210113L_OPImage_2x1.jpg', low_contrast_image)
axs[1, 0].set_visible(True)

# Reduced gray level depth
reduced_depth_image = (grey_image >> 4)*16
axs[1, 1].imshow(reduced_depth_image,cmap='gray',vmin=0,vmax=255)
axs[1, 1].set_title('2x2 - Reduced Gray Level Depth')
cv2.imwrite('210113L_OPImage_2x2.jpg', reduced_depth_image )
axs[1, 1].set_visible(True)
 
# Vertical mirror image
flipped_image = grey_image[:, ::-1]
axs[1, 2].imshow(flipped_image,cmap='gray',vmin=0,vmax=255)
axs[1, 2].set_title('2x3 - Vertical Mirror Image')
cv2.imwrite('210113L_OPImage_2x3.jpg', flipped_image)
axs[1, 2].set_visible(True)

plt.tight_layout()
plt.savefig('210113L_SubPlot.jpg')
plt.show()