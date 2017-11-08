# -*- coding: utf-8 -*-

# An advanced setup script to create multiple executables and demonstrate a few
# of the features available to setup scripts
#
# hello.py is a very simple 'Hello, world' type script which also displays the
# environment in which the script runs
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the script without Python

import sys
from cx_Freeze import setup, Executable

options = {
    'build_exe': {
        'include_files': [
            'assets/image1.png',
            'assets/image2.png',
            'assets/image3.png',
            'assets/image6.gif',
            'assets/sound1.wav'
        ],
        'path': sys.path + ['modules']
    }
}

executables = [
    Executable('BikeRider.py')
]

setup(name='Bike Rider',
      version='0.1',
      description='Python Bike Rider',
      options=options,
      executables=executables
      )
