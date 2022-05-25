"""
Project: AK_SM_RECORDER Azure Kinect SM Recorder https://github.com/GRAP-UdL-AT/ak_sm_recorder

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: August 2021
Description:
    Remote Management Console, this sends commands to the central server. It offers a basic interface
    to manage the acquisition system.
Use:

    python ak_sm_recorder.py
"""

# import locale
# import gettext
# import os
# import logging
# import helpers.helper_load_config as hc
import os
from os.path import expanduser
import sys
sys.path.append(os.path.join(os.path.abspath('.'), 'src'))



from gui_single_mode.gui_ak_single_config import GUIKASingleModeConfig
from gui_single_mode.gui_classes import GUIKASingleMode
from helpers.helper_filesystem import *

if __name__ == '__main__':
    # current_locale, encoding = locale.getdefaultlocale()
    # LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))
    # locale_path = os.path.join(LOCAL_PATH, 'locale')
    # language = gettext.translation('gui_classes', locale_path, ['en_US']) # todo: change gui_classes to gui_single_mode
    # language.install()

    BASE_DIR = os.path.abspath('.')
    path_log_file = os.path.join(BASE_DIR, 'log', 'gui_ka_single_mode.log')
    path_conf_file = os.path.join(BASE_DIR, 'conf', 'kinect_azure_settings.conf')
    path_gui_conf_file = os.path.join(BASE_DIR, 'conf', 'gui_ka_single_mode.conf')
    path_video_output = os.path.join(BASE_DIR, 'recorded_video')  # todo: correct this must be in default
    user_path = expanduser("~")

    current_main_path_str = __file__
    package_path = os.path.dirname(os.path.normpath(current_main_path_str))
    package_path_config_files = os.path.join(package_path, 'conf')
    path_user_config_files = os.path.join(BASE_DIR, 'conf')

    print('BASE_DIR->', BASE_DIR)
    print('user_path->', user_path)
    print('saved_str', current_main_path_str)
    print('package_path', package_path)
    print('path_gui_conf_file->', path_gui_conf_file)
    print('path_user_config_files->', path_user_config_files)

    # if directory doen't exist, then create
    if os.path.exists(path_user_config_files):
        print('Directory exist!!!', path_user_config_files)
    else:
        print('Directory doesnt exist!!!', path_user_config_files)
        print('Creating directory ', path_user_config_files)
        os.mkdir(path_user_config_files)
        copy_folder(package_path_config_files, path_user_config_files)

    # -------------------------
    gui_config_obj = GUIKASingleModeConfig(path_gui_conf_file)
    gui_config_obj.file_browser_input_folder = path_video_output
    gui_config_obj.path_conf_file = path_conf_file
    app = GUIKASingleMode(gui_config_obj)
    app.mainloop()
    # -------------------------

    # INTERNATIONALIZATION
    # base file for translation is located in /base/
    # Use xgettext https://www.gnu.org/software/gettext/manual/html_node/xgettext-Invocation.html
    # xgettext -d gui_single_mode -o locale/gui_single_mode.pot gui_single_mode/gui_single_mode.py
