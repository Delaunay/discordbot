import discord
import importlib_resources

import os



class FFmpegAudio(discord.FFmpegAudio):
    def __init__(self, source, *, executable='ffmpeg', args, **subprocess_kwargs) -> None:
        super().__init__(source, executable='ffmpeg', **subprocess_kwargs)


class VLCAudioSource:
    def read(self):
        pass

    def is_opus(self):
        pass

    def cleanup(self):
        pass


MySource = FFmpegAudio



class VLCBotClient(discord.Client):
    def __init__(self, *args, audio_source_factory, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.audio_source_factory = audio_source_factory

    async def on_ready(self):
        for guild in self.guilds:
            print(f'{self.user} is connected to the following guild:\n'f'{guild.name}(id: {guild.id})')

            # for channel in guild.channels:

            for channel in guild.voice_channels:
                print(channel, channel.id)

            voice = await channel.connect()
            voice.play(self.audio_source_factory())


    async def on_member_join(self, member):
        pass

