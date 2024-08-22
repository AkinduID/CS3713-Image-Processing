# CS3713-Image-Processing
This includes all the source files of Labs given under "Image Processing" module in semester 5 of Computer Science and Engineering Department, University of Moratuwa

# Assignment 1

## 1. Unprocessed Grayscale Image (Grid 1,1)

**Explanation:** 
Converting a color image to grayscale involves averaging or applying a weighted sum of the red, green, and blue (RGB) channels to obtain the intensity value for each pixel.

**Equation:**
\[ I_{gray}(x, y) = 0.299 \cdot R(x, y) + 0.587 \cdot G(x, y) + 0.114 \cdot B(x, y) \]

where:
- \( I_{gray}(x, y) \) is the grayscale intensity at pixel \((x, y)\),
- \( R(x, y) \), \( G(x, y) \), and \( B(x, y) \) are the red, green, and blue intensity values at pixel \((x, y)\), respectively.

## 2. Negative Image (Grid 1,2)

**Explanation:**
To create a negative image, the intensity values of each pixel are inverted. This transformation inverts the grayscale values, making light areas dark and vice versa.

**Equation:**
\[ I_{neg}(x, y) = 255 - I_{gray}(x, y) \]

where:
- \( I_{neg}(x, y) \) is the intensity of the negative image at pixel \((x, y)\),
- \( I_{gray}(x, y) \) is the grayscale intensity of the original image at pixel \((x, y)\).

## 3. Increased Brightness by 20% (Grid 1,3)

**Explanation:**
To increase the brightness of an image, a percentage of the pixel intensity is added to each pixel value. Here, each pixel's value is increased by 20%, and the result is clamped to stay within the valid range of 0 to 255.

**Equation:**
\[ I_{bright}(x, y) = \text{clip}(1.2 \cdot I_{gray}(x, y), 0, 255) \]

where:
- \( I_{bright}(x, y) \) is the intensity of the brightened image at pixel \((x, y)\),
- \( I_{gray}(x, y) \) is the grayscale intensity of the original image at pixel \((x, y)\),
- \(\text{clip}(v, \text{min}, \text{max})\) ensures that the values are constrained between 0 and 255.

## 4. Reduced Contrast (Grid 2,1)

**Explanation:**
Reducing contrast compresses the range of pixel values into a specified range. Here, the gray levels are adjusted to be between 125 and 175, reducing the dynamic range.

**Equation:**
\[ I_{contrast}(x, y) = \text{clip}\left(\frac{I_{gray}(x, y) - \mu}{\sigma} \cdot \alpha + \beta, 125, 175\right) \]

where:
- \( \mu \) is the mean intensity of the grayscale image,
- \( \sigma \) is the standard deviation of the grayscale image intensity,
- \( \alpha \) and \( \beta \) are constants to scale and shift the pixel values to the desired range.

## 5. Reduced Gray Level Depth to 4bpp (Grid 2,2)

**Explanation:**
Reducing the gray level depth from 8 bpp to 4 bpp involves quantizing the intensity levels into fewer distinct values, which groups similar pixel values together.

**Equation:**
\[ I_{4bpp}(x, y) = \left\lfloor \frac{I_{gray}(x, y)}{16} \right\rfloor \cdot 16 \]

where:
- \( I_{4bpp}(x, y) \) is the intensity of the image with reduced gray level depth at pixel \((x, y)\),
- \( I_{gray}(x, y) \) is the grayscale intensity of the original image at pixel \((x, y)\),
- \(\left\lfloor \cdot \right\rfloor\) denotes the floor function, which rounds down to the nearest integer.

## 6. Vertical Mirror Image (Grid 2,3)

**Explanation:**
The vertical mirror operation flips the image along the horizontal axis, producing a reflection of the original image as if viewed in a mirror placed vertically.

**Equation:**
\[ I_{mirror}(x, y) = I_{gray}(x, H - y) \]

where:
- \( I_{mirror}(x, y) \) is the intensity of the mirrored image at pixel \((x, y)\),
- \( I_{gray}(x, y) \) is the grayscale intensity of the original image at pixel \((x, y)\),
- \( H \) is the height of the image.


