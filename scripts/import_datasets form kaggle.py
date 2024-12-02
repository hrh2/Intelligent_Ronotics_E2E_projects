import kagglehub

# Download latest version
path = kagglehub.dataset_download("gakundohope/automatic-number-plate-recognition")

print("Path to dataset files:", path)