SmileCapture: 
A Real-Time Selfie Application using MediaPipe and OpenCV
This project automatically captures an image when the user smiles. It utilizes Google's MediaPipe library for face detection and landmark tracking, specifically focusing on eyebrow movements to detect a smile. The application displays a live camera feed, and when the distance between the outer edges of the eyebrows exceeds a threshold, indicating a smile, it takes a picture and plays a shutter sound.


Technologies Used:
-OpenCV: A powerful open-source computer vision library used for capturing and processing camera frames.
-MediaPipe: A cross-platform, customizable machine learning library developed by Google, utilized here for face detection and landmark tracking.
-winsound: A simple Python library used to play the shutter sound when a photo is taken.

Limitations:
-The current implementation focuses only on the distance between eyebrow landmarks to detect a smile, which may not work accurately for all users or scenarios.
-Performance may vary depending on the user's system resources and camera capabilities.
-It also assumes the user is not too far or not too close to the camera.

