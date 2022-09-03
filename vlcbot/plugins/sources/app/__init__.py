import subprocess
import os
from typing import Any

import discord

from vlcbot.core.conf import ffmpeg


class CustomFFmpegPCMAudio(discord.FFmpegPCMAudio):
    def _spawn_process(self, args: Any, **subprocess_kwargs: Any) -> subprocess.Popen:
        print(' '.join(args))

        # args = [args[0], '-f', 'dshow', '-i', 'audio="virtual-audio-capturer"', '-f', 'gdigrab', '-i', 'VLC media Player' ]
        return super()._spawn_process(args, **subprocess_kwargs)


class AppAudioSource(discord.FFmpegAudio):
    def __init__(self, source, *, args, **subprocess_kwargs) -> None:
        super().__init__(source, executable=ffmpeg(), args=args, **subprocess_kwargs)

    def read(self) -> bytes:
        ret = self._stdout.read(discord.opus.OpusEncoder.FRAME_SIZE)
        if len(ret) != discord.opus.OpusEncoder.FRAME_SIZE:
            return b''
        return ret


def source():
        return discord.PCMVolumeTransformer(
        CustomFFmpegPCMAudio(
            executable=ffmpeg(),
            source='audio="Stereo Mix"',
            stderr=subprocess.PIPE,
            before_options='-f dshow',
        ),
        volume=0.25
    )

    # return AppAudioSource("title=VLC media player", args=[])
