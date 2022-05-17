"""
Project: Kinect Azure management
Author: Juan Carlos Miranda
Date: August 2021
Description:
Example of testing Azure Kinect functions as a thread process

Use:
python test_main_threads_azure.py
"""

"""
Run an example ot threads
python main_threads_Azure.py
"""
import logging
import os
import time
import src.helpers.helper_path as hp
hp.kinect()
import src.helpers.helper_load_config as hc
from src.camera_classes.job_thread_azure import JobThreadAzure
from time import gmtime

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

if __name__ == '__main__':
    BASE_DIR = os.path.abspath('.')
    path_log_file = os.path.join(BASE_DIR, 'log', 'threadlogger.log')
    path_conf_file = os.path.join(BASE_DIR, 'conf', 'kinect_azure_settings.conf')
    path_video_output = os.path.join(BASE_DIR, 'recorded_video',)
    logging.basicConfig(format='%(asctime)s %(message)s', filename=path_log_file, level=logging.INFO)
    logging.Formatter.converter = gmtime

    my_device_configuration = hc.load_config_from_file(path_conf_file)

    try:
        print('Running functions from threads --> ')
        job_ka_camera = JobThreadAzure(my_device_configuration, path_video_output)
        job_ka_camera.start()
        print('Waiting 5 seconds and recording data--> ')
        time.sleep(4)
        job_ka_camera.shutdown_flag.set()
        job_ka_camera.join()
        print('Video saved in --> ', path_video_output)

    except ServiceExit:
        print('ServiceExit Exception --> ')
        print('CATCHING any Exception HERE!-->')
        job_ka_camera.shutdown_flag.set()
        job_ka_camera.join()