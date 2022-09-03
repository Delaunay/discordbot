import subprocess
import discord

from vlcbot.core.conf import ffmpeg

FILE = 'Z:/music/Amy MacDonald/This Is the Life/02 Amy Mcdonald - The Road To Home.mp3'

def source():
    return discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(executable=ffmpeg(), source=FILE, stderr=subprocess.PIPE),
        volume=0.25
    )
