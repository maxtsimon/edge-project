import cv2

from ultralytics import YOLO

import supervision as sv

import webbrowser

import time

import os


def main():
    
    cap = cv2.VideoCapture(0)

    model = YOLO("yolov8s.pt")

    box_annotator = sv.BoundingBoxAnnotator()
    label_annotaor = sv.LabelAnnotator()

    confidence_threshold = 0.65

    detection_time = None  

    while True:
            ret, frame = cap.read()

            result = model(frame, verbose=False)[0]
            detections = sv.Detections.from_ultralytics(result)

            labels = [
                f"{model.model.names[class_id]} {confidence:0.2f}"
                for class_id, confidence in zip(detections.class_id, detections.confidence)
            ]

            for class_id, confidence in zip(detections.class_id, detections.confidence):
                
                if confidence >= confidence_threshold and class_id == 2:

                    if detection_time is None: 
                        detection_time = time.time()

                    # comment out the second os line if using Windows, comment out the first os line if using Mac
                    os.system("taskkill /im chrome.exe /f")
                    # os.system("killall -9 'Google Chrome'")
                    webbrowser.open("https://www.youtube.com/watch?v=UpgM_8_2Hus")
                    return detection_time


            frame = box_annotator.annotate(scene=frame, detections=detections)
            frame = label_annotaor.annotate(scene=frame, detections=detections, labels=labels)

            cv2.imshow("yolov8", frame)

            if (cv2.waitKey(30) == 27):
                break

    return detection_time

if __name__ == "__main__":
    detection_time = main()
    if detection_time is not None:
        exit_time = time.time()
        detection_exit_duration = exit_time - detection_time
        print(f"Time between detection and exit: {detection_exit_duration} seconds")
