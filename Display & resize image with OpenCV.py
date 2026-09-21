import cv2

# Since your script and image are both on your Desktop, just use the filename!
image = cv2.imread('example.jpg')

# Safety check: Make sure the image loaded successfully
if image is None:
    print("Error: Could not load image. Make sure 'example.jpg' is right on your Desktop.")
else:
    # Resize the actual image array (Width x Height -> 800x500)
    resized_image = cv2.resize(image, (800, 500))

    # Create a resizable window and display the resized image
    cv2.namedWindow('Resized Image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Resized Image', 800, 500)
    
    cv2.imshow('Resized Image', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Print the new image properties (Height, Width, Channels)
    print(f"New Image Dimensions: {resized_image.shape}")