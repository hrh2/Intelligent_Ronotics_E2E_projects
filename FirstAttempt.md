
## **First Attempt: Multi-Class Dataset**
### **Steps and Guide**

#### **Step 1: Project Setup**
1. Create the base directory for your project:
   ```bash
   mkdir ANPR
   cd ANPR
   ```
2. Clone the YOLOv5 repository and install dependencies:
   ```bash
   git clone https://github.com/ultralytics/yolov5
   cd yolov5
   pip install -r requirements.txt
   ```

---

#### **Step 2: Download Extended Dataset**
1. Download the **[Extended Dataset Link](https://huggingface.co/datasets/Hirwa/Automatic_Number_Plate_Recognition/resolve/main/ANPR_dataset00.zip?download=true)**.
2. Unzip the downloaded file `ANPR_dataset00.zip`, extract its contents, and locate the `dataset00` directory inside unzipped  `ANPR_dataset00`.
3. Move the `dataset00` directory into your `yolov5` project folder:
4. Open terminal in your Project directory `ANPR` run the below command
   ```bash
   mv dataset00 ./yolov5
   ```

---

#### **Step 3: Training Phase**
1. Locate the `dataset00.yaml` configuration file with in the `dataset00` directory which was moved  to `yolov5` in the last step.
2. Manually move the configuration file `dataset00.yaml` into the main `yolov5` directory or use the below command :
   ```bash
   mv dataset00/dataset00.yaml ./yolov5
   ```
3. Edit and Update the paths in `dataset00.yaml` to point to the correct dataset locations:
   ```yaml
   # Auto-generated dataset.yaml
   
   train: ./dataset00/images/train
   val: ./dataset00/images/val
   ```
4. Train the model using the following command:
   ```bash
   python train.py --img 640 --batch 16 --epochs 50 --data dataset00.yaml --weights yolov5s.pt --name ANPR_C58B16E50_YV5
   ```
    - **Explanation of Naming Convention**:
        - `C58`: Number of classes (58).
        - `B16`: Batch size (16).
        - `E50`: Number of epochs (50).
        - `YV5`: YOLO version (YOLOv5).
    - This naming convention helps in comparing different models and their configurations.

---

#### **Step 4: Performing Inference**
1. Run inference on a video using the trained model:
   ```bash
   python detect.py --source "../test/transit-01.mov" --weights "runs/train/ANPR_C58B16E50_YV5/weights/best.pt"
   ```
2. For customized detection with hardware communication, use the modified script:
   ```bash
   python detect_communicate.py --source ../test/transit-01.mov --weights runs/train/ANPR_C58B16E50_YV5/weights/best.pt  --conf-thres 0.55
   ```
    - Ensure the video path specified in the `--source` parameter is correct.

---
## Continue with the **[hardware](./Hardware.md)** ...