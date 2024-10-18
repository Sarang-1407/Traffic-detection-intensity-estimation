# Traffic-detection-intensity-estimation
 This repository contains a Real-time system for detecting vehicles and estimating traffic intensity using YOLOv8 algorithm

## Contents

- `yolo_vehicle_detection.pynb`: Jupyter Notebook implementing the YOLO vehicle detection model.
- `QuadMarker.py`: A script for drawing quadrilaterals on images and video frames.
- `Vehicle_Detection_Image_Dataset/`: Directory containing the training and validation dataset in YOLO format (images and labels) along with a `data.yaml` configuration file.
- Sample images and videos used for testing.

## Requirements

Make sure to install the required packages before running the scripts. You can create a virtual environment and install dependencies using the following command:

```bash
pip install opencv-python numpy
```

## Usage

### Quadrilateral Marking

1. **Run the QuadMarker script**: This script allows you to mark quadrilaterals on images or video frames.

   ```bash
   python QuadMarker.py
   ```

2. **Interactivity**: Click on the image/video to mark points. Once you have selected four points, a quadrilateral will be drawn. The coordinates of the quadrilaterals will be printed to the console.

3. **Exiting the tool**: Press 'q' to quit the marking tool once you have drawn the desired quadrilaterals.

### YOLO Vehicle Detection

1. **Open the Jupyter Notebook**: Launch `yolo_vehicle_detection.pynb` in Jupyter Notebook to start the vehicle detection process.

2. **Configuration**: Make sure to configure the paths to your dataset in the `data.yaml` file according to your setup.

3. **Running the Notebook**: Execute the cells step by step to train and test the YOLO model on the dataset provided.

## Dataset

The dataset used in this project is formatted for YOLO training and validation, containing images and corresponding label files. It has been sourced from Roboflow, and it includes sample images and videos for testing the detection model.

## Notes

- Ensure that the OpenCV and NumPy libraries are installed to use the quadrilateral marking functionality and for video processing.
- For optimal performance, use a machine with a capable GPU when training the YOLO model.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- YOLO authors and contributors.
- Roboflow for providing the dataset.
