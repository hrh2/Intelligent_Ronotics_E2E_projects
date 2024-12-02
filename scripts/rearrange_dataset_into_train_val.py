import os
import random
import shutil

def prepare_data(src_folder):
    # Create temporary folders for organizing images and labels if they don’t exist
    images_folder = os.path.join(src_folder, "original_images")
    labels_folder = os.path.join(src_folder, "original_labels")
    os.makedirs(images_folder, exist_ok=True)
    os.makedirs(labels_folder, exist_ok=True)

    # Move images and labels to their respective folders
    for file in os.listdir(src_folder):
        if file.endswith('.jpg'):
            shutil.move(os.path.join(src_folder, file), images_folder)
        elif file.endswith('.txt') and file != 'classes.txt':
            shutil.move(os.path.join(src_folder, file), labels_folder)

def split_data(src_folder, train_images, train_labels, val_images, val_labels, split_ratio=0.8):
    images_folder = os.path.join(src_folder, "original_images")
    labels_folder = os.path.join(src_folder, "original_labels")

    # Ensure destination directories exist
    os.makedirs(train_images, exist_ok=True)
    os.makedirs(train_labels, exist_ok=True)
    os.makedirs(val_images, exist_ok=True)
    os.makedirs(val_labels, exist_ok=True)

    # List and shuffle images
    files = [f for f in os.listdir(images_folder) if f.endswith('.jpg')]
    random.shuffle(files)

    # Calculate split index
    split_index = int(len(files) * split_ratio)
    train_files = files[:split_index]
    val_files = files[split_index:]

    # Move training files
    for file in train_files:
        img_path = os.path.join(images_folder, file)
        label_path = os.path.join(labels_folder, file.replace('.jpg', '.txt'))
        if os.path.exists(label_path):
            shutil.move(img_path, os.path.join(train_images, file))
            shutil.move(label_path, os.path.join(train_labels, file.replace('.jpg', '.txt')))
        else:
            print(f"Warning: Missing label for {file}")

    # Move validation files
    for file in val_files:
        img_path = os.path.join(images_folder, file)
        label_path = os.path.join(labels_folder, file.replace('.jpg', '.txt'))
        if os.path.exists(label_path):
            shutil.move(img_path, os.path.join(val_images, file))
            shutil.move(label_path, os.path.join(val_labels, file.replace('.jpg', '.txt')))
        else:
            print(f"Warning: Missing label for {file}")

    # Delete temporary folders
    shutil.rmtree(images_folder)
    shutil.rmtree(labels_folder)

# Directories
src_folder = "../dataset00"  # The main dataset directory
train_images = "../yolov5/dataset00/images/train"
train_labels = "../yolov5/dataset00/labels/train"
val_images = "../yolov5/dataset00/images/val"
val_labels = "../yolov5/dataset00/labels/val"

# Prepare and split the data
prepare_data(src_folder)
split_data(src_folder, train_images, train_labels, val_images, val_labels)
