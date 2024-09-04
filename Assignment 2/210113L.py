import cv2
import numpy as np
# Filter A
filter_a = np.array([
    [0, -1, -1, -1, 0],
    [-1, 2, 2, 2, -1],
    [-1, 2, 8, 2, -1],
    [-1, 2, 2, 2, -1],
    [0, -1, -1, -1, 0]
])
# Filter B
filter_b = np.array([
    [1, 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, 36, 24, 6],
    [4, 16, 24, 16, 4],
    [1, 4, 6, 4, 1]
])
# Filter C
filter_c = np.array([
    [5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5]
])
# Filter D
filter_d = np.array([
    [0, -1, -1, -1, 0],
    [-1, 2, 2, 2, -1],
    [-1, 2, 16, 2, -1],
    [-1, 2, 2, 2, -1],
    [0, -1, -1, -1, 0]
])

def convert_to_grayscale(image):
    height = len(image)
    width = len(image[0])
    grey_image = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            R = image[i][j][0]
            G = image[i][j][1]
            B = image[i][j][2]
            grey_value = int(0.2989 * R + 0.5870 * G + 0.1140 * B)
            grey_image[i][j] = grey_value
    return np.array(grey_image)

def enhance_contrast(image):
    # Ensure the image is in grayscale
    if len(image.shape) != 2:
        raise ValueError("Input image should be a grayscale image represented by a 2D array.")
    # Find the minimum and maximum pixel values
    min_pixel = image.min()
    max_pixel = image.max()
    # Perform linear contrast stretching
    stretched_image = 255 * (image - min_pixel) / (max_pixel - min_pixel)
    stretched_image = np.clip(stretched_image, 0, 255).astype(np.uint8)
    return stretched_image

def normalize_filter(matrix_filter):
    """Normalize the filter matrix."""
    filter_sum = np.sum(matrix_filter)
    if filter_sum == 0:
        return matrix_filter
    return [[value / filter_sum for value in row] for row in matrix_filter]

def apply_filter(image, filter_):
    # Ensure the image and filter are numpy arrays
    image = np.array(image, dtype=np.float64)
    filter_ = np.array(filter_, dtype=np.float64)
    # Get the dimensions of the image and filter
    image_height, image_width = image.shape
    filter_height, filter_width = filter_.shape
    # Pad the image to handle edges
    pad_height = filter_height // 2
    pad_width = filter_width // 2
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)
    # Create an empty array to hold the filtered image
    filtered_image = np.zeros_like(image)
    # Perform convolution
    for i in range(image_height):
        for j in range(image_width):
            # Extract the region of interest
            region = padded_image[i:i + filter_height, j:j + filter_width]
            # Apply the filter
            filtered_image[i, j] = np.sum(region * filter_)
    # Clip the filtered image values to be in the valid range [0, 255]
    filtered_image = np.clip(filtered_image, 0, 255)
    # Calculate the RMS difference
    rms_difference = np.sqrt(np.mean((image - filtered_image) ** 2))
    return filtered_image, rms_difference
# Load the image

try:
    SrcImage = cv2.imread("road13.png")
except:
    print('Image not found')
    exit()
grey_image = convert_to_grayscale(SrcImage)
enhanced_image = enhance_contrast(grey_image)
cv2.imwrite('original.jpg', enhanced_image)
image_a,rms_diff_a = apply_filter(enhanced_image, filter_a)
cv2.imwrite('filter_a.jpg', image_a)
filter_b_normalized = normalize_filter(filter_b)
image_b,rms_diff_b = apply_filter(enhanced_image, filter_b_normalized)
cv2.imwrite('filter_b.jpg', image_b)
filter_c_normalized = normalize_filter(filter_c)
image_c,rms_diff_c = apply_filter(enhanced_image, filter_c_normalized)
cv2.imwrite('filter_c.jpg', image_c)
image_d,rms_diff_d = apply_filter(enhanced_image, filter_d)
cv2.imwrite('filter_d.jpg', image_d)
print("Filter A =>", rms_diff_a)
print("Filter B =>", rms_diff_b)
print("Filter C =>", rms_diff_c)
print("Filter D =>", rms_diff_d)