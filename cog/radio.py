import re

import nextcord
from nextcord.ext import commands
from nextcord import FFmpegPCMAudio, PCMVolumeTransformer

from radio_api import get_current_song


class Radio(commands.Cog):

    def __init__(self, client, radio_url):
        self.client = client
        self.radio_url = radio_url
        self.player = None
        super().__init__()

    @commands.command(aliases=['radio'], pass_context=True)
    async def play(self, ctx, ):
        channel = ctx.message.author.voice.channel
        # current_song = await get_current_song()

        self.player = await channel.connect()
        ffmpeg_source = FFmpegPCMAudio(self.radio_url)
        volume_manager = PCMVolumeTransformer(ffmpeg_source, volume=0.025)
        self.player.play(volume_manager)
        # self.player.play(ffmpeg_source)

        # await self.client.change_presence(
        #     activity=nextcord.Activity(type=nextcord.ActivityType.listening, name=current_song))
        await self.client.change_presence(
            activity=nextcord.Activity(type=nextcord.ActivityType.listening, name="Radio Ulitka"))

    @commands.command(aliases=['stop_radio'], pass_context=True)
    async def stop(self, ctx):
        self.player.stop()


def setup(client, url):
    client.add_cog(Radio(client, url))
