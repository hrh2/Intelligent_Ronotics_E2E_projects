import os
import shutil

# Paths to your directories
images_dir = 'datasets'        # Directory with images
labels_dir = 'datasets_labels'        # Directory with label files
unwanted_dir = 'unwanted'    # Directory to move images without labels

# Create 'unwanted' directory if it doesn't exist
if not os.path.exists(unwanted_dir):
    os.makedirs(unwanted_dir)

# List all image files in the images directory
for image_name in os.listdir(images_dir):
    # Check if the file is an image (assuming .jpg, .jpeg, .png for YOLO images)
    if image_name.endswith(('.jpg', '.jpeg', '.png')):
        # Get the label file corresponding to the image
        label_name = os.path.splitext(image_name)[0] + '.txt'
        label_path = os.path.join(labels_dir, label_name)

        # Check if the label file exists
        if not os.path.exists(label_path):
            # If label does not exist, move the image to the unwanted directory
            image_path = os.path.join(images_dir, image_name)
            shutil.move(image_path, os.path.join(unwanted_dir, image_name))
            print(f"Moved {image_name} to unwanted directory")
        else:
            print(f"Label exists for {image_name}")
