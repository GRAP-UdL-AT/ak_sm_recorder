"""
Project: AK_SM_RECORDER Azure Kinect SM Recorder https://github.com/GRAP-UdL-AT/ak_sm_recorder

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: April 2022
Description:

Use:
    python __main__.py
"""
import os
import sys
sys.path.append(os.path.join(os.path.abspath('.'), 'src'))
from os.path import expanduser

from gui_single_mode.gui_ak_single_config import GUIKASingleModeConfig
from gui_single_mode.gui_classes import GUIKASingleMode
from helpers.helper_filesystem import *

if __name__ == '__main__':
    user_path = expanduser("~")
    BASE_DIR = os.path.abspath('.')  # it gives the current location

    current_main_path_str = __file__
    package_path = os.path.join(os.path.dirname(os.path.normpath(current_main_path_str)), 'ak_sm_recorder')
    # ------------
    package_path_config_files = os.path.join(package_path, 'conf')
    package_path_log_files = os.path.join(package_path, 'log')

    path_conf_file = os.path.join(package_path_config_files, 'kinect_azure_settings.conf')
    ui_path_config_file = os.path.join(package_path_config_files, 'gui_ka_single_mode.conf')
    path_log_file = os.path.join(package_path_log_files, 'gui_ka_single_mode.log')  # todo: check if this is used

    # ------------
    root_folder = os.path.join(BASE_DIR, 'ak_sm_recorder')  #
    package_path_config_files = os.path.join(package_path, 'conf')
    path_user_config_files = os.path.join(root_folder, 'conf')
    path_user_output_folder = os.path.join(root_folder, 'recorded_video')

    print(f'user_path -> {user_path}')
    print('BASE_DIR->', BASE_DIR)
    print('current_main_path_str', current_main_path_str)
    print('package_path', package_path)
    print('path_gui_conf_file->', ui_path_config_file)
    print("package_path_config_files->", package_path_config_files)
    print('path_user_config_files->', path_user_config_files)

    # if directory doen't exist, then create
    if os.path.exists(root_folder):
        print('Directory exist!!!', root_folder)
    else:
        # creates hierarchy
        print('CREATING ', root_folder)
        print('CREATING ', path_user_config_files)
        print('CREATING ', path_user_output_folder)
        os.mkdir(root_folder)
        os.mkdir(path_user_config_files)
        os.mkdir(path_user_output_folder)

    if os.path.exists(path_user_config_files):
        print('Directory exist!!!', path_user_config_files)
    else:
        print('Directory doesn\'t exist!!!', path_user_config_files)
        print('Creating directory ', path_user_config_files)
        os.mkdir(path_user_config_files)
        copy_folder(package_path_config_files, path_user_config_files)

    # -------------------------
    if os.path.exists(path_user_output_folder):
        print('Directory exist!!!', path_user_output_folder)
    else:
        print('Directory doesn\'t exist!!!', path_user_output_folder)
        print('Creating directory ', path_user_output_folder)
        os.mkdir(path_user_output_folder)

    # -------------------------
    gui_config_obj = GUIKASingleModeConfig(ui_path_config_file)
    gui_config_obj.file_browser_input_folder = path_user_output_folder
    gui_config_obj.path_conf_file = path_conf_file
    # -------------------------
    app = GUIKASingleMode(gui_config_obj)
    app.mainloop()
    # -------------------------

    # INTERNATIONALIZATION
    # base file for translation is located in /base/
    # Use xgettext https://www.gnu.org/software/gettext/manual/html_node/xgettext-Invocation.html
    # xgettext -d gui_single_mode -o locale/gui_single_mode.pot gui_single_mode/gui_single_mode.py
