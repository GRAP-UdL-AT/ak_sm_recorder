"""
Project: AK_SM_RECORDER Azure Kinect SM Recorder https://github.com/GRAP-UdL-AT/ak_sm_recorder

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: April 2022
Description:
    This is an wrapper to use Azure Kinect functions 3D point clouds as a thread process.
    This class is used when we need to launch process  from buttons
Use:
"""

"""
Project: Kinect Azure management
Author: Juan Carlos Miranda
Date: April 2022
Description:
This is an wrapper to use Azure Kinect functions 3D point clouds as a thread process
This class is used when we need to launch process  from loops as
a remote client or buttons

Use:
"""

import threading
import logging
import os
import pyk4a
import numpy as np
from pyk4a import Config, PyK4A
from pyk4a import ColorResolution, ImageFormat, DepthMode, FPS
from datetime import datetime


class JobThread3DAzure(threading.Thread):
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
        f_extension = ".xyz"
        f_name = resolutionp + "_" + date_string + f_extension
        f_path_name = os.path.join(self._f_path, f_name)
        logging.info(f"CREATING_FILE {f_path_name}")

        return f_path_name

    def run(self):
        """
        Adapted from example https://github.com/etiennedub/pyk4a/blob/master/example/viewer_point_cloud.py
        :return:
        """
        # open sensor
        self.initialize_sensor()
        print("Capturing 3D data")
        f_path_name = self.get_file_name()
        print("Capturing 3D data... Creating file.")
        # ------------------------------------------------
        # getters and setters directly get and set on device
        self._device.whitebalance = 4500
        assert self._device.whitebalance == 4500
        self._device.whitebalance = 4510
        assert self._device.whitebalance == 4510
        while True:
            capture = self._device.get_capture()
            if np.any(capture.depth) and np.any(capture.color):
                break
        while True:
            capture = self._device.get_capture()
            if np.any(capture.depth) and np.any(capture.color):
                break
        points_data = capture.depth_point_cloud.reshape((-1, 3))
        color_data = capture.transformed_color[..., (2, 1, 0)].reshape((-1, 3))
        point_cloud_3d = np.append(points_data, color_data, axis=1)
        np.savetxt(f_path_name, point_cloud_3d, delimiter=' ', fmt='%u')
        # ------------------------------------------------
        # print(f"{record.captures_count} frames written.")
        # ... Clean shutdown code here ...
        print(f'3D CAPTURING-STOPPED #{self.ident}')
        # logging.info(f'RECORDING-STOPPED #{self.ident}')
        # close sensor sensor
        self.finalize_sensor()
