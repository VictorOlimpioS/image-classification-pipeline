import cv2


def standardize_image(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Could not read the image at {image_path}")
        return None
    # Resize the image to a standard size (e.g., 256x256)
    image_resized = cv2.resize(image, (256, 256))
    print(f"Image shape: {image_resized.shape}, dtype: {image_resized.dtype}, max: {image_resized.max()}, min: {image_resized.min()}")
    return image_resized