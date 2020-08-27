# Covid-Social-Distancing
Detecting social distancing in OpenCV using YOLO Object Detector v4.

This repository contains code for giving a video input to the file social_distance_detector.py which generates an output file.

### The file structure for the repository is as follows:
```

    .
    ├── image_processing                   # This folder contains the files for config and person detection
    ├── yolov4                             # weights used from the YOLO github repo (https://github.com/pjreddie/darknet)
    ├── .gitattributes                     # attributes to push large file size using git LFS
    ├── coco.names                         # Names of object from Microsoft COCO dataset (https://cocodataset.org/#home)
    ├── distance_detector.py               # Main file that compiles and runs for object detection
    ├── LICENSE                            # Default license added
    └── README.md                          # Description of the repository
    
```

### Usage
To run the code use distance_detector.py  <video_file>
