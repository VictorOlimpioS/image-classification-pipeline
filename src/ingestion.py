import cv2


def ingest_image(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Could not read the image at {image_path}")
        return None
    print(f"Image shape: {image.shape}, dtype: {image.dtype}, max: {image.max()}, min: {image.min()}")
    return image