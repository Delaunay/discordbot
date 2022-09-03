import os

import discord

from vlcbot.core.bot import VLCBotClient
from vlcbot.core.sources import get_source


TOKEN = 'MTAxNTY2Mzc2MTE2OTg1MDQxOA.GJ22GE.iAMOHuP1WCXC780rfDUv99CoOT2OfZ0qv1Ov1A'
os.environ['DISCORD_TOKEN'] = TOKEN



# get_source('vlcbot.plugins.sources.file')


client_id = 1015663761169850418

client = VLCBotClient(
    application_id=client_id,
    status=discord.Status.online,
    intents=discord.Intents.default(),
    audio_source_factory=get_source('vlcbot.plugins.sources.app')
)

client.run(TOKEN)
