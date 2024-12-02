import cv2
import os
from ultralytics import YOLO

# Load the YOLOv8n model
model = YOLO('..\\models\\yolov8n.pt')  # Ensure the model is in the correct path

# Function to detect vehicles and automatically save frames containing cars with high confidence
def capture_car_frames(video_path, output_dir, confidence_threshold=0.5, frame_skip=10):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open video file
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    saved_frame_count = 0

    # Get frames per second (FPS) to calculate the time per frame
    fps = cap.get(cv2.CAP_PROP_FPS)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # Skip frames based on the frame_skip parameter
        if frame_count % frame_skip != 0:
            continue

        # Calculate the current time in seconds
        current_time_sec = frame_count / fps
        minutes = int(current_time_sec // 60)
        seconds = int(current_time_sec % 60)

        # Display the timeline (minute:second) of the video
        print(f"Processing frame {frame_count}, Time: {minutes}m:{seconds}s")

        # Run YOLOv8 detection on the frame
        results = model(frame)

        # Filter detections for cars or vehicles with high confidence
        for result in results:
            # Get detected class IDs and confidence scores
            class_ids = result.boxes.cls.cpu().numpy()
            confidences = result.boxes.conf.cpu().numpy()

            # Check if any detection is a car or vehicle class with high confidence
            for cls_id, confidence in zip(class_ids, confidences):
                if cls_id in [2, 3, 5, 7] and confidence >= confidence_threshold:
                    saved_frame_count += 1

                    # Save the frame to the output directory
                    frame_filename = os.path.join(output_dir, f'frame_{saved_frame_count}.jpg')
                    cv2.imwrite(frame_filename, frame)
                    print(f"Saved: {frame_filename} (Confidence: {confidence})")
                    break  # Save only one frame per detection to avoid duplicates

        # Stop when all frames in the video are processed
        if frame_count >= cap.get(cv2.CAP_PROP_FRAME_COUNT):
            break

    cap.release()
    cv2.destroyAllWindows()

# Usage
video_path = 'footage/In-Transit-Vehicle-Plate-Captures-[001].mp4'  # Path to the video file
output_dir = 'output'  # Directory where car frames will be saved

# Set confidence threshold to 0.5 and capture 1 frame every 10 frames
capture_car_frames(video_path, output_dir, confidence_threshold=0.85, frame_skip=4)
