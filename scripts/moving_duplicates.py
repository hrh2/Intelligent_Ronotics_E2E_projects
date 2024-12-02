import os
import imagehash
from PIL import Image
import shutil

def compute_image_hash(image_path):
    """Compute the hash of an image."""
    try:
        image = Image.open(image_path)
        return imagehash.phash(image)  # You can use other hash methods like dhash or ahash
    except Exception as e:
        print(f"Error reading image {image_path}: {e}")
        return None

def move_duplicates(base_dir, duplicate_dir):
    """Move duplicate images to a 'duplicates' directory."""
    # Ensure the 'duplicates' directory exists
    if not os.path.exists(duplicate_dir):
        os.makedirs(duplicate_dir)

    image_hashes = {}
    for root, _, files in os.walk(base_dir):
        for file in files:
            image_path = os.path.join(root, file)
            # Skip non-image files
            if not file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
                continue

            # Compute hash of the image
            image_hash = compute_image_hash(image_path)
            if image_hash is None:
                continue

            # If the hash is already seen, it's a duplicate
            if image_hash in image_hashes:
                duplicate_image_path = image_path
                print(f"Duplicate found: {image_path}")

                # Move duplicate image to the 'duplicates' directory
                new_path = os.path.join(duplicate_dir, file)
                counter = 1
                # Ensure no overwrite by checking if the file exists in the duplicates folder
                while os.path.exists(new_path):
                    new_path = os.path.join(duplicate_dir, f"{counter}_{file}")
                    counter += 1

                shutil.move(duplicate_image_path, new_path)
                print(f"Moved to {new_path}")
            else:
                # Otherwise, store the hash with the image path
                image_hashes[image_hash] = image_path

if __name__ == "__main__":
    base_dir = 'datasets'  # Replace with your base directory path
    duplicate_dir = 'duplicates'  # Replace with your duplicates directory path
    move_duplicates(base_dir, duplicate_dir)
