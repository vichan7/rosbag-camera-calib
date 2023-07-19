# ros-camera-calib
Camera calibration from rosbag file to camera matrix, distortion coefficent, rotation vectors, and translation vectors. 

## How To
1. Add your rosbags to the repo folder
2. Create `imgs` and `final_imgs` folders
3. Change file paths and bag names in `bagtopng.py`
4. Run `bagtopng.py`
5. Pick the images you want to use from the `imgs` folder and move them to the `final_imgs` folder
6. Change the dimensions of the checkerboard (count the inner corners) and the file extension in `camcalib.py`
7. Run `camcalib.py`

## Sample Chessboard
![IMG_6598](https://github.com/vichan7/ros-camera-calib/assets/117228381/1e17886e-89ec-46f8-af90-678717c69ad5)
(9x6)

## Resources
[OpenCV](https://www.geeksforgeeks.org/camera-calibration-with-python-opencv/#)

[https://idorobotics.com/2021/03/08/extracting-ros-bag-files-to-python/](https://idorobotics.com/2021/03/08/extracting-ros-bag-files-to-python/)

