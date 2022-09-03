#!/usr/bin/env python
from setuptools import setup


if __name__ == '__main__':
    setup(
        name='vlcbot',
        version='0.0.0',
        description='VLC bot for discord',
        author='Pierre Delaunay',
        packages=[
            'vlcbot.core',
        ],
        setup_requires=['setuptools', "discord", "appdirs"],
        namespace_packages=[
            'vlcbot.sources',
            'vlcbot.commands',
        ],
        package_data={
            "vlcbot.binaries.ffmpeg.win64": [
                'vlcbot/binaries/ffmpeg/win64',
            ],
        },
    )
