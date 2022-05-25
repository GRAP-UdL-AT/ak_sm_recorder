"""
Project: AK_SM_RECORDER Azure Kinect SM Recorder https://github.com/GRAP-UdL-AT/ak_sm_recorder

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:
    This is an wraper to use Azure Kinect functions as a thread process
    This class is used when we need to launch process  from buttons

Use:

"""


import threading
import logging
import os
import helpers.helper_path as hp
# hp.kinect()
import pyk4a
import numpy as np
from pyk4a import Config, PyK4A, PyK4ARecord
from pyk4a import ColorResolution, ImageFormat, DepthMode, FPS
from datetime import datetime


class JobThreadAzure(threading.Thread):
    # Kinect device
    _device = None
    _capture = None
    device_config = None
    _f_path = None
    _mode_of_use = None

    # IR
    _infrared_show = None
    # Depth
    _depth_show = None
    # Depth
    _rgb_show = None

    def __init__(self, device_config=None, f_path_output=None):
        print('__INIT__')
        if device_config is None:
            logging.debug("Default conf loaded")
            # Load conf by default
            self.device_config = Config(
                color_resolution=ColorResolution.RES_720P,
                color_format=ImageFormat.COLOR_BGRA32,
                depth_mode=DepthMode.NFOV_UNBINNED,
                camera_fps=FPS.FPS_30,
                synchronized_images_only=True,
                depth_delay_off_color_usec=0,
                wired_sync_mode=pyk4a.WiredSyncMode.STANDALONE,
                subordinate_delay_off_master_usec=0,
                disable_streaming_indicator=False
            )
        else:
            logging.debug('External conf loaded')
            self.device_config = device_config

        if f_path_output is None:
            logging.debug("Default f_path_output loaded")
            BASE_DIR = os.path.abspath('.')
            self.f_path = os.path.join(BASE_DIR, 'recorded_video')
        else:
            self._f_path = f_path_output

        threading.Thread.__init__(self)
        self.shutdown_flag = threading.Event()

    def __del__(self):
        print('__DEL__')
        # logging.debug("__del__(self): - Finalize Azure Manager")
        # self.finalize_sensor()

    def initialize_sensor(self):
        logging.debug("Initialize_sensor()")
        self._device = PyK4A(self.device_config)
        self._device.start()

    def finalize_sensor(self):
        logging.debug("finalize_sensor()")
        self._device.stop()

    def get_file_name(self):
        print("Recording data")
        resolutionp = "_"
        resolutionp = self.device_config.color_resolution.name

        if (self.device_config.color_resolution == pyk4a.ColorResolution.RES_720P):
            resolutionp = "1080"
        if (self.device_config.color_resolution == pyk4a.ColorResolution.RES_1080P):
            resolutionp = "1080"
        if (self.device_config.color_resolution == pyk4a.ColorResolution.RES_1440P):
            resolutionp = "1440"
        if (self.device_config.color_resolution == pyk4a.ColorResolution.RES_1536P):
            resolutionp = "1536"
        if (self.device_config.color_resolution == pyk4a.ColorResolution.RES_2160P):
            resolutionp = "2160P"
        if (self.device_config.color_resolution == pyk4a.ColorResolution.RES_3072P):
            resolutionp = "3072P"

        now = datetime.now()
        date_string = now.strftime("%d%m%Y%H%M%S")
        f_extension = ".mkv"
        f_name = resolutionp + "_" + date_string + f_extension
        f_path_name = os.path.join(self._f_path, f_name)
        logging.info(f"CREATING_FILE {f_path_name}")

        return f_path_name

    def run(self):
        # open sensor
        self.initialize_sensor()
        print("Recording data")
        f_path_name = self.get_file_name()
        print("Recording... Creating file.")
        record = PyK4ARecord(device=self._device, config=self.device_config, path=f_path_name)
        record.create()
        #####################
        # RECORD loop
        #####################
        try:
            print('RECORDING-STARTED #%s' % self.ident)
            logging.info(f'RECORDING-STARTED #{self.ident}')
            while not self.shutdown_flag.is_set():
                self._capture = self._device.get_capture()
                record.write_capture(self._capture)
        except Exception:
            print("An exception occurred")
        #####################
        record.flush()
        record.close()
        print(f"{record.captures_count} frames written.")
        # ... Clean shutdown code here ...
        print(f'RECORDING-STOPPED #{self.ident}')
        logging.info(f'RECORDING-STOPPED #{self.ident}')
        # close sensor sensor
        self.finalize_sensor()
