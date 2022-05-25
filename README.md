# AK_SM_RECORDER
A simple GUI recorder based on Python to manage Azure Kinect camera devices in a standalone mode.

![SOFTWARE_PRESENTATION](https://github.com/GRAP-UdL-AT/ak_sm_recorder/blob/main/docs/img/ak_sm_recorded_presentation.png?raw=true)

## Contents
* Pre-requisites
* Functionalities
* Content 3

## Pre-requisites
* Azure Kinect DK camera connected to the computer. Specifications can be seen in the [manufacturer site](https://docs.microsoft.com/es-es/azure/kinect-dk/hardware-specification).
* [SDK Azure Kinect](https://docs.microsoft.com/es-es/azure/kinect-dk/set-up-azure-kinect-dk) installed.
* [pyk4a library](https://pypi.org/project/pyk4a/) installed. If the operating system is Windows, follow this [steps](https://github.com/etiennedub/pyk4a/).  You can find test basic examples with pyk4a [here](https://github.com/etiennedub/pyk4a/tree/master/example).


## Functionalities
The functionalities of the software are briefly described.
* **[Show real time]** Display images of the device in real time. Used to see where the camera is pointing.
* **[Start record]** Start a video recording.
* **[Stop record]** Stops a video recording in progress.
* **[Take screenshots]** Take screenshots and save them in Matroska format as short videos.
* **[Take 3D point cloud capture]** Take the captures as 3D point cloud data and save them in .XYZ format.
* **[Save config]** Enables to the user to configure Azure Kinect devices parameters.
* Videos and 3D cloud points can be retrieved from **"RECORDER_VIDEOS/"** folder.


## Run AK_SM_RECORDER
## Install
```
python ak_sm_recorder_main.py
```


### Windows (TODO)
Copy folder FOLDER_HERE and execute "FILENAME_EXE.EXE".

### Linux (TODO)
..


## Package distribution format
Explain about packages distribution. 

| Package type | Package |  Url |  Description | 
|--------------|---------|------|------| 
| Windows      | .EXE    | .EXE | Executables are stored under build/ | 
| Linux        | .deb    | .deb | NOT IMPLEMENTED YET| 
| PIP          | .whl    | .whl | PIP packages are stored in build/ | 
| . | . | . |

## Files and folder description
Folder description:

| Folders                    | Description            |
|---------------------------|-------------------------|
| docs/ | Documentation |
| src/ | Source code |
| win_exe_conf/ | Specifications for building .exe files with Pyinstaller.|
| . | . |
  

Files description:

| Files                    | Description              | OS |
|---------------------------|-------------------------|---|
| activate.bat | Activate environments in Windows | WIN |
| clean_files.bat | Clean files under CMD. | WIN |
| recording.bat | Executing main script | WIN |
| build_pip.bat | Build PIP package to distribution | WIN |
| build_win.bat | Build .EXE for distribution | WIN |
| /src/ak_sm_recorder/__main__.py | Main function used in package compilation | Supported by Python |
| /ak_sm_recorder_main.py | Main function | Supported by Python |
| setup.cfg | Package configuration PIP| Supported by Python |
| pyproject.toml | Package description pip| Supported by Python |
| . | . | . |


## Development tools and environment
* [Pyinstaller](https://pyinstaller.org).
* [Opencv](https://opencv.org/).
* [Curses for Python](https://docs.python.org/3/howto/curses.html) ```pip install windows-curses```.


### Notes for developers
You can use the __main__.py for execute as first time in src/ak_frame_extractor/_ _ main _ _.py
Configure the path of the project, if you use Pycharm, put your folder root like this:
![ak_sm_recorder](https://github.com/GRAP-UdL-AT/ak_sm_recorder/blob/main/img/configuration_pycharm.png?raw=true)

### Creating virtual environment Linux (TODO)
```
python3 -m venv ./venv
source ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements_linux.txt
```

### Creating virtual environment  Windows (TODO)
```
%userprofile%"\AppData\Local\Programs\Python\Python38\python.exe" -m venv ./venv
venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements_win.txt
```
** If there are some problems in Windows, follow [this](https://github.com/etiennedub/pyk4a/) **
```
pip install pyk4a --no-use-pep517 --global-option=build_ext --global-option="-IC:\Program Files\Azure Kinect SDK v1.4.1\sdk\include" --global-option="-LC:\Program Files\Azure Kinect SDK v1.4.1\sdk\windows-desktop\amd64\release\lib"
```

### Running software
Lorem ipsum


## Authorship
This project is contributed by [GRAP-UdL-AT](http://www.grap.udl.cat/en/index.html). Please contact authors to report
bugs juancarlos.miranda@udl.cat

## Citation
If you find this code useful, please consider citing:
[GRAP-UdL-AT/ak_frame_extractor](https://github.com/GRAP-UdL-AT/ak_sm_recorder/).
