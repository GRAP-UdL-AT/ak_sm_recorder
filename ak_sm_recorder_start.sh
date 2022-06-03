#!/bin/bash

# HEADER FOR BASH SCRIPTS
# Project: AK_SM_RECORDER Azure Kinect SM Recorder https://github.com/GRAP-UdL-AT/ak_sm_recorder
#
# * PAgFRUIT http://www.pagfruit.udl.cat/en/
# * GRAP http://www.grap.udl.cat/
#
# Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda

# commands definitions
PYTHON_CMD='python3'

# folders names definitions
DEVELOPMENT_ENV_PATH='development_env'
COMMON_ENV_PATH='bin/activate'


# files extensions names
EXT_SCRIPTS_SH='*.sh'
EXT_ZIP='.zip'

# folders names definitions
DEVELOPMENT_PATH='development'
DEVELOPMENT_ENV_PATH='development_env'
COMMON_ENV_PATH='bin/activate'


# software folders names
SM_RECORDER_NAME='ak_sm_recorder-main'


# project folders
ROOT_FOLDER_F=$HOME/$DEVELOPMENT_PATH/
SM_RECORDER_NAME_F=$ROOT_FOLDER_F$SM_RECORDER_NAME/

# environment folders
ENV_NAME='_venv'
ROOT_ENV_F=$HOME/$DEVELOPMENT_ENV_PATH/
SM_RECORDER_ENV_F=$ROOT_ENV_F$SM_RECORDER_NAME$ENV_NAME/

# activating environments
source $SM_RECORDER_ENV_F$COMMON_ENV_PATH

python ak_sm_recorder_main.py
deactivate
