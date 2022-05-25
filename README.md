#README

## AK_SM_RECORDER functionalities
* Take captures and save it in Matroska format.
* Record videos.
* Setting configuration options for device.
* Capture data as 3D point cloud.



This directory contains examples and methods related to the use of Kinect Azure and own 
experiments and settings with this device.
Some examples are adapted from Pyk4a oficial site

## Kinect Azure camera pre-requisites
* Install SDK Azure Kinect https://docs.microsoft.com/es-es/azure/kinect-dk/set-up-azure-kinect-dk
* Install Python Wrapper pyk4a https://pypi.org/project/pyk4a/ 
If the operating system is Windows, follow this steps https://github.com/etiennedub/pyk4a/

* You can test basic examples of uses in https://github.com/etiennedub/pyk4a/tree/master/example
* Camera specifications https://docs.microsoft.com/es-es/azure/kinect-dk/hardware-specification

# Requirements
* Curses for Python https://docs.python.org/3/howto/curses.html
Especial installation for Windows pip install windows-curses
* OpenCV for Python https://opencv.org/


# Files
* test_main_threads_azure.py -> simple example of use of jobs
* test_manager_main.py -> simple example to use KAmanager class

* ui_manager_menu.py -> UI based in courses and using KAmanager class 
* ui_threat_menu.py -> UI based in courses and using JobThreadAzure

# Installing steps Linux(TODO)
python3 -m venv ./venv
sourc ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements_win.txt


# Installing in Windows 10
From command line CMD
%userprofile%"\AppData\Local\Programs\Python\Python38\python.exe" -m venv ./venv
venv\Scripts\activate.bat
pip install --upgrade pip
pip install windows-curses
pip install pyk4a
pip install path
pip install opencv-python

Or 
pip install -r requirements_win.txt

* check this page if you have problems https://github.com/etiennedub/pyk4a/

pip install pyk4a --no-use-pep517 --global-option=build_ext --global-option="-IC:\Program Files\Azure Kinect SDK v1.4.1\sdk\include" --global-option="-LC:\Program Files\Azure Kinect SDK v1.4.1\sdk\windows-desktop\amd64\release\lib""



