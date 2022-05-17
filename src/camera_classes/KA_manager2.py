"""
Project:
Author: Juan Carlos Miranda
Date:
Description: Manager of Azure Kinect Sensor
This is an examples adapted from:
 * https://github.com/UnaNancyOwen/AzureKinectSample/blob/master/sample/python/color.py
 * https://github.com/etiennedub/pyk4a/blob/master/example/

This is a first approach based on examples from the above urls adn modified from KA_manager1.py
This has simplified methods and it is used in
stand alone recording app.


  Configure sensor
  Take a capture with all cameras
  Show each camera results
  Show config data of one sensor
# todo: add descriptions
Use:
"""
import numpy as np
import cv2 as cv
import logging
import os
import pyk4a
from pyk4a import Config, ImageFormat, PyK4A, PyK4ARecord
from datetime import datetime


class KAManager2:
    # Kinect device
    my_device = None
    _capture = None
    device_config = None
    _f_path = None

    # IR
    _infrared_show = None
    # Depth
    _depth_show = None
    # Depth
    _rgb_show = None

    def __init__(self, device_config=None, f_path_output=None):
        if device_config is None:
            logging.debug("Default config loaded")
            # Load config by default
            self.device_config = Config(
                color_resolution=pyk4a.ColorResolution.RES_720P,
                color_format=pyk4a.ImageFormat.COLOR_BGRA32,
                depth_mode=pyk4a.DepthMode.NFOV_UNBINNED,
                camera_fps=pyk4a.FPS.FPS_30,
                synchronized_images_only=True,
                depth_delay_off_color_usec=0,
                wired_sync_mode=pyk4a.WiredSyncMode.STANDALONE,
                subordinate_delay_off_master_usec=0,
                disable_streaming_indicator=False
            )
            # todo: when we take a picture use BGRA32, WHEN WE RECORD DATA USE MPG
        else:
            logging.debug('External config loaded')
            self.device_config = device_config

        self._f_path = f_path_output
        # logging.debug("__init__(self): - Initialize loading Azure Manager")

    def __del__(self):
        logging.debug("__del__(self): - Finalize Azure Manager")
        self.finalize_sensor()

    def set_config_default(self):
        # todo: create configuration decoupled in object format
        device_config = Config()
        device_config.color_resolution = pyk4a.ColorResolution.OFF
        device_config.depth_mode = pyk4a.DepthMode.NFOV_UNBINNED
        device_config.synchronized_images_only = True
        self.device_config = device_config

    def initialize_sensor(self):
        logging.debug("Initialize_sensor()")
        self.my_device = PyK4A(self.device_config)
        self.my_device.start()

    def finalize_sensor(self):
        logging.debug("finalize_sensor()")
        self.my_device.stop()
        #self.my_device.close()
        pass

    def get_file_name(self):
        print("Recording data")
        resolution_p = "_"
        if self.device_config.color_resolution == pyk4a.ColorResolution.RES_720P:
            resolution_p = "1080"
        if self.device_config.color_resolution == pyk4a.ColorResolution.RES_1080P:
            resolution_p = "1080"
        if self.device_config.color_resolution == pyk4a.ColorResolution.RES_1440P:
            resolution_p = "1440"
        if self.device_config.color_resolution == pyk4a.ColorResolution.RES_1536P:
            resolution_p = "1536"
        if self.device_config.color_resolution == pyk4a.ColorResolution.RES_2160P:
            resolution_p = "2160P"
        if self.device_config.color_resolution == pyk4a.ColorResolution.RES_3072P:
            resolution_p = "3072P"

        now = datetime.now()
        date_string = now.strftime("%d%m%Y%H%M%S")
        f_extension = ".mkv"
        f_name = resolution_p + "_" + date_string + f_extension
        f_path_name = os.path.join(self._f_path, f_name)
        logging.info(f"Recording... Creating file. {self._f_path}")

        return f_path_name

    def recording(self):
        self.initialize_sensor()
        print("Recording data")
        f_path_name = self.get_file_name()
        print("Recording... Creating file.")
        record = PyK4ARecord(device=self.my_device, config=self.device_config, path=f_path_name)
        record.create()
        #####################
        # RECORD loop
        #####################
        try:
            print("Recording... Press CTRL-C to stop recording.")
            while True:
                self._capture = self.my_device.get_capture()
                record.write_capture(self._capture)
        except KeyboardInterrupt:
            print("CTRL-C pressed. Exiting.")
        #####################
        record.flush()
        record.close()
        print(f"{record.captures_count} frames written.")
        self.finalize_sensor()

    def update_capture_frame(self):
        # Capture Frame
        self._capture = self.my_device.get_capture()
        if self._capture is None:
            raise IOError("failed get capture!")

    def draw(self):
        self.draw_infrared()
        self.draw_depth()
        self.draw_rgb()

    def draw_infrared(self):
        # Draw Infrared
        self._infrared_show = self._capture.ir

    def draw_depth(self):
        # Draw Infrared
        self._depth_show = self._capture.depth

    def draw_rgb(self):
        # Draw rgb
        self._rgb_show = self._capture.color

    def show(self):
        self.show_infrared()
        self.show_depth()
        self.show_rgb()

    def show_infrared(self):
        # Scaling Infrared
        # self._infrared_show = self._infrared_show * 0.5
        self._infrared_show = self._infrared_show.astype(np.uint8)
        cv.imshow("Infrared", self._infrared_show)

    def show_depth(self):
        # Scaling depth
        self._depth_show = self._depth_show.astype(np.uint8)
        cv.imshow("Depth", self._depth_show)

    def show_rgb(self):
        cv.imshow("RGB", self._rgb_show)

    def run_real_time(self):
        self.initialize_sensor()
        while True:
            self.update_capture_frame()
            self.draw()
            self.show()

            key = cv.waitKey(10)
            if key == ord('q'):
                cv.destroyAllWindows()
                break
        self.finalize_sensor()

    def show_a_capture(self):
        # todo: a problem with configuratoni mode in BGRA, may be variable assignment
        self.initialize_sensor()
        temporal = self.device_config.color_format
        self.device_config.color_format = ImageFormat.COLOR_BGRA32
        self.update_capture_frame()
        self.draw()
        self.show()
        key = cv.waitKey(10)
        self.device_config.color_format = temporal
        self.finalize_sensor()

    def get_a_capture(self):
        self.initialize_sensor()
        temporal = self.device_config.color_format
        self.device_config.color_format = ImageFormat.COLOR_BGRA32
        self.update_capture_frame()
        self.device_config.color_format = temporal
        self.finalize_sensor()
        return self._capture
