import pathlib
import ingestion
import random
import numpy as np


images = []
labels = []



categories = [("data/raw/non_flooded", 0), ("data/raw/flooded", 1)]
for category_path, label in categories:
    category_images = pathlib.Path(category_path).glob("*.jpg")
    for image in category_images:
        standardized_image = ingestion.standardize_image(str(image))
        if standardized_image is not None:
            images.append(standardized_image)
            labels.append(label)

combined_data = list(zip(images, labels))
random.shuffle(combined_data)
images[:], labels[:] = zip(*combined_data)
images = np.array(images)
labels = np.array(labels)
        
