import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    """Utility function to display an image."""
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:  # Grayscale image
        plt.imshow(image, cmap='gray')
    else:  # Color image
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def interactive_edge_detection(image_path):
    """Interactive activity for edge detection and filtering."""
    image = cv2.imread(image_path)
    if image is None:
        print("Error: 'example.jpg' not found! Make sure it's on your Desktop.")
        return

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Original Grayscale Image", gray_image)

    print("\n--- OpenCV Edge Detection & Filtering Menu ---")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")

    while True:
        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            # Sobel Edge Detection (Using convertScaleAbs to safely handle negative gradients)
            sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
            abs_sobel_x = cv2.convertScaleAbs(sobel_x)
            abs_sobel_y = cv2.convertScaleAbs(sobel_y)
            combined_sobel = cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)
            display_image("Sobel Edge Detection", combined_sobel)

        elif choice == "2":
            # Canny Edge Detection
            print("Adjust thresholds for Canny (default recommended: 100 and 200)")
            try:
                lower_thresh = int(input("Enter Lower threshold: "))
                upper_thresh = int(input("Enter Upper threshold: "))
                edges = cv2.Canny(gray_image, lower_thresh, upper_thresh)
                display_image("Canny Edge Detection", edges)
            except ValueError:
                print("Please enter valid integers for thresholds.")

        elif choice == "3":
            # Laplacian Edge Detection
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            abs_laplacian = cv2.convertScaleAbs(laplacian)
            display_image("Laplacian Edge Detection", abs_laplacian)

        elif choice == "4":
            # Gaussian Smoothing
            print("Adjust kernel size for Gaussian blur (must be an odd number, e.g., 5, 9, 15)")
            try:
                kernel_size = int(input("Enter kernel size (odd number): "))
                if kernel_size % 2 == 0:
                    print("Kernel size must be odd! Using 5 by default.")
                    kernel_size = 5
                blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
                display_image("Gaussian Smoothed Image", blurred)
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "5":
            # Median Filtering
            print("Adjust kernel size for Median filtering (must be an odd number, e.g., 5, 9)")
            try:
                kernel_size = int(input("Enter kernel size (odd number): "))
                if kernel_size % 2 == 0:
                    print("Kernel size must be odd! Using 5 by default.")
                    kernel_size = 5
                median_filtered = cv2.medianBlur(image, kernel_size)
                display_image("Median Filtered Image", median_filtered)
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "6":
            # Exit
            print("Exiting edge detection menu. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")

# Run the interactive script using the image on the Desktop
interactive_edge_detection('example.jpg')