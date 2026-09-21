import cv2

# Load the image
image = cv2.imread('example.jpg')

# Safety check: Ensure the image actually loaded before doing anything else
if image is None:
    print("Error: Could not load 'example.jpg'. Make sure the image is on your Desktop!")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize the grayscale image to 224x224
    resized_image = cv2.resize(gray_image, (224, 224))

    # Display the resized grayscale image in a single window
    cv2.imshow('Processed Image', resized_image)

    # Wait for a key press
    key = cv2.waitKey(0)  # Wait indefinitely for a key press

    # Check if the "S" or "s" key was pressed
    if key == ord('s') or key == ord('S'):
        # Save the processed image when "S" or "s" is pressed
        cv2.imwrite('grayscale_resized_image.jpg', resized_image)
        print("Image saved as grayscale_resized_image.jpg")
    else:
        print("Image not saved")

    # Close the window
    cv2.destroyAllWindows()

    # Print processed image properties
    print(f"Processed Image Dimensions: {resized_image.shape}")