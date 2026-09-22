import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('example.jpg')

# Safety check
if image is None:
    print("Error: Could not load 'example.jpg'. Make sure the image is on your Desktop!")
else:
    height, width = image.shape[:2]
    print(f"Original Image Dimensions: {height}x{width}")

    # 1. Convert BGR to RGB for correct colors in Matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 2. Convert to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 3. Cropping the image (Rows 100 to 300, Columns 200 to 400)
    # Added a safeguard so it doesn't crash if your image happens to be too small
    y1, y2 = min(100, height), min(300, height)
    x1, x2 = min(200, width), min(400, width)
    cropped_image = image[y1:y2, x1:x2]
    cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)

    # Create a figure with 1 row and 3 columns to show everything together
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Display RGB Image
    axes[0].imshow(image_rgb)
    axes[0].set_title("RGB Image")
    axes[0].axis('off')  # Hide axis ticks

    # Display Grayscale Image
    axes[1].imshow(gray_image, cmap='gray')
    axes[1].set_title("Grayscale Image")
    axes[1].axis('off')

    # Display Cropped Region
    axes[2].imshow(cropped_rgb)
    axes[2].set_title("Cropped Region")
    axes[2].axis('off')

    # Show all images nicely formatted in one window
    plt.tight_layout()
    plt.show()