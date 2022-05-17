"""
Project: Fruit Size Estimation
Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:
    Remote Management Console, this sends commands to the central server. It offers a basic interface
    to manage the acquisition system.
Use:

    python ka_single_mode_project.py

"""
import locale
import gettext
import os
import logging
import src.helpers.helper_load_config as hc
from gui_single_mode.gui_ka_single_config import GUIKASingleModeConfig
from gui_single_mode.gui_classes import GUIKASingleMode
from camera_classes.KA_manager2 import KAManager2



if __name__ == '__main__':
    #current_locale, encoding = locale.getdefaultlocale()
    #LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))
    #locale_path = os.path.join(LOCAL_PATH, 'src', 'locale')
    #language = gettext.translation('gui_classes', locale_path, ['en_US']) # todo: change gui_classes to gui_single_mode
    #language.install()

    BASE_DIR = os.path.abspath('.')
    path_log_file = os.path.join(BASE_DIR, 'src', 'log', 'gui_ka_single_mode.log')
    path_conf_file = os.path.join(BASE_DIR,  'src', 'conf', 'kinect_azure_settings.conf')
    path_gui_conf_file = os.path.join(BASE_DIR,  'src', 'conf', 'gui_ka_single_mode.conf')
    path_video_output = os.path.join(BASE_DIR, 'recorded_video') # todo: correct this must be in default


    my_device_configuration = hc.load_config_from_file(path_conf_file)
    my_ka_manager1 = KAManager2(my_device_configuration, path_video_output)

    gui_config_obj = GUIKASingleModeConfig(path_gui_conf_file)
    gui_config_obj.file_browser_input_folder = path_video_output
    app = GUIKASingleMode(gui_config_obj, my_device_configuration, my_ka_manager1)
    app.mainloop()

    # INTERNATIONALIZATION
    # base file for translation is located in /base/
    # Use xgettext https://www.gnu.org/software/gettext/manual/html_node/xgettext-Invocation.html
    # xgettext -d gui_single_mode -o locale/gui_single_mode.pot gui_single_mode/gui_single_mode.py