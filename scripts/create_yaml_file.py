import os

# Paths
dataset_path = "../dataset"  # Replace with the actual dataset path
classes_file = os.path.join(dataset_path, "classes.txt")  # Path to classes.txt
output_file = os.path.join(dataset_path, "dataset.yaml")  # Path to dataset.yaml

# Ensure the paths to images are correct
train_images = os.path.join(dataset_path, "images", "train")
val_images = os.path.join(dataset_path, "images", "val")

# Read class names from classes.txt
with open(classes_file, "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# Create the dataset.yaml content
yaml_content = f"""# Auto-generated dataset.yaml
train: {train_images}
val: {val_images}

nc: {len(class_names)}  # Number of classes
names:
"""

# Add class names
yaml_content += "\n".join([f"  - {name}" for name in class_names])

# Write to dataset.yaml
with open(output_file, "w") as f:
    f.write(yaml_content)

print(f"dataset.yaml created successfully at {output_file}")
