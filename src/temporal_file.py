    def draw_radiobuttons(self):
        self.selected_depth = tk.StringVar()  # todo: to improve this because is dirty code
        self.selected_depth.set(self.my_device_configuration.depth_mode.name)  # default asignment from config
        self.selected_color = tk.StringVar()
        self.selected_color.set(self.my_device_configuration.color_format.name)
        self.selected_resolution = tk.StringVar()
        self.selected_resolution.set(self.my_device_configuration.color_resolution.name)
        self.selected_framerate = tk.StringVar()
        self.selected_framerate.set(self.my_device_configuration.camera_fps.name)

        self.depth_mode_list = (
            (DepthMode.NFOV_2X2BINNED.name, DepthMode.NFOV_2X2BINNED.name),
            (DepthMode.NFOV_UNBINNED.name, DepthMode.NFOV_UNBINNED.name),
            (DepthMode.WFOV_2X2BINNED.name, DepthMode.WFOV_2X2BINNED.name),
            (DepthMode.WFOV_UNBINNED.name, DepthMode.WFOV_UNBINNED.name)
        )

        for depth_mode_option in self.depth_mode_list:
            self.depth_mode_radio_0 = ttk.Radiobutton(
                self.depth_mode_frame,
                text=depth_mode_option[0],
                value=depth_mode_option[1],
                variable=self.selected_depth
            )

            self.depth_mode_radio_0.pack(fill='x', padx=5, pady=5)
        # --------------
        self.color_mode_list = (
            (ImageFormat.COLOR_BGRA32.name, ImageFormat.COLOR_BGRA32.name),
            (ImageFormat.COLOR_MJPG.name, ImageFormat.COLOR_MJPG.name),
            (ImageFormat.COLOR_NV12.name, ImageFormat.COLOR_NV12.name),
            (ImageFormat.COLOR_YUY2.name, ImageFormat.COLOR_YUY2.name)
        )

        for color_mode_option in self.color_mode_list:
            self.color_mode_radio = ttk.Radiobutton(
                self.color_mode_frame,
                text=color_mode_option[0],
                value=color_mode_option[1],
                variable=self.selected_color
            )
            self.color_mode_radio.pack(fill='x', padx=5, pady=5)
        # --------------
        # --------------
        self.resolution_mode_list = (
            (ColorResolution.RES_720P.name, ColorResolution.RES_720P.name),
            (ColorResolution.RES_1080P.name, ColorResolution.RES_1080P.name),
            (ColorResolution.RES_1440P.name, ColorResolution.RES_1440P.name),
            (ColorResolution.RES_2160P.name, ColorResolution.RES_2160P.name),
            (ColorResolution.RES_1536P.name, ColorResolution.RES_1536P.name),
            (ColorResolution.RES_3072P.name, ColorResolution.RES_3072P.name),
        )

        for resolution_mode_option in self.resolution_mode_list:
            self.resolution_mode_radio = ttk.Radiobutton(
                self.resolution_mode_frame,
                text=resolution_mode_option[0],
                value=resolution_mode_option[1],
                variable=self.selected_resolution
            )
            self.resolution_mode_radio.pack(fill='x', padx=5, pady=5)
        # --------------
        # --------------
        self.framerate_mode_list = (
            (FPS.FPS_30.name, FPS.FPS_30.name),
            (FPS.FPS_15.name, FPS.FPS_15.name),
            (FPS.FPS_5.name, FPS.FPS_5.name)
        )

        for framerate_mode_option in self.framerate_mode_list:
            self.framerate_mode_radio = ttk.Radiobutton(
                self.framerate_mode_frame,
                text=framerate_mode_option[0],
                value=framerate_mode_option[1],
                variable=self.selected_framerate
            )
            self.framerate_mode_radio.pack(fill='x', padx=5, pady=5)
        # --------------
        pass


    depth_mode_option = self.depth_mode_list[0]
    self.depth_mode_radio_0 = ttk.Radiobutton(
        self.depth_mode_frame,
        text=depth_mode_option[0],
        value=depth_mode_option[1],
        variable=self.selected_depth
    )
    self.depth_mode_radio_0.pack(fill='x', padx=5, pady=5)

    depth_mode_option = self.depth_mode_list[1]
    self.depth_mode_radio_1 = ttk.Radiobutton(
        self.depth_mode_frame,
        text=depth_mode_option[0],
        value=depth_mode_option[1],
        variable=self.selected_depth
    )
    self.depth_mode_radio_1.pack(fill='x', padx=5, pady=5)
    self.depth_mode_radio_1.config(state='disabled')
    self.depth_mode_radio_1.pack(fill='x', padx=5, pady=5)


    # list = self.depth_mode_frame.winfo_children()
    # for l in list:
    #    l.destroy()