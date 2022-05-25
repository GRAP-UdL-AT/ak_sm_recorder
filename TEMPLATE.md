# AK_SM_RECORDER
A simple GUI recorder based on Python to manage Azure Kinect camera devices in a standalone mode.

![SOFTWARE_PRESENTATION]((https://github.com/GRAP-UdL-AT/ak_sm_recorder/blob/main/docs/img/ak_sm_recorded_presentation.png?raw=true))

## Contents
* Pre-requisites.
* Functionalities
* Content 3.

## Pre-requisites
* Azure Kinect DK camera connected to the computer. Specifications can be seen in the [manufacturer site](https://docs.microsoft.com/es-es/azure/kinect-dk/hardware-specification).
* [SDK Azure Kinect](https://docs.microsoft.com/es-es/azure/kinect-dk/set-up-azure-kinect-dk) installed.
* [pyk4a library](https://pypi.org/project/pyk4a/) installed. If the operating system is Windows, follow this [steps](https://github.com/etiennedub/pyk4a/).  You can find test basic examples with pyk4a [here](https://github.com/etiennedub/pyk4a/tree/master/example).


## Functionalities
The functionalities of the software are briefly described.

### Camera tab
* **Show real time** Display images of the device in real time. Used to see where the camera is pointing.
* **Start record** Start a video recording.
* **Stop record** Stops a video recording in progress.
* **Take screenshots** Take screenshots and save them in Matroska format as short videos.
* **Take 3D point cloud capture** Take the captures as 3D point cloud data and save them in .XYZ format.

![CONFIGURATION_TAB_1](https://github.com/GRAP-UdL-AT/ak_sm_recorder/blob/main/docs/img/ak_sm_recorder_1.png?raw=true)

### Configuration tab
* **Save config** Enables to the user to configure Azure Kinect devices parameters.

![CONFIGURATION_TAB_2](https://github.com/GRAP-UdL-AT/ak_sm_recorder/blob/main/docs/img/ak_sm_recorder_2.png?raw=true)

## Retrieving stored data
Videos and 3D cloud points can be retrieved from:

![SCHEMA_RETRIEVING_DATA](https://github.com/GRAP-UdL-AT/ak_sm_recorder/blob/main/docs/img/diagram_features_1.png?raw=true)

## Install
LOREM IPSUM


## Run SOFTWARE_TITLE
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

## Files in directory

| Folder                    | Description                                                                                                                                                                                                     |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| docs/ | Documentation |
| src/ | Source code |
| win_exe_conf/ | Specifications for build .exe files with Pyinstaller |
|  | Desktop GUI based on Tkinter library. Offers the possibility of sending instructions to the remote devices.                                                                                                     |
| server_rest_api           | The server acts as an intermediary in the management of messages between remote clients and the managemen console, and stores information about of the instructions sent and received. It uses SQLite database. |
| .                         | .  

## Development tools and environment

* Development tool 1.
* Development tool 2.
* Development tool 3.

Here some developments.

## Notes for developers

You can use the __main__.py for execute as first time in src/ak_frame_extractor/_ _ main _ _.py
Configure the path of the project, if you use Pycharm, put your folder root like this:
![ak_sm_recorder](https://github.com/GRAP-UdL-AT/ak_sm_recorder/blob/main/img/configuration_pycharm.png?raw=true)

### Installing steps Linux (TODO)
Lorem ipsum

### Installing steps Windows (TODO)
Lorem ipsum

### Running software
Lorem ipsum


## Authorship
This project is contributed by [GRAP-UdL-AT](http://www.grap.udl.cat/en/index.html). Please contact authors to report
bugs juancarlos.miranda@udl.cat

## Citation
If you find this code useful, please consider citing:
[GRAP-UdL-AT/ak_frame_extractor](https://github.com/GRAP-UdL-AT/ak_sm_recorder/).
