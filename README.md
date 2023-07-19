# ros-camera-calib
Camera calibration from rosbag file to camera matrix, distortion coefficent, rotation vectors, and translation vectors. 

## How To
1. Create `imgs` and `final_imgs` folders
2. Change file paths and bag names in `bag2png.py`
3. Run `bag2png.py`
4. Pick the images you want to use from the `imgs` folder and move them to the `final_imgs` folder
5. Change the dimensions of the checkerboard (count the inner corners) and the file extension in `camcalib.py`
6. Run `camcalib.py`

## Resources
[OpenCV](https://www.geeksforgeeks.org/camera-calibration-with-python-opencv/#)

[https://idorobotics.com/2021/03/08/extracting-ros-bag-files-to-python/](https://idorobotics.com/2021/03/08/extracting-ros-bag-files-to-python/)
