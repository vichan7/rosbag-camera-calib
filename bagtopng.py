import rosbag
import cv2
from cv_bridge import CvBridge
import numpy as np


FILENAME = 'rc3_camcalib_front'
ROOT_DIR = '/home/mmpug/cam_calib'
BAGFILE = ROOT_DIR + '/' + FILENAME + '.bag'

if __name__ == '__main__':
    bag = rosbag.Bag(BAGFILE)
    TOPIC = '/basestation/cmu_rc3/front/image_raw'
    image_topic = bag.read_messages(TOPIC)
    for k, b in enumerate(image_topic):
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(b.message, b.message.encoding)
        cv_image.astype(np.uint8)      
        if not cv2.imwrite(ROOT_DIR + '/imgs/' + str(b.timestamp) + '.png', cv_image):
            raise Exception("Could not write image")
        print('saved: ' + str(b.timestamp) + '.png')


    bag.close()

    print('PROCESS COMPLETE')