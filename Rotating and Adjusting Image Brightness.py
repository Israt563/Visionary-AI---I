import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('example.jpg')

# Safety check
if image is None:
    print("Error: Could not load 'example.jpg'. Make sure the image is on your Desktop!")
else:
    # Convert original to RGB for plotting
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 1. Rotate the image by 45 degrees around its center
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 45, 1.0)  # rotate by 45 degrees
    rotated = cv2.warpAffine(image, M, (w, h))
    rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)

    # 2. Increase brightness by adding 50 to all pixel values
    brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
    brighter = cv2.add(image, brightness_matrix)
    brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)

    # Create a figure with 3 columns to display them all together
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Display Original Image
    axes[0].imshow(image_rgb)
    axes[0].set_title("Original Image")
    axes[0].axis('off')

    # Display Rotated Image
    axes[1].imshow(rotated_rgb)
    axes[1].set_title("Rotated (45°)")
    axes[1].axis('off')

    # Display Brighter Image
    axes[2].imshow(brighter_rgb)
    axes[2].set_title("Brighter Image")
    axes[2].axis('off')

    # Adjust layout and display the window
    plt.tight_layout()
    plt.show()