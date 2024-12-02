# **Third Attempt 2: Fresh Training on Instructor Dataset**
## **Guide**
### **Step 1: Project Setup**
1. Navigate to your base project directory (or create one if you are starting fresh):
   ```bash
   mkdir ANPR  # For new users
   cd ANPR
   ```
2. Clone the YOLOv5 repository and install dependencies:
   ```bash
   git clone https://github.com/ultralytics/yolov5
   cd yolov5
   pip install -r requirements.txt
   ```

---

### **Step 2: Download and Prepare the Dataset**
1. Download the **Instructor Dataset** (refer to the Datasets section for the download link).
2. Extract the dataset (`ANPR_dataset01.zip`) and locate the `dataset01` directory.
3. Use the provided script [`rearrange_dataset_into_train_val`.py](./scripts/rearrange_dataset_into_train_val.py) to organize the dataset for training:
   ```bash
   mv dataset01 ./yolov5
   python rearrange_dataset_into_train_val.py
   ```
    - Modify the script to ensure the paths align with your project setup:
      ```python
      src_folder = "./dataset01"  # Main dataset directory containing images, labels, and `class.txt`.
      train_images = "./yolov5/dataset01/images/train"
      train_labels = "./yolov5/dataset01/labels/train"
      val_images = "./yolov5/dataset01/images/val"
      val_labels = "./yolov5/dataset01/labels/val"
      ```

4. Download the configuration file [`dataset01.yaml`](https://huggingface.co/datasets/Hirwa/Automatic_Number_Plate_Recognition/resolve/main/dataset01.yaml?download=true) and place it in the `yolov5` directory.

---

### **Step 3: Train the Model**
1. Train the YOLOv5 model with the prepared dataset:
   ```bash
   python train.py --img 640 --batch 10 --epochs 20 --data dataset01.yaml --weights yolov5s.pt --name ANPR_C3B10E20_YV5
   ```
    - **Naming Convention Explained**:
        - `C3`: Number of classes (3).
        - `B10`: Batch size (10).
        - `E20`: Number of epochs (20).
        - `YV5`: YOLOv5 pre-trained weights.

---

### **Step 4: Performing Inference**
1. Perform inference on a video using the newly trained model:
   ```bash
   python detect.py --source "../test/transit-01.mov" --weights "runs/train/ANPR_C3B10E20_YV5/weights/best.pt"
   ```
2. For customized detection integrated with hardware communication:
   ```bash
   python detect_communicate.py --source ../test/transit-01.mov --weights runs/train/ANPR_C3B10E20_YV5/weights/best.pt
   ```
    - Ensure the video path specified in the `--source` parameter is accurate.

---
## Continue with the **[hardware](./Hardware.md)** ...