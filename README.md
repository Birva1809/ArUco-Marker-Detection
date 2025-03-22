# Authors 
 - **Birva Dave** | GitHub: [Birva1809](https://github.com/Birva1809)
 - **Brijraj Kacha** | GitHub: [BR-Kacha](https://github.com/BR-Kacha)

# ArUco Marker Detection

This project provides a Python script that uses OpenCV to detect ArUco markers in an image, identify their unique IDs, calculate their center coordinates, determine their orientation, and extract their corner points. This information is useful for robotics systems and other computer vision applications.

## What are ArUco Markers?

ArUco markers are black and white square patterns that are used in computer vision applications to easily detect and identify objects. Each marker has a unique ID, making it possible to distinguish between different markers. They are commonly used in robotics, augmented reality, and other fields that require precise location and orientation tracking.

## Features

- **Marker ID Detection**: Each marker has a unique ID that is identified and returned as an integer.
- **Center Coordinates Calculation**: The center (X, Y) coordinates of each marker are calculated and returned as a list of integers.
- **Orientation Calculation**: The orientation of each marker with respect to the vertical axis is determined and returned as an integer angle.
- **Corner Points Extraction**: The corner points of each marker are extracted and stored in a dictionary for further processing or plotting.

## Requirements

- Python 3.x
- OpenCV (`cv2`)

