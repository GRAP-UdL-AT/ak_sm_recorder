#!/bin/bash
# HEADER FOR BASH SCRIPTS
# Project: AK_SM_RECORDER Azure Kinect SM Recorder https://github.com/GRAP-UdL-AT/ak_sm_recorder
#
# * PAgFRUIT http://www.pagfruit.udl.cat/en/
# * GRAP http://www.grap.udl.cat/
#
# Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda

set -e

FILENAME_ZIP='ak_sm_recorder-main.zip'
REQUERIMENTS_LINUX='requirements_linux.txt'

# commands definitions
PYTHON_CMD='python3'
UNZIP_CMD=`which unzip`
MKDIR_CMD='mkdir -p'
CHMOD_CMD='chmod 755'
PIP_INSTALL_CMD='pip install'
PIP_UPDATE_CMD='pip install --upgrade pip'

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

# creating environments automatically
$PYTHON_CMD -m venv $SM_RECORDER_ENV_F
source $SM_RECORDER_ENV_F$COMMON_ENV_PATH
$PIP_UPDATE_CMD
$PIP_INSTALL_CMD -r $SM_RECORDER_NAME_F$REQUERIMENTS_LINUX
deactivate

