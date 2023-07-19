# rosbag-camera-calib
Camera calibration from rosbag file to camera matrix, distortion coefficent, rotation vectors, and translation vectors.

## Contents
* [How To](https://github.com/vichan7/ros-camera-calib/blob/main/README.md#how-to)  
* [Example (using CMU MMPUG Project)](https://github.com/vichan7/ros-camera-calib/blob/main/README.md#example)  
* [Sample Chessboard](https://github.com/vichan7/ros-camera-calib/edit/main/README.md#sample-chessboard)  
* [Resources](https://github.com/vichan7/ros-camera-calib/blob/main/README.md#resources)

## How To
1. Record rosbags of the calibration chessboard in front of your camera at various angles
2. Add your rosbags to the repo folder
3. Create `imgs` folder
4. Change file paths and bag names in `bagtopng.py`
5. Run `bagtopng.py` (fills `imgs` with pictures)
7. Change the dimensions of the checkerboard (count the inner corners), the number of images you want to use, and the file extension of your images in `camcalib.py`
8. Run `camcalib.py`

## Example
### Recording rosbags
### Running `bagtopng.py`
### Running `camcalib.py`

## Sample Chessboard
![IMG_6598](https://github.com/vichan7/ros-camera-calib/assets/117228381/1e17886e-89ec-46f8-af90-678717c69ad5)
(9x6 inner corners)

## Resources
[OpenCV](https://www.geeksforgeeks.org/camera-calibration-with-python-opencv/#)

[https://idorobotics.com/2021/03/08/extracting-ros-bag-files-to-python/](https://idorobotics.com/2021/03/08/extracting-ros-bag-files-to-python/)

