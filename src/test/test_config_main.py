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
from pyk4a import Config, ColorResolution, ImageFormat, DepthMode
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
    BASE_DIR = os.path.abspath('../')
    path_log_file = os.path.join(BASE_DIR, 'log', 'recording_data.log')
    path_conf_file = os.path.join(BASE_DIR, 'ak_sm_recorder', 'conf', 'kinect_azure_settings.conf')
    path_video_output = os.path.join(BASE_DIR,  'ak_sm_recorder', 'recorded_video')
    logging.basicConfig(format='%(asctime)s %(message)s', filename=path_log_file, level=logging.INFO)
    logging.Formatter.converter = gmtime
    # ---------------
    my_device_configuration = hc.load_config_from_file(path_conf_file)
    # ---------------
    my_device_configuration.color_resolution = ColorResolution.RES_720P
    my_device_configuration.color_format = ImageFormat.COLOR_BGRA32
    # ---------------
    hc.save_config_in_file(path_conf_file, my_device_configuration)
    # ---------------

    pass

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

