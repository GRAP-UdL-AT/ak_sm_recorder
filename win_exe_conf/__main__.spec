# -*- mode: python ; coding: utf-8 -*-
block_cipher = None
PATH = 'C:/Users/Usuari/development/ak_sm_recorder/'

PATH_FOLDER = 'ak_sm_recorder_f'
EXECUTABLE_NAME = 'ak_sm_recorder_e'
EXECUTABLE_VERSION_NUMBER = '_0.0.1'

a = Analysis(
    [ PATH+'src/ak_sm_recorder/__main__.py' ],
    pathex=[
        PATH+'src',
        PATH+'src/ak_sm_recorder/',
        PATH+'src/ak_sm_recorder/conf/',
        PATH+'src/gui_single_mode/',
        PATH+'src/gui_single_mode/assets'
        ],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=EXECUTABLE_NAME+EXECUTABLE_VERSION_NUMBER,  # YOUR EXECUTABLE NAME HERE
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=PATH_FOLDER, # YOUR EXECUTABLE FOLDER HERE
)
