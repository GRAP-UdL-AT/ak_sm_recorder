"""
Project:
Author: Juan Carlos Miranda
Date: July 2021
Description:
 Example showing real time data obtained from Azure Kinect

Use:
"""
import logging
import os
import cv2 as cv
import helpers.helper_path as hp
from pyk4a import ImageFormat
from camera_classes.KA_manager2 import KAManager2
import helpers.helper_load_config as hc
from time import gmtime

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # ---------------------------------------
    # My config TESTING
    # 1080P, NFOV UNBINNED, 15 FPS, COLOR BGRA
    # ---------------------------------------
    # https://docs.microsoft.com/es-es/azure/kinect-dk/hardware-specification
    BASE_DIR = os.path.abspath('.')
    path_log_file = os.path.join(BASE_DIR, 'log', 'recording_data.log')
    path_conf_file = os.path.join(BASE_DIR, 'conf', 'kinect_azure_settings.conf')
    path_video_output = os.path.join(BASE_DIR, 'recorded_video')
    logging.basicConfig(format='%(asctime)s %(message)s', filename=path_log_file, level=logging.INFO)
    logging.Formatter.converter = gmtime

    my_device_configuration = hc.load_config_from_file(path_conf_file)
    my_device_configuration.color_format = ImageFormat.COLOR_BGRA32
    my_ka_manager = KAManager2(my_device_configuration, path_video_output)
    capture_data = my_ka_manager.get_a_capture()
    print('Taking a capture and getting results from library ->')
    print('Press any key to continue over image windows...')
    cv.imshow("RGB-from Manager Libray", capture_data.color)
    key = cv.waitKey()
    print('Press any key to continue ...')
    # run real time data in a window
    print('Now showing in real time ->')
    my_ka_manager.run_real_time()
    print('Press any key to continue over image windows ...')

# ---------------------------------------

# -------------------
# ALGORITHM
# -------------------
# get data from command line
# configure data in sensor
# load data from sensor
# save in file
# activate IMU data


# save IMU DATA
# save data for x seconds
# SAVE DATA AND RETURN IN REAL TIME
# GET IMU DATA AND SAVE IN mATROSKA

