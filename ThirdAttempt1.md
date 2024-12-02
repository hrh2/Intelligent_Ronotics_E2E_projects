### **Third Attempt 1: Fresh Training on Instructor Extended Dataset**
1. #### **Guide (For Those Who didn't the Second Attempt)**: [READ](./ThirdAttempt3.md)
2. #### **Guide (For Those Who Completed the Second Attempt)** :
   Since the dataset structure remains the same, you can directly proceed to training. Instead of reusing the old weights, we’ll initialize the training with YOLOv5’s pre-trained weights.

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