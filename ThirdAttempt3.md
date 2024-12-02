## **Second Attempt: Reduced Classes** *(If you  didn't  Any Attempt)*

### **Guide**

#### **Step 1: Project Setup**
1. Navigate to your base project directory (or create it if you are starting fresh):
   ```bash
   mkdir ANPR  # For users who didn’t try the first attempt
   cd ANPR
   ```
2. Clone the YOLOv5 repository and install dependencies (skip this step if already done):
   ```bash
   git clone https://github.com/ultralytics/yolov5
   cd yolov5
   pip install -r requirements.txt
   ```

---

#### **Step 2: Download the Extended Dataset**
1. Download the **[Instructor Extended Dataset](https://huggingface.co/datasets/Hirwa/Automatic_Number_Plate_Recognition/resolve/main/ANPR_dataset02.zip?download=true)** .
2. Extract the downloaded file `ANPR_dataset02.zip` and locate the `dataset02` directory.
3. Move the `dataset02` directory into your `yolov5` project folder:
   ```bash
   mv dataset02 ./yolov5
   ```

---

#### **Step 3: Training Phase**
1. Locate the `dataset02.yaml` configuration file within the `dataset02` directory.
2. Move the configuration file to the main `yolov5` directory:
   ```bash
   mv dataset02/dataset02.yaml ./yolov5
   ```
3. Update the paths in `dataset02.yaml` to point to the correct dataset locations:
   ```yaml
   # Auto-generated dataset.yaml

   train: ./dataset02/images/train
   val: ./dataset02/images/val
   ```

#### *Step 1 : *Train the Model**:
   ```bash
   python train.py --img 640 --batch 10 --epochs 20 --data dataset02.yaml --weights yolov5s.pt --name ANPR_C5B10E20_YV5
   ```
    - **Naming Convention Explained**:
        - `C5`: Number of classes (5).
        - `B10`: Batch size (10).
        - `E20`: Number of epochs (20).
        - `YV5`: YOLOv5 pre-trained weights.
    - This naming scheme helps maintain consistency for comparison across training attempts.

---

#### **Step 2: Performing Inference**
1. Perform inference on a video using the newly trained model:
   ```bash
   python detect.py --source "../test/transit-01.mov" --weights "runs/train/ANPR_C5B10E20_YV5/weights/best.pt"
   ```
2. For customized detection integrated with hardware communication, use the modified script:
   ```bash
   python detect_communicate.py --source ../test/transit-01.mov --weights runs/train/ANPR_C5B10E20_YV5/weights/best.pt
   ```
   - Ensure the video path specified in the `--source` parameter is accurate.

---
## Continue with the **[hardware](./Hardware.md)** ...