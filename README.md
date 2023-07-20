# rosbag-camera-calib
Camera calibration from rosbag file to camera matrix, distortion coefficent, rotation vectors, and translation vectors.

## Contents
* [How To](https://github.com/vichan7/ros-camera-calib/blob/main/README.md#how-to)  
* [Recording Rosbags](https://github.com/vichan7/rosbag-camera-calib/edit/main/README.md#recording-rosbags)  
* [Results](https://github.com/vichan7/rosbag-camera-calib/edit/main/README.md#result)  
* [Resources](https://github.com/vichan7/ros-camera-calib/blob/main/README.md#resources)

## How To
1. Record rosbags of the calibration chessboard in front of your camera at various angles
2. Add your rosbags to the repo folder
3. Create `imgs` folder
4. Change file paths and bag names in `bagtopng.py`
5. Run `bagtopng.py` (fills `imgs` with `.png`s)
7. Change the dimensions of the checkerboard (count the inner corners) and the number of images you want to use in `camcalib.py`
8. Run `camcalib.py`

## Recording Rosbags
The checkerboard was attached to a flat, mobile surface and moved around in front of the camera to capture various orientations (tilting, side-to-side, etc.) of the checkerboard. Here are some examples of our captured orientations.  
<img src="https://github.com/vichan7/rosbag-camera-calib/assets/100101338/61eaff56-ae23-4e24-8981-7ea271bf4e1d" width="200" height="200">
<img src="https://github.com/vichan7/rosbag-camera-calib/assets/100101338/64af1d47-82b8-47f3-97f1-3be257a770fc" width="200" height="200">
<img src="https://github.com/vichan7/rosbag-camera-calib/assets/100101338/7b91d423-8783-447d-a3a3-544e928ed029" width="150" height="200">

## Results
The last step should produce a camera matrix, distortion coefficient, rotation vectors, and translation vectors.  
![Screenshot from 2023-07-19 17-55-57](https://github.com/vichan7/rosbag-camera-calib/assets/100101338/8bda46f3-79bf-4746-91f4-25f8cd7c7551)
![Screenshot from 2023-07-19 17-56-03](https://github.com/vichan7/rosbag-camera-calib/assets/100101338/168680b6-cda5-4f5f-8825-2ad8c0d37ad0)



## Sample Chessboard
![IMG_6598](https://github.com/vichan7/ros-camera-calib/assets/117228381/1e17886e-89ec-46f8-af90-678717c69ad5)
(9x6 inner corners)

## Resources
[OpenCV](https://www.geeksforgeeks.org/camera-calibration-with-python-opencv/#)

[https://idorobotics.com/2021/03/08/extracting-ros-bag-files-to-python/](https://idorobotics.com/2021/03/08/extracting-ros-bag-files-to-python/)

