import os

# Define the directory containing annotation files
fine_tuning_dir = "../pre_datasets"
new_class_id = 4  # The new class ID to set for all objects

# Process every `.txt` file in the directory
for label_file in os.listdir(fine_tuning_dir):
    label_path = os.path.join(fine_tuning_dir, label_file)

    if label_file.endswith(".txt"):
        updated_lines = []

        # Read the current label file
        with open(label_path, "r") as f:
            for line in f:
                parts = line.strip().split()

                if len(parts) >= 5:  # Ensure the line has the correct YOLO format
                    # Replace the class_id with the new one
                    parts[0] = str(new_class_id)
                    updated_lines.append(" ".join(parts))

        # Write the updated lines back to the file
        with open(label_path, "w") as f:
            f.write("\n".join(updated_lines))

print(f"Class IDs updated to {new_class_id} in all files.")
