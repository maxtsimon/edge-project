# edge-project
Real-Time Content Moderation for Firearms in Child Accessible Media

# Requirements
- Python Libraries
  
```
pip install ultralytics
pip install supervision
pip install opencv-python
```
- Google Chrome
- A Webcam

# Usage
1. Once all of the required libraries are installed, download main.py as well as the pre-trained yolov8s.pt model from this repo and put them in the same directory
2. Run main.py
3. Open up YouTube in a Google Chrome browser window and point the webcam at the screen
4. Enjoy watching YouTube with peace of mind that the program will prevent users from seeing any gun-related content
5. Hit the escape key with the CV2 window (webcam footage) open to terminate the program

# Sources
This project could not have been possible without the pre-trained YOLOv8 model publicly available in [this repository](https://github.com/macedoti13/Real-Time-Gun-Detection-YOLOv8?tab=readme-ov-file#conclusion) hosting the research materials of Thiago Macedo and Vitor Pires.

APA Citation: Macedo, T. de A., \& Fuentes Pires, V. F. (2023, June 26). Detecção em tempo real de armas de fogo em câmeras de segurança: uma comparação entre YOLOv5 e YOLOv8. Real-Time-Gun-Detection-YOLOv8. https://github.com/macedoti13/Real-Time-Gun-Detection-YOLOv8/tree/main
