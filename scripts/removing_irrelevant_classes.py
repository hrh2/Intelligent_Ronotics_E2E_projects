import os

# Paths
labels_dir = "../dataset/labels"
irrelevant_classes_count = 0  # Number of default classes to skip

# Directories for train and val labels
sub_dirs = ["train", "val"]

# Process each label file
for sub_dir in sub_dirs:
    sub_dir_path = os.path.join(labels_dir, sub_dir)

    if os.path.exists(sub_dir_path):
        for label_file in os.listdir(sub_dir_path):
            label_path = os.path.join(sub_dir_path, label_file)

            # Read and update the label file
            updated_lines = []
            with open(label_path, "r") as f:
                for line in f:
                    parts = line.strip().split()
                    class_id = int(parts[0])

                    # Update class_id by subtracting irrelevant classes
                    if class_id >= irrelevant_classes_count:
                        new_class_id = class_id - irrelevant_classes_count
                        updated_lines.append(f"{new_class_id} {' '.join(parts[1:])}")

            # Overwrite the label file with updated class IDs
            with open(label_path, "w") as f:
                f.write("\n".join(updated_lines))

print("Annotations updated successfully!")
