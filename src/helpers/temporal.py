selected_size = tk.StringVar()
depth_mode_list = None
depth_mode_radio = None

selected_color = tk.StringVar()
color_mode_list = None
color_mode_radio = None

selected_resolution = tk.StringVar()
resolution_mode_list = None
resolution_mode_radio = None

selected_framerate = tk.StringVar()
framerate_mode_list = None
framerate_mode_radio = None

self.device_config = Config(
    color_resolution=pyk4a.ColorResolution.RES_720P,
    color_format=pyk4a.ImageFormat.COLOR_BGRA32,
    depth_mode=pyk4a.DepthMode.NFOV_UNBINNED,
    camera_fps=pyk4a.FPS.FPS_30,
    synchronized_images_only=True,
    depth_delay_off_color_usec=0,
    wired_sync_mode=pyk4a.WiredSyncMode.STANDALONE,
    subordinate_delay_off_master_usec=0,
    disable_streaming_indicator=False
)

