# Assignment 1
In this Assignment we have to open and image. do several operations on that image, display the different images after each operation while saving them individually and as a plot.
This is the Source Image
<div class="image-container">
  <img src="Assignment 1/210113L_SrcImage.jpg" width="400" alt="Source Image" />
</div>

Opening the Image
```python
SrcImage = cv2.imread("210113L_SrcImage.jpg")
```

## 1. Unprocessed Grayscale Image (Grid 1,1)
<div class="image-container">
  <img src="Assignment 1/210113L_OPImage_1x1.jpg" width="400" alt="Source Image" />
</div>



**Explanation:** 
Converting a color image to grayscale involves averaging or applying a weighted sum of the red, green, and blue (RGB) channels to obtain the intensity value for each pixel.

```python
#The Operation can be done in python as follows
height = len(SrcImage)
width = len(SrcImage[0])
grey_image = [[0 for _ in range(width)] for _ in range(height)]

for i in range(height):
    for j in range(width):
        R = SrcImage[i][j][0]
        G = SrcImage[i][j][1]
        B = SrcImage[i][j][2]
        grey_value = int(0.2989 * R + 0.5870 * G + 0.1140 * B)
        grey_image[i][j] = grey_value

# Using Numpy
grey_image = np.dot(SrcImage[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)

# Using OpenCV
grey_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)
```

## 2. Negative Image (Grid 1,2)
<div class="image-container">
  <img src="Assignment 1/210113L_OPImage_1x2.jpg" width="400" alt="Source Image" />
</div>

**Explanation:**
To create a negative image, the intensity values of each pixel are inverted. This transformation inverts the grayscale values, making light areas dark and vice versa.
```python
# Python Only
height = len(grey_image)
width = len(grey_image[0])
negative_image = [[255 - grey_image[i][j] for j in range(width)] for i in range(height)]

# Numpy
negative_image = 255 - grey_image

# OpenCV
negative_image = cv2.bitwise_not(grey_image)

```
## 3. Increased Brightness by 20% (Grid 1,3)
<div class="image-container">
  <img src="Assignment 1/210113L_OPImage_1x3.jpg" width="400" alt="Source Image" />
</div>
**Explanation:**
To increase the brightness of an image, a percentage of the pixel intensity is added to each pixel value. Here, each pixel's value is increased by 20%, and the result is clamped to stay within the valid range of 0 to 255.

```python
# Python
brightness_increase = 0.2 * 255
height = len(grey_image)
width = len(grey_image[0])
bright_image = [[min(255, grey_image[i][j] + brightness_increase) for j in range(width)] for i in range(height)]

# Numpy
bright_image = grey_image + 0.2 * 255
bright_image = np.clip(bright_image, 0, 255).astype(np.uint8)

# OpenCV
bright_image = cv2.convertScaleAbs(grey_image, alpha=1, beta=0.2 * 255)
```

## 4. Reduced Contrast (Grid 2,1)
<div class="image-container">
  <img src="Assignment 1/210113L_OPImage_2x1.jpg" width="400" alt="Source Image" />
</div>

**Explanation:**
Reducing contrast compresses the range of pixel values into a specified range. Here, the gray levels are adjusted to be between 125 and 175, reducing the dynamic range.

```python
# Reduced contrast
normalized_image = grey_image / 255.0
# Scale the normalized values to the range 125-175
low_contrast_image = (normalized_image * 50) + 125
# Convert the scaled values back to 8-bit format
low_contrast_image = np.clip(low_contrast_image, 125, 175).astype(np.uint8)

```

## 5. Reduced Gray Level Depth to 4bpp (Grid 2,2)
<div class="image-container">
  <img src="Assignment 1/210113L_OPImage_2x2.jpg" width="400" alt="Source Image" />
</div>

**Explanation:**
Reducing the gray level depth from 8 bpp to 4 bpp involves quantizing the intensity levels into fewer distinct values, which groups similar pixel values together.
```python
reduced_depth_image = (grey_image >> 4)*16

```

## 6. Vertical Mirror Image (Grid 2,3)
<div class="image-container">
  <img src="Assignment 1/210113L_OPImage_2x3.jpg" width="400" alt="Source Image" />
</div>


**Explanation:**
The vertical mirror operation flips the image along the horizontal axis, producing a reflection of the original image as if viewed in a mirror placed vertically.
```python
flipped_image = grey_image[:, ::-1]

```


