# To load an image from a file, use the open() function in the Image module:

from PIL import Image
im = Image.open("path/to/your_file")

# If successful, this function returns an Image object. You can now use instance attributes to examine the file contents:
print(im.format, im.size, im.mode)
# output: PPM (512, 512) RGB

# .format() gets the format for the file for example PNG
# .size() returns a tuple which is (width, height)

# You can resize an image using the Pillow library (PIL) in Python by following these steps:

# 1. Install Pillow (if not already installed):
# If you don't have Pillow installed, you can install it using pip:

# pip install Pillow
  

# 2. Import the Pillow library:

from PIL import Image


# 3. Open the image you want to resize:
original_image = Image.open("path/to/your/image.jpg")
# Replace `"path/to/your/image.jpg"` with the path to your image file.

# 4. Resize the image:
# You can resize the image using the `resize` method. This method takes the new dimensions as a tuple (width, height).
# For example, to resize the image to a width of 300 pixels and a proportional height:

width, height = 300, int(original_image.height * (300 / original_image.width))
resized_image = original_image.resize((width, height))

   

# If you want to specify only the height and maintain the aspect ratio:

height = 200
width = int(original_image.width * (200 / original_image.height))
resized_image = original_image.resize((width, height))
  


# 5. Save or display the resized image:
# You can save the resized image to a file or display it as needed:
# To save the image to a file:
resized_image.save("path/to/your/resized_image.jpg")

# To display the image using a built-in image viewer:
resized_image.show()


# Here's a complete example that opens an image, resizes it, and saves the resized image:

from PIL import Image

original_image = Image.open("path/to/your/image.jpg")

# Resize the image to a specific width and maintain aspect ratio
width, height = 300, int(original_image.height * (300 / original_image.width))
resized_image = original_image.resize((width, height))

# Save the resized image
resized_image.save("path/to/your/resized_image.jpg")

# Remember to replace `"path/to/your/image.jpg"` and `"path/to/your/resized_image.jpg"` with the actual paths for your input and output files.

# To get the size of an image in megabytes, you can convert the size in bytes to megabytes by dividing by 1024 twice (first to get from bytes to kilobytes and then to megabytes).
# Here's how you can do it:

from PIL import Image

# Open the image
image = Image.open("path/to/your/image.jpg")

# Get the size of the image in bytes
image_size_bytes = len(image.tobytes())

# Convert to megabytes
image_size_megabytes = image_size_bytes / (1024.0 * 1024.0)

# Print the size in megabytes
print(f"The image size is {image_size_megabytes:.2f} megabytes")

# This code will give you the size of the image in megabytes, rounded to two decimal places.
