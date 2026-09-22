import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    """Apply the specified color filter to the image."""
    filtered_image = image.copy()
    
    if filter_type == "original":
        return filtered_image
    elif filter_type == "red_tint":
        # Keep only the Red channel (Index 2)
        filtered_image[:, :, 0] = 0  # Blue channel to 0
        filtered_image[:, :, 1] = 0  # Green channel to 0
    elif filter_type == "blue_tint":
        # Keep only the Blue channel (Index 0)
        filtered_image[:, :, 1] = 0  # Green channel to 0
        filtered_image[:, :, 2] = 0  # Red channel to 0
    elif filter_type == "green_tint":
        # Keep only the Green channel (Index 1)
        filtered_image[:, :, 0] = 0  # Blue channel to 0
        filtered_image[:, :, 2] = 0  # Red channel to 0
    elif filter_type == "increase_red":
        # Increase the intensity of the red channel safely
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == "decrease_blue":
        # Decrease the intensity of the blue channel safely
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
        
    return filtered_image

# Load the image from the Desktop
image_path = 'example.jpg'  
image = cv2.imread(image_path)

if image is None:
    print("Error: 'example.jpg' not found! Make sure it's on your Desktop.")
else:
    filter_type = "original"  # Default filter type

    print("\n--- OpenCV Interactive Color Filters ---")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - Increase Red Intensity")
    print("d - Decrease Blue Intensity")
    print("o - Reset to Original")
    print("q - Quit")
    print("---------------------------------------")

    while True:
        # Apply the selected filter
        filtered_image = apply_color_filter(image, filter_type)
        
        # Display the filtered image
        cv2.imshow("Interactive Color Filters", filtered_image)
        
        # Wait for key press
        key = cv2.waitKey(0) & 0xFF

        # Map key presses to filters
        if key == ord('r'):
            filter_type = "red_tint"
            print("Applied: Red Tint")
        elif key == ord('b'):
            filter_type = "blue_tint"
            print("Applied: Blue Tint")
        elif key == ord('g'):
            filter_type = "green_tint"
            print("Applied: Green Tint")
        elif key == ord('i'):
            filter_type = "increase_red"
            print("Applied: Increase Red Intensity")
        elif key == ord('d'):
            filter_type = "decrease_blue"
            print("Applied: Decrease Blue Intensity")
        elif key == ord('o'):
            filter_type = "original"
            print("Reset to Original Image")
        elif key == ord('q'):
            print("Exiting application...")
            break
        else:
            print("Invalid key! Use 'r', 'b', 'g', 'i', 'd', 'o', or 'q'.")

cv2.destroyAllWindows()