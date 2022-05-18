"""
Project: Fruit Size Estimation
Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: November 2021
Description:

Use:
from gui_frame_ext.about_window import AboutWindow

    def open_about_data(self):
        about_windows = AboutWindow(self)
        about_windows.grab_set()
"""
import os
import datetime
import time
import tkinter as tk
#from tkinter import *
from tkinter import ttk

import helpers.helper_load_config as hc
from pyk4a import Config, ColorResolution, ImageFormat, DepthMode
from pyk4a import FPS, WiredSyncMode

from gui_single_mode.about_window import AboutWindow2
from camera_classes.job_thread_azure import JobThreadAzure
from camera_classes.job_thread_3d_azure import JobThread3DAzure
from camera_classes.KA_manager2 import KAManager2


class GUIKASingleMode(tk.Tk):
    take_a_capture_flag = False

    FRAME_WIDTH = 100
    LABEL_WIDTH = 15
    ENTRY_WIDTH_PATH = 50
    BUTTON_WIDTH = 30

    TAB_NAME_1 = 'Camera'
    TAB_NAME_2 = 'Configuration'

    ui_config_obj = None
    path_video_output = None
    my_device_configuration = None
    # ----------------------------
    selected_depth = None
    depth_mode_list = None
    depth_mode_radio_0 = None
    depth_mode_radio_1 = None

    selected_color = None
    color_mode_list = None
    color_mode_radio = None

    selected_resolution = None
    resolution_mode_list = None
    resolution_mode_radio = None

    selected_framerate = None
    framerate_mode_list = None
    framerate_mode_radio = None

    # ----------------------------
    def __init__(self, ui_config_obj, master=None):
        super().__init__()
        # -----------------------
        self.geometry(ui_config_obj.geometry_main)
        self.title(ui_config_obj.app_title)
        self.resizable(width=False, height=False)
        self.attributes('-topmost', True)
        # -----------------------
        assets_path = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(assets_path, 'assets', 'icon_app.png')
        self.iconphoto(False, tk.PhotoImage(file=img_path))

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        # ---------------
        self.ui_config_obj = ui_config_obj
        self.path_video_output = self.ui_config_obj.file_browser_input_folder
        self.initialize_device()
        # ---------------
        # calling methods to create components
        self.create_tabs()
        self.create_tab_page_1()
        self.create_tab_page_2()
        self.create_menu_bars()
        # ------

    def initialize_device(self):
        self.my_device_configuration = hc.load_config_from_file(self.ui_config_obj.path_conf_file)
        self.my_ka_manager = None
        #self.my_ka_manager = KAManager2(self.my_device_configuration, self.path_video_output)
        pass

    def create_tabs(self):
        self.tab_group = ttk.Notebook(self)
        self.tab_1 = tk.Frame(self.tab_group)
        self.tab_2 = tk.Frame(self.tab_group)
        self.tab_group.bind("<<NotebookTabChanged>>", self.on_tab_selected)
        self.tab_group.add(self.tab_1, text=self.TAB_NAME_1)
        self.tab_group.add(self.tab_2, text=self.TAB_NAME_2)
        self.tab_group.pack(expand=1, fill="both")
        pass

    def on_tab_selected(self, event):
        print('on_tab_selected')
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")
        print(tab_text)
        if tab_text == "Configurations":
            print('Make something with Configurations')

        if tab_text == "Camera":
            print('Make something with Camera')
        pass

    def draw_depth_mode_radiobuttons(self):
        self.depth_mode_list = (
            (DepthMode.NFOV_2X2BINNED.name, DepthMode.NFOV_2X2BINNED.name),
            (DepthMode.NFOV_UNBINNED.name, DepthMode.NFOV_UNBINNED.name),
            (DepthMode.WFOV_2X2BINNED.name, DepthMode.WFOV_2X2BINNED.name),
            (DepthMode.WFOV_UNBINNED.name, DepthMode.WFOV_UNBINNED.name)
        )

        depth_mode_option = self.depth_mode_list[0]
        self.depth_mode_radio_0 = ttk.Radiobutton(
            self.depth_mode_frame,
            text=depth_mode_option[0],
            value=depth_mode_option[1],
            variable=self.selected_depth,
            command=self.process_depth_radiobutton
        )
        self.depth_mode_radio_0.pack(fill='x', padx=5, pady=5)

        depth_mode_option = self.depth_mode_list[1]
        self.depth_mode_radio_1 = ttk.Radiobutton(
            self.depth_mode_frame,
            text=depth_mode_option[0],
            value=depth_mode_option[1],
            variable=self.selected_depth,
            command=self.process_depth_radiobutton
        )
        self.depth_mode_radio_1.pack(fill='x', padx=5, pady=5)

        depth_mode_option = self.depth_mode_list[2]
        self.depth_mode_radio_2 = ttk.Radiobutton(
            self.depth_mode_frame,
            text=depth_mode_option[0],
            value=depth_mode_option[1],
            variable=self.selected_depth,
            command=self.process_depth_radiobutton
        )
        self.depth_mode_radio_2.pack(fill='x', padx=5, pady=5)

        depth_mode_option = self.depth_mode_list[3]
        self.depth_mode_radio_3 = ttk.Radiobutton(
            self.depth_mode_frame,
            text=depth_mode_option[0],
            value=depth_mode_option[1],
            variable=self.selected_depth,
            command=self.process_depth_radiobutton
        )
        self.depth_mode_radio_3.pack(fill='x', padx=5, pady=5)

    def draw_color_mode_radiobuttons(self):
        self.color_mode_list = (
            (ImageFormat.COLOR_BGRA32.name, ImageFormat.COLOR_BGRA32.name),
            (ImageFormat.COLOR_MJPG.name, ImageFormat.COLOR_MJPG.name),
            (ImageFormat.COLOR_NV12.name, ImageFormat.COLOR_NV12.name),
            (ImageFormat.COLOR_YUY2.name, ImageFormat.COLOR_YUY2.name)
        )

        color_mode_option = self.color_mode_list[0]
        self.color_mode_radio_0 = ttk.Radiobutton(
            self.color_mode_frame,
            text=color_mode_option[0],
            value=color_mode_option[1],
            variable=self.selected_color,
            command=self.process_color_mode_radiobutton
        )
        self.color_mode_radio_0.pack(fill='x', padx=5, pady=5)

        color_mode_option = self.color_mode_list[1]
        self.color_mode_radio_1 = ttk.Radiobutton(
            self.color_mode_frame,
            text=color_mode_option[0],
            value=color_mode_option[1],
            variable=self.selected_color,
            command=self.process_color_mode_radiobutton
        )
        self.color_mode_radio_1.pack(fill='x', padx=5, pady=5)

        color_mode_option = self.color_mode_list[2]
        self.color_mode_radio_2 = ttk.Radiobutton(
            self.color_mode_frame,
            text=color_mode_option[0],
            value=color_mode_option[1],
            variable=self.selected_color,
            command=self.process_color_mode_radiobutton
        )
        self.color_mode_radio_2.pack(fill='x', padx=5, pady=5)

        color_mode_option = self.color_mode_list[3]
        self.color_mode_radio_3 = ttk.Radiobutton(
            self.color_mode_frame,
            text=color_mode_option[0],
            value=color_mode_option[1],
            variable=self.selected_color,
            command=self.process_color_mode_radiobutton
        )
        self.color_mode_radio_3.pack(fill='x', padx=5, pady=5)
        # --------------

    def draw_resolution_mode_radiobuttons(self):
        print('draw_resolution_mode_radiobutton()')
        # --------------
        self.resolution_mode_list = (
            (ColorResolution.RES_720P.name, ColorResolution.RES_720P.name),
            (ColorResolution.RES_1080P.name, ColorResolution.RES_1080P.name),
            (ColorResolution.RES_1440P.name, ColorResolution.RES_1440P.name),
            (ColorResolution.RES_2160P.name, ColorResolution.RES_2160P.name),
            (ColorResolution.RES_1536P.name, ColorResolution.RES_1536P.name),
            (ColorResolution.RES_3072P.name, ColorResolution.RES_3072P.name),
        )

        resolution_mode_option = self.resolution_mode_list[0]
        self.resolution_mode_radio_0 = ttk.Radiobutton(
            self.resolution_mode_frame,
            text=resolution_mode_option[0],
            value=resolution_mode_option[1],
            variable=self.selected_resolution,
            command=self.process_resolution_mode_radiobutton
        )
        self.resolution_mode_radio_0.pack(fill='x', padx=5, pady=5)

        resolution_mode_option = self.resolution_mode_list[1]
        self.resolution_mode_radio_1 = ttk.Radiobutton(
            self.resolution_mode_frame,
            text=resolution_mode_option[0],
            value=resolution_mode_option[1],
            variable=self.selected_resolution,
            command=self.process_resolution_mode_radiobutton
        )
        self.resolution_mode_radio_1.pack(fill='x', padx=5, pady=5)

        resolution_mode_option = self.resolution_mode_list[2]
        self.resolution_mode_radio_2 = ttk.Radiobutton(
            self.resolution_mode_frame,
            text=resolution_mode_option[0],
            value=resolution_mode_option[1],
            variable=self.selected_resolution,
            command=self.process_resolution_mode_radiobutton
        )
        self.resolution_mode_radio_2.pack(fill='x', padx=5, pady=5)

        resolution_mode_option = self.resolution_mode_list[3]
        self.resolution_mode_radio_3 = ttk.Radiobutton(
            self.resolution_mode_frame,
            text=resolution_mode_option[0],
            value=resolution_mode_option[1],
            variable=self.selected_resolution,
            command=self.process_resolution_mode_radiobutton
        )
        self.resolution_mode_radio_3.pack(fill='x', padx=5, pady=5)

        resolution_mode_option = self.resolution_mode_list[4]
        self.resolution_mode_radio_4 = ttk.Radiobutton(
            self.resolution_mode_frame,
            text=resolution_mode_option[0],
            value=resolution_mode_option[1],
            variable=self.selected_resolution,
            command=self.process_resolution_mode_radiobutton
        )
        self.resolution_mode_radio_4.pack(fill='x', padx=5, pady=5)

        resolution_mode_option = self.resolution_mode_list[5]
        self.resolution_mode_radio_5 = ttk.Radiobutton(
            self.resolution_mode_frame,
            text=resolution_mode_option[0],
            value=resolution_mode_option[1],
            variable=self.selected_resolution,
            command=self.process_resolution_mode_radiobutton
        )
        self.resolution_mode_radio_5.pack(fill='x', padx=5, pady=5)

    def draw_framerate_mode_radiobuttons(self):
        print('draw_framerate_mode_radiobuttons()')
        # --------------
        self.framerate_mode_list = (
            (FPS.FPS_30.name, FPS.FPS_30.name),
            (FPS.FPS_15.name, FPS.FPS_15.name),
            (FPS.FPS_5.name, FPS.FPS_5.name)
        )

        framerate_mode_option = self.framerate_mode_list[0]
        self.framerate_mode_radio_0 = ttk.Radiobutton(
            self.framerate_mode_frame,
            text=framerate_mode_option[0],
            value=framerate_mode_option[1],
            variable=self.selected_framerate,
            command=self.process_framerate_mode_radiobutton
        )
        self.framerate_mode_radio_0.pack(fill='x', padx=5, pady=5)

        framerate_mode_option = self.framerate_mode_list[1]
        self.framerate_mode_radio_1 = ttk.Radiobutton(
            self.framerate_mode_frame,
            text=framerate_mode_option[0],
            value=framerate_mode_option[1],
            variable=self.selected_framerate,
            command=self.process_framerate_mode_radiobutton
        )
        self.framerate_mode_radio_1.pack(fill='x', padx=5, pady=5)

        framerate_mode_option = self.framerate_mode_list[2]
        self.framerate_mode_radio_2 = ttk.Radiobutton(
            self.framerate_mode_frame,
            text=framerate_mode_option[0],
            value=framerate_mode_option[1],
            variable=self.selected_framerate,
            command=self.process_framerate_mode_radiobutton
        )
        self.framerate_mode_radio_2.pack(fill='x', padx=5, pady=5)

    def draw_radiobuttons(self):
        self.selected_depth = tk.StringVar()  # todo: to improve this because is dirty code
        self.selected_depth.set(self.my_device_configuration.depth_mode.name)  # default asignment from config
        self.selected_color = tk.StringVar()
        self.selected_color.set(self.my_device_configuration.color_format.name)
        self.selected_resolution = tk.StringVar()
        self.selected_resolution.set(self.my_device_configuration.color_resolution.name)
        self.selected_framerate = tk.StringVar()
        self.selected_framerate.set(self.my_device_configuration.camera_fps.name)

        self.draw_depth_mode_radiobuttons()
        self.draw_color_mode_radiobuttons()
        self.draw_resolution_mode_radiobuttons()
        self.draw_framerate_mode_radiobuttons()

        self.process_depth_radiobutton()
        self.process_color_mode_radiobutton()
        self.process_resolution_mode_radiobutton()
        self.process_framerate_mode_radiobutton()

    def disable_high_resolution_mode(self):
        # ----------
        self.resolution_mode_radio_1.config(state='disabled')
        self.resolution_mode_radio_1.pack(fill='x', padx=5, pady=5)
        self.resolution_mode_radio_2.config(state='disabled')
        self.resolution_mode_radio_2.pack(fill='x', padx=5, pady=5)
        self.resolution_mode_radio_3.config(state='disabled')
        self.resolution_mode_radio_3.pack(fill='x', padx=5, pady=5)
        self.resolution_mode_radio_4.config(state='disabled')
        self.resolution_mode_radio_4.pack(fill='x', padx=5, pady=5)
        self.resolution_mode_radio_5.config(state='disabled')
        self.resolution_mode_radio_5.pack(fill='x', padx=5, pady=5)
        # ----------
        # select first options
        self.selected_resolution.set(ColorResolution.RES_720P.name)
        self.resolution_mode_radio_0.config(state='normal')
        self.resolution_mode_radio_0.config(variable=self.selected_resolution)
        # ----------

    def disable_high_framerate_mode(self):
        self.selected_framerate.set(FPS.FPS_15.name)
        self.framerate_mode_radio_0.config(state='disabled')
        self.framerate_mode_radio_1.config(state='normal')
        self.framerate_mode_radio_1.config(variable=self.selected_framerate)

    def enable_depth_mode_radiobuttons(self):
        self.depth_mode_radio_0.config(state='normal')
        self.depth_mode_radio_0.pack(fill='x', padx=5, pady=5)
        self.depth_mode_radio_1.config(state='normal')
        self.depth_mode_radio_1.pack(fill='x', padx=5, pady=5)
        self.depth_mode_radio_2.config(state='normal')
        self.depth_mode_radio_2.pack(fill='x', padx=5, pady=5)
        self.depth_mode_radio_3.config(state='normal')
        self.depth_mode_radio_3.pack(fill='x', padx=5, pady=5)

    def enable_color_mode_radiobuttons(self):
        self.color_mode_radio_0.config(state='normal')
        self.color_mode_radio_0.pack(fill='x', padx=5, pady=5)
        self.color_mode_radio_1.config(state='normal')
        self.color_mode_radio_1.pack(fill='x', padx=5, pady=5)
        self.color_mode_radio_2.config(state='normal')
        self.color_mode_radio_2.pack(fill='x', padx=5, pady=5)
        self.color_mode_radio_3.config(state='normal')
        self.color_mode_radio_3.pack(fill='x', padx=5, pady=5)

    def enable_resolution_mode_radiobuttons(self):
        self.resolution_mode_radio_0.config(state='normal')
        self.resolution_mode_radio_0.pack(fill='x', padx=5, pady=5)
        self.resolution_mode_radio_1.config(state='normal')
        self.resolution_mode_radio_1.pack(fill='x', padx=5, pady=5)
        self.resolution_mode_radio_2.config(state='normal')
        self.resolution_mode_radio_2.pack(fill='x', padx=5, pady=5)
        self.resolution_mode_radio_3.config(state='normal')
        self.resolution_mode_radio_3.pack(fill='x', padx=5, pady=5)
        self.resolution_mode_radio_4.config(state='normal')
        self.resolution_mode_radio_4.pack(fill='x', padx=5, pady=5)
        self.resolution_mode_radio_5.config(state='normal')
        self.resolution_mode_radio_5.pack(fill='x', padx=5, pady=5)

    def enable_frame_rate_radiobuttons(self):
        self.framerate_mode_radio_0.config(state='normal')
        self.framerate_mode_radio_0.pack(fill='x', padx=5, pady=5)
        self.framerate_mode_radio_1.config(state='normal')
        self.framerate_mode_radio_1.pack(fill='x', padx=5, pady=5)
        self.framerate_mode_radio_2.config(state='normal')
        self.framerate_mode_radio_2.pack(fill='x', padx=5, pady=5)

    def process_depth_radiobutton(self):
        print('process_depth_radiobutton(self):', self.selected_depth.get())
        if self.selected_depth.get() == DepthMode.NFOV_2X2BINNED.name:
            self.enable_depth_mode_radiobuttons()
            self.enable_color_mode_radiobuttons()
            self.enable_resolution_mode_radiobuttons()
            self.enable_frame_rate_radiobuttons()

        elif self.selected_depth.get() == DepthMode.NFOV_UNBINNED.name:
            self.enable_depth_mode_radiobuttons()
            self.enable_color_mode_radiobuttons()
            self.enable_resolution_mode_radiobuttons()
            self.enable_frame_rate_radiobuttons()

        elif self.selected_depth.get() == DepthMode.WFOV_2X2BINNED.name:
            self.enable_depth_mode_radiobuttons()
            self.enable_color_mode_radiobuttons()
            self.enable_resolution_mode_radiobuttons()
            self.enable_frame_rate_radiobuttons()

        elif self.selected_depth.get() == DepthMode.WFOV_UNBINNED.name:
            self.disable_high_framerate_mode()

        if self.selected_color.get() == ImageFormat.COLOR_NV12.name:
            self.disable_high_resolution_mode()

        if self.selected_color.get() == ImageFormat.COLOR_YUY2.name:
            self.disable_high_resolution_mode()

    def process_color_mode_radiobutton(self):
        print('process_color_mode_radiobutton(self):', self.selected_color.get())

        if self.selected_color.get() == ImageFormat.COLOR_BGRA32.name:
            self.enable_depth_mode_radiobuttons()
            self.enable_color_mode_radiobuttons()
            self.enable_resolution_mode_radiobuttons()
            self.enable_frame_rate_radiobuttons()

        elif self.selected_color.get() == ImageFormat.COLOR_MJPG.name:
            self.enable_depth_mode_radiobuttons()
            self.enable_color_mode_radiobuttons()
            self.enable_resolution_mode_radiobuttons()
            self.enable_frame_rate_radiobuttons()

            if self.selected_depth.get() == DepthMode.WFOV_2X2BINNED:
                self.disable_high_framerate_mode()

            elif self.selected_depth.get() == DepthMode.WFOV_UNBINNED.name:
                self.disable_high_framerate_mode()

        elif self.selected_color.get() == ImageFormat.COLOR_NV12.name:
            # ----------
            self.disable_high_resolution_mode()
            self.disable_high_framerate_mode()
            # ----------

        elif self.selected_color.get() == ImageFormat.COLOR_YUY2.name:
            self.enable_depth_mode_radiobuttons()
            self.enable_color_mode_radiobuttons()
            self.enable_resolution_mode_radiobuttons()
            self.enable_frame_rate_radiobuttons()
            # ----------
            self.disable_high_resolution_mode()

            if self.selected_depth.get() == DepthMode.WFOV_UNBINNED.name:
                self.disable_high_framerate_mode()
            # ----------

    def process_resolution_mode_radiobutton(self):
        print('process_resolution_mode_radiobutton(self):', self.selected_resolution.get())
        pass

    def process_framerate_mode_radiobutton(self):
        print('process_framerate_mode_radiobutton(self):', self.selected_framerate.get())
        pass

    def process_radiobuttons(self):
        print('PROCESS RADIOBUTTONS')
        print('selected_depth ->', self.selected_depth.get())
        print('selected_color ->', self.selected_color.get())
        print('selected_resolution ->', self.selected_resolution.get())
        print('selected_framerate ->', self.selected_framerate.get())
        print('update main configuration')
        print('save in file')
        self.my_device_configuration = Config(
            color_resolution=hc.convert_color_resolution(self.selected_resolution.get()),
            color_format=hc.convert_color_format(self.selected_color.get()),
            depth_mode=hc.convert_depth_mode(self.selected_depth.get()),
            camera_fps=hc.convert_camera_fps(self.selected_framerate.get()),
            synchronized_images_only=True,
            depth_delay_off_color_usec=0,
            wired_sync_mode=WiredSyncMode.STANDALONE,
            subordinate_delay_off_master_usec=0,
            disable_streaming_indicator=False
        )
        hc.save_config_in_file(self.ui_config_obj.path_conf_file, self.my_device_configuration)
        self.initialize_device()
        pass

    def create_tab_page_2(self):
        self.depth_mode_frame = tk.LabelFrame(self.tab_2, text="Depth options", width=self.FRAME_WIDTH)
        self.depth_mode_frame.grid(row=1, column=1, padx=5, pady=5)

        self.color_mode_frame = tk.LabelFrame(self.tab_2, text="Color options", width=self.FRAME_WIDTH)
        self.color_mode_frame.grid(row=1, column=2, padx=5, pady=5)

        self.resolution_mode_frame = tk.LabelFrame(self.tab_2, text="Resolution options", width=self.FRAME_WIDTH)
        self.resolution_mode_frame.grid(row=2, column=1, padx=5, pady=5)

        self.framerate_mode_frame = tk.LabelFrame(self.tab_2, text="Framerate options", width=self.FRAME_WIDTH)
        self.framerate_mode_frame.grid(row=2, column=2, padx=5, pady=5)

        self.start_config_button = tk.Button(self.tab_2, text='Save config', command=self.process_radiobuttons,
                                             width=self.BUTTON_WIDTH, )
        self.start_config_button.grid(row=3, column=1, columnspan=3, padx=5, ipady=5)
        self.draw_radiobuttons()

    def create_tab_page_1(self):
        self.camera_cmd_frame = tk.LabelFrame(self.tab_1, text="Commands", relief=tk.RIDGE,
                                              width=self.FRAME_WIDTH)  # todo: change frame
        self.camera_cmd_frame.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        # ---------------
        self.show_real_time_button = tk.Button(self.camera_cmd_frame, text='Show real time',
                                               command=self.show_real_time,
                                               width=self.BUTTON_WIDTH)
        self.show_real_time_button.grid(row=1, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.start_record_button = tk.Button(self.camera_cmd_frame, text='Start record', command=self.enable_record,
                                             width=self.BUTTON_WIDTH)
        self.start_record_button.grid(row=2, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.stop_record_button = tk.Button(self.camera_cmd_frame, text='Stop record', command=self.stop_record,
                                            width=self.BUTTON_WIDTH)
        self.stop_record_button.grid(row=3, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.take_capture_button = tk.Button(self.camera_cmd_frame, text='Take capture', command=self.take_capture,
                                             width=self.BUTTON_WIDTH)
        self.take_capture_button.grid(row=4, column=1, sticky=tk.W, ipadx=3, ipady=3)

        self.take_3d_capture_button = tk.Button(self.camera_cmd_frame, text='Take 3D point cloud capture', command=self.take_3d_capture, width=self.BUTTON_WIDTH)
        self.take_3d_capture_button.grid(row=5, column=1, sticky=tk.W, ipadx=3, ipady=3)


        ########################################################
        # MESSAGE FRAME
        self.message_frame = tk.LabelFrame(self.tab_1, text="Info", relief=tk.RIDGE, width=self.FRAME_WIDTH)
        self.message_frame.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

        self.messages_label = tk.Label(self.message_frame, text='Messages:')
        self.messages_label.grid(row=1, column=0, sticky=tk.W, ipadx=3, ipady=3)

        self.messages_info = tk.Text(self.message_frame, width=28, height=5)
        self.messages_info.grid(row=2, column=0, sticky=tk.W)
        # ---------------
        self.quit_button = tk.Button(self.tab_1, text='Quit', command=self.quit_app, width=32)
        self.quit_button.grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)
        # ---------------
        self.ui_buttons_enable_all()
        # ---------------

    def update_tasks(self):
        execution_time_update = datetime.datetime.utcnow()
        # print(f"We make a task HERE!! {execution_time_update}")
        self.after(2000, self.update_tasks)

    def create_menu_bars(self):
        self.menubar = tk.Menu(self)
        self.menu_help = tk.Menu(self.menubar, tearoff=False)  # delete dash lines
        self.menu_help.add_command(label='About...', command=self.not_implemented_yet)
        self.menubar.add_cascade(menu=self.menu_help, label='About', underline=0)
        self.config(menu=self.menubar)  # add menu to window

    def ui_buttons_enable_all(self):
        self.show_real_time_button["state"] = "active"
        self.start_record_button["state"] = "active"
        self.stop_record_button["state"] = "disabled"
        self.take_capture_button["state"] = "active"

    def ui_buttons_disable_all(self):
        self.show_real_time_button["state"] = "active"
        self.start_record_button["state"] = "active"
        self.stop_record_button["state"] = "disabled"
        self.take_capture_button["state"] = "disabled"

    def ui_buttons_enable_record(self):
        self.show_real_time_button["state"] = "disabled"
        self.start_record_button["state"] = "disabled"
        self.stop_record_button["state"] = "active"
        self.take_capture_button["state"] = "disabled"

    def ui_buttons_stop_record(self):
        self.show_real_time_button["state"] = "active"
        self.start_record_button["state"] = "active"
        self.stop_record_button["state"] = "disabled"
        self.take_capture_button["state"] = "active"

    def ui_buttons_take_capture(self):
        self.show_real_time_button["state"] = "disabled"
        self.show_real_time_button["state"] = "disabled"
        self.start_record_button["state"] = "disabled"
        self.stop_record_button["state"] = "active"
        print("Taking a capture!")
        self.job_ak_camera = JobThreadAzure(self.my_device_configuration, self.path_video_output)
        self.job_ak_camera.start()
        print('Waiting seconds and recording data--> ')
        time.sleep(4)  # todo: put this in config
        self.job_ak_camera.shutdown_flag.set()
        self.job_ak_camera.join()
        print('Video saved in --> ', self.path_video_output)
        self.ui_buttons_enable_all()
        pass


    def ui_buttons_3d_take_capture(self):
        self.show_real_time_button["state"] = "disabled"
        self.show_real_time_button["state"] = "disabled"
        self.start_record_button["state"] = "disabled"
        self.stop_record_button["state"] = "active"
        print("Taking a 3d cloud point capture!")
        self.job_ak_3d_camera = JobThread3DAzure(self.my_device_configuration, self.path_video_output)
        self.job_ak_3d_camera.start()
        print('Waiting seconds and recording data--> ')
        time.sleep(1)  # todo: put this in config
        self.job_ak_3d_camera.shutdown_flag.set()
        self.job_ak_3d_camera.join()
        print('3d point cloud saved in --> ', self.path_video_output)
        self.ui_buttons_enable_all()
        pass

    def not_implemented_yet(self):
        print("Not implemented yet!!!")
        about_windows = AboutWindow2(self)
        about_windows.grab_set()

    def show_real_time(self):
        print('show_real_time->')
        temporal_configuration = self.my_device_configuration
        temporal_configuration.color_format = ImageFormat.COLOR_BGRA32
        self.my_ka_manager = KAManager2(temporal_configuration, self.path_video_output)
        self.my_ka_manager.run_real_time()
        #self.my_ka_manager.show_a_capture()
        #self.my_ka_manager = None
        pass

    def enable_record(self):
        self.messages_info.insert("end", "Enable recording" + "\n")
        self.ui_buttons_enable_record()
        # self.my_device_configuration.color_format = ImageFormat.COLOR_MJPG
        self.job_ak_camera = JobThreadAzure(self.my_device_configuration, self.path_video_output)
        self.job_ak_camera.start()

    def stop_record(self):
        self.messages_info.insert("end", "Stop recording" + "\n")
        self.ui_buttons_stop_record()
        self.job_ak_camera.shutdown_flag.set()
        self.job_ak_camera.join()

    def take_capture(self):
        self.messages_info.insert("end", "Taking capture" + "\n")
        self.ui_buttons_take_capture()
        self.messages_info.insert("end", "A capture was launch!!" + "\n")
        time.sleep(5)
        self.messages_info.insert("end", "Capture time finished" + "\n")
        pass

    def take_3d_capture(self):
        self.messages_info.insert("end", "Taking 3D point cloud capture!" + "\n")
        self.ui_buttons_3d_take_capture()
        self.messages_info.insert("end", "A capture was launch!!" + "\n")
        time.sleep(5)
        self.messages_info.insert("end", "3D point cloud capture time finished" + "\n")
        pass


    def quit_app(self):
        # ---------------------------------------------
        # close token, close connection
        # ---------------------------------------------
        # self.my_ka_manager.__del__()
        self.quit
        self.destroy()
        # ---------------------------------------------
