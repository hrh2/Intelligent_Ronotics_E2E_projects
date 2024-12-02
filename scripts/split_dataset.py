import os
import random
import shutil

# Paths to your dataset
dataset_dir = "../dataset"
images_dir = os.path.join(dataset_dir, "images")
labels_dir = os.path.join(dataset_dir, "labels")

# Output directories for train and val splits
train_images_dir = os.path.join(images_dir, "train")
val_images_dir = os.path.join(images_dir, "val")
train_labels_dir = os.path.join(labels_dir, "train")
val_labels_dir = os.path.join(labels_dir, "val")

# Ensure output directories exist
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# Train/val split ratio
train_ratio = 0.8  # 80% training, 20% validation

# List all images
all_images = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
random.shuffle(all_images)  # Shuffle for randomness

# Split into train and val sets
train_size = int(len(all_images) * train_ratio)
train_images = all_images[:train_size]
val_images = all_images[train_size:]

# Move files to train and val directories
def move_files(image_list, target_images_dir, target_labels_dir):
    for image_name in image_list:
        base_name = os.path.splitext(image_name)[0]
        image_path = os.path.join(images_dir, image_name)
        label_path = os.path.join(labels_dir, f"{base_name}.txt")

        # Move image
        if os.path.exists(image_path):
            shutil.move(image_path, target_images_dir)

        # Move label (if it exists)
        if os.path.exists(label_path):
            shutil.move(label_path, target_labels_dir)

# Move training and validation sets
move_files(train_images, train_images_dir, train_labels_dir)
move_files(val_images, val_images_dir, val_labels_dir)

print(f"Dataset split completed!")
print(f"Training images: {len(os.listdir(train_images_dir))}, Training labels: {len(os.listdir(train_labels_dir))}")
print(f"Validation images: {len(os.listdir(val_images_dir))}, Validation labels: {len(os.listdir(val_labels_dir))}")
