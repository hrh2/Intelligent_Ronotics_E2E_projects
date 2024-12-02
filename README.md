# **Automatic Number Plate Recognition (ANPR) Project**

This project is an end-to-end implementation of an **Automatic Number Plate Recognition (ANPR)** system using **YOLOv5** for number plate detection and Arduino for hardware interaction. The project includes custom dataset preparation, model training, and hardware integration via UART communication protocol.

---

## **Project Overview**
The goal of this project is to detect car number plates from images or video, classify them into specific categories, and send the detected results to a hardware component (Arduino). The hardware performs actions such as blinking an LED corresponding to a detected car's number plate.

---

## **Key Features**
1. **Dataset Preparation**:
    - Extract frames from videos.
    - Filter images with visible number plates and remove duplicates.
    - Annotate images and organize them into a structured dataset.
2. **Model Training**:
    - Train YOLOv5 models with different configurations and datasets.
    - Evaluate and compare model performance using metrics.
3. **Hardware Integration**:
    - Use UART communication to send detection results to Arduino.
    - Perform actions (e.g., LED blinking) based on detected classes.

---

## **Project Workflow**

### **1. Dataset Preparation**
1. **Extract Frames**:
   ```bash
   python extract_frames.py 
   ```
2. **Remove Duplicates**:
   ```bash
   python remove_duplicates.py
   ```
3. **Filter images**\
   Filter many  images  for each  car (For example:Many Images of a car with plate number **RAH213T**) with visible number plates move them in the dataset directory

4. **Annotation**:
   Use `LabelImg` to annotate images and save labels in YOLO format.
   ```bash
    labelImg <your data set directory>
   ```
5. **Organize Dataset**:\
Organize images into directories for training.\
    use  the below scripts \
   [Rearrange dataset Script](./scripts/rearrange_dataset_into_train_val.py)\
   but makes you alter these lines to update the path well to suit you project
    ```bash
    src_folder = "<path to your dataset directory with images and their classes>"  # The main dataset directory  which contain only images their labels and `class.txt`
    train_images = "./yolov5/dataset/images/train"
    train_labels = "./yolov5/datase/labels/train"
    val_images = "./yolov5/dataset/images/val"
    val_labels = "./yolov5/dataset/labels/val"
   ```
---

### **2. Model Training**
1. **Train Model**:
   Go into you `yolov5` directory with `cd yolov5` and run the following Commands one at a time  or even one of them according to your preferred arguments
   ```bash
   python train.py --img 640 --batch 16 --epochs 20 --data <configuration_file> --weights yolov5s.pt --name <name_of_your_training_directory>
   python train.py --img 640 --batch 16 --epochs 20 --data dataset00.yaml --weights yolov5s.pt --name ANPR_B16E20_YV5
   ```
   Replace `dataset.yaml` with your dataset configuration file.

2. **Fine-Tuning on new dataset**:
   Whenever you are going to Fine-tune refer to the below scripts\
   Before running the below codes make sure  you first use [Rearrange dataset Script](./scripts/rearrange_dataset_into_train_val.py)  to insure datasets are well organized are ready for training
   ```bash
   python train.py --img 640 --batch 16 --epochs 50 --data <configuration_file> --weights <any_path_to_your_previous_weights>
   python train.py --img 640 --batch 16 --epochs 50 --data dataset01.yaml --weights runs/train/ANPR_C10B16E20_YV5/weights/best.pt
   ```

---

### **3. Inference**
1. **Run Detection**:
   Use the `detect.py` or if you have the modified one use it:
   ```bash
   python detect.py --source <input_source> --weights <path_to_model_weights>  --img <size> --conf-thres <input_your_confidence_threshold_normally_from_0_to_1>
   #Default  detect.py
   python detect.py --source "../test/transit-01.mov" --weights "runs/train/ANPR_B16E20_YV5/weights/best.pt" --conf-thres 0.3
   #Customized detect.py with a new name
   python detect_communicate.py --source ../test/transit-01.mov --weights runs/train/ANPR_B16E20_YV5/weights/best.pt --conf-thres 0.5
   ```

2. **Example Output**:
   ```
    #sample output of the default detect.py
   
    video 1/1 (47/5164) /home/hrh/Documents/Workspace/ANPR/test/transit-01.mov: 384x640 (no detections), 81.4ms
    video 1/1 (82/5164) /home/hrh/Documents/Workspace/ANPR/test/transit-01.mov: 384x640 1 RAH213T, 79.4ms
   
    #sample on the modified detect.py -> detect_communicate.py
   
    video 1/1 (65/5164) /home/hrh/Documents/Workspace/ANPR/test/transit-01.mov: 384x640 (no detections), 71.1ms
    video 1/1 (66/5164) /home/hrh/Documents/Workspace/ANPR/test/transit-01.mov: 384x640 (no detections), 79.6ms
    Signal sent: RAH213T
    video 1/1 (67/5164) /home/hrh/Documents/Workspace/ANPR/test/transit-01.mov: 384x640 1 RAH213T, 76.5ms
   ``` 

---

# **My Training Approaches**
## **First Attempt: Multi-Class Dataset**

#### **Dataset**
- The initial dataset included several car classes extracted from video footage.
    - Focused on cars with visible number plates, ensuring at least 7 images per class.
    - Total classes: 10+.

- #### **Model**
    - Used the YOLOv5s pre-trained model fine-tuned on the custom dataset.

- #### **[Metrics](https://huggingface.co/Hirwa/ANPR/blob/main/ANPR_C58B10E20_YV5/F1_curve.png)**
  - The model's performance was suboptimal, with low precision and recall scores.
- #### **Challenges**:
    - Dataset inconsistencies, uneven representation across classes.
    - A high number of classes relative to dataset size, leading to poor generalization.

- #### **Observation**
  - The model struggled with overfitting, failing to generalize effectively to unseen data.
#### **[GUIDE 1](./FirstAttempt.md)**

---
## **Second Attempt: Reduced Classes** *(For Those Who Tried the First Attempt)*

- #### **Dataset**
  - An instructor-provided dataset initially contained 3 dominant classes. I extended it by adding 2 additional classes, resulting in a total of 5 classes.
  - All images were carefully annotated using `LabelImg` to ensure high-quality labels.

- #### **Model**
  - Fine-tuned the YOLOv5s model on the updated dataset.
  - Used weights from the first attempt as a starting point for fine-tuning.

- #### **[Metrics](https://huggingface.co/Hirwa/ANPR/blob/main/ANPR_C5B8E10_V2/F1_curve.png)**
  - Achieved improved performance in terms of mAP, precision, and recall compared to the first model.
  - The reduced number of classes and a cleaner, more consistent dataset contributed significantly to better generalization and reduced overfitting.
#### **[GUIDE 2](./SecondAttempt.md)**

---
### **Third Attempt 1: Fresh Training on Instructor Extended Dataset**

- #### **Dataset**
  - The dataset from the second attempt was reused (5 classes).

- #### **Model**
  - YOLOv5s model trained from scratch using the YOLOv5 pre-trained weights (`yolov5s.pt`).
  - Training was conducted without leveraging weights from previous models.

- #### **[Metrics](https://huggingface.co/Hirwa/ANPR/blob/main/ANPR_C5B8E15_YV5/F1_curve.png)**
  - Achieved results comparable to the fine-tuned model in the second attempt.
  - This training method served as a baseline comparison to evaluate the impact of fine-tuning on performance.

#### **[GUIDE 3](./ThirdAttempt1.md)**

---

# Ultimate Quick start

---

### **Third Attempt 2: Fresh Training on Instructor Dataset**

#### **Dataset**
- Used the [instructor-provided dataset](https://huggingface.co/datasets/Hirwa/Automatic_Number_Plate_Recognition/resolve/main/ANPR_dataset01.zip?download=true) with 3 classes (same as in the first attempt).

#### **Model**
- YOLOv5s model trained from scratch using the YOLOv5 pre-trained weights (`yolov5s.pt`).

#### **Metrics**
- Achieved results comparable to those from the fine-tuned model in the second attempt.
- This approach served as a benchmark for analyzing the impact of training from scratch on a few classes but enough dataset.

#### **[GUIDE 4](./ThirdAttempt2.md)**

---


## **Hardware Integration**

### **UART Communication**
A modified copy of`detect.py` named [detect_communicate.py](./scripts/detect_communicate.py) was created to enable hardware communication:
- The script sends detected classes (e.g., car registration numbers) over a serial connection.
- Arduino reads the class and performs corresponding actions (e.g., lighting LEDs).

### **Arduino Code**
Below is the Arduino code used to control LEDs based on the detected number plate class:

Codes : [Hardware](./Hardware.md)

## **Scripts and Files**
### **Custom Scripts**
1. [Frame Extraction Script](./scripts/extract_frames.py)
2. [Duplicate Removal Script](./scripts/moving_duplicates.py)
3. [Rearrange dataset Script](./scripts/rearrange_dataset_into_train_val.py)
4. [Modified `detect.py` for UART Communication](./scripts/detect_communicate.py)

### **Datasets**
- Extended Dataset: [Extended Dataset Link](https://huggingface.co/datasets/Hirwa/Automatic_Number_Plate_Recognition/resolve/main/ANPR_dataset00.zip?download=true)
- Instructor Dataset: [Dataset Link](https://huggingface.co/datasets/Hirwa/Automatic_Number_Plate_Recognition/resolve/main/ANPR_dataset01.zip?download=true)
- Instructor Extended Dataset : [I.E.Dataset](https://huggingface.co/datasets/Hirwa/Automatic_Number_Plate_Recognition/resolve/main/ANPR_dataset02.zip?download=true)
### **Trained Models**
- First Model v1: [Model Link](https://huggingface.co/Hirwa/ANPR/tree/main/ANPR_C58B10E20_YV5)
- First Model v2: [Model Link](https://huggingface.co/Hirwa/ANPR/tree/main/ANPR_C58B16E20_YV5)
- Fine-Tuned Model v1: [Model Link](https://huggingface.co/Hirwa/ANPR/tree/main/ANPR_C5B18E20_V1)
- Fine-Tuned Model v2: [Model Link](https://huggingface.co/Hirwa/ANPR/tree/main/ANPR_C5B8E10_V2)
- Freshly Trained Model v1: [Model Link](https://huggingface.co/Hirwa/ANPR/tree/main/ANPR_C5B8E10_V2)

---

## **Metrics Comparison**
| Attempt         | Dataset Classes | mAP  | Precision | Recall | Notes                                        |
|-----------------|-----------------|------|-----------|--------|----------------------------------------------|
| First Attempts  | 10+             | Low  | Low       | Low    | Poor dataset consistency, too many classes   |
| Second Attempts | 5               | High | High      | High   | Cleaner dataset, reduced classes             |
| Third Attempt   | 5               | High | High      | High   | Trained from scratch for baseline comparison |
---

## **Future Work**
1. Integrate actuators (e.g., gates or barriers) for real-world applications.
2. Experiment with other YOLO variants (e.g., YOLOv8) for further improvements.
3. Expand the dataset for broader generalization.

---

## **References**
1. YOLOv5 Repository: [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5)
2. LabelImg Tool: [LabelImg](https://github.com/tzutalin/labelImg)
3. Dataset Resources: [Dataset Resource Link](https://huggingface.co/datasets/Hirwa/Automatic_Number_Plate_Recognition)

---