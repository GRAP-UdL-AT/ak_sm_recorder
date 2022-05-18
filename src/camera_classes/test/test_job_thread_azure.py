"""
Project: Azure Kinect management
Author: Juan Carlos Miranda
Date: May 2022
Description:
Example of testing Azure Kinect functions as a thread process

Usage:
python -m unittest $HOME/development/ak_sm_recorded/src/camera_classes/test_job_thread_azure.py

"""
import unittest
import os
import time
import helpers.helper_load_config as hc
from camera_classes.job_thread_azure import JobThreadAzure


class ServiceExit(Exception):
    """
    Custom exception which is used to trigger the clean exit
    of all running threads and the main program.
    """
    print('Service Exit --> \r')
    pass


def service_shutdown(signum, frame):
    print('Service shut down --> Caught signal %d' % signum)
    raise ServiceExit


class TestJobThreadAzure(unittest.TestCase):
    def setUp(self):
        self.root_folder = os.path.abspath('')
        self.path_conf_file = os.path.join(self.root_folder, 'test_conf', 'test_kinect_azure_settings.conf')
        self.path_video_output = os.path.join(self.root_folder, 'test_recorded_video', )
        self.my_device_configuration = hc.load_config_from_file(self.path_conf_file)
        pass

    def test_launch_thread_azure(self):
        # ----------------
        try:
            print('Running functions from threads --> ')
            job_ka_camera = JobThreadAzure(self.my_device_configuration, self.path_video_output)
            job_ka_camera.start()
            print('Waiting 5 seconds and recording data--> ')
            time.sleep(4)
            job_ka_camera.shutdown_flag.set()
            job_ka_camera.join()
            print('Video saved in --> ', self.path_video_output)
            flag_exist_video_list = os.listdir(self.path_video_output)
            if flag_exist_video_list is not None:
                flag_video_created = True
            # cleaning all .mkv files
            for a_filename in os.listdir(self.path_video_output):
                if a_filename.endswith('.mkv'):
                    print(a_filename)
                    os.remove(os.path.join(self.path_video_output, a_filename))
        # ----------------
        except ServiceExit:
            print('ServiceExit Exception --> ')
            print('CATCHING any Exception HERE!-->')
            job_ka_camera.shutdown_flag.set()
            job_ka_camera.join()
        # ----------------
        self.assertEqual(True, flag_video_created)
