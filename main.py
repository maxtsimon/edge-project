import cv2

from ultralytics import YOLO

import supervision as sv

import pyautogui

import webbrowser

import time

import os

# https://www.youtube.com/watch?v=eq3vD93GgLs
# https://www.youtube.com/watch?v=Aw2qISZgA3c


# https://www.youtube.com/watch?v=-K8ZDhaPXpg

def main():
    
    cap = cv2.VideoCapture(0)

    # dog example
    # model = YOLO("yolov8n.pt")

    # comment out model declaration below for dog example
    model = YOLO("yolov8s.pt")

    box_annotator = sv.BoundingBoxAnnotator()
    label_annotaor = sv.LabelAnnotator()

    confidence_threshold = 0.65

    detection_time = None  # Initialize variable to store detection time

    while True:
            ret, frame = cap.read()

            result = model(frame, verbose=False)[0]
            detections = sv.Detections.from_ultralytics(result)

            labels = [
                f"{model.model.names[class_id]} {confidence:0.2f}"
                for class_id, confidence in zip(detections.class_id, detections.confidence)
            ]

            for class_id, confidence in zip(detections.class_id, detections.confidence):
                
                # dog example
                # if confidence >= confidence_threshold and class_id == 16:

                # comment out if statment below for dog example
                if confidence >= confidence_threshold and class_id == 2:

                    if detection_time is None:  # Record detection time only once
                        detection_time = time.time()

                    # pyautogui.hotkey('alt', 'f4')
                    os.system("taskkill /im chrome.exe /f")
                    webbrowser.open("https://www.youtube.com/watch?v=UpgM_8_2Hus")
                    return detection_time


            frame = box_annotator.annotate(scene=frame, detections=detections)
            frame = label_annotaor.annotate(scene=frame, detections=detections, labels=labels)

            cv2.imshow("yolov8", frame)

            if (cv2.waitKey(30) == 27):
                break

if __name__ == "__main__":
    detection_time = main()
    if detection_time is not None:
        exit_time = time.time()
        detection_exit_duration = exit_time - detection_time
        print(f"Time between detection and exit: {detection_exit_duration} seconds")