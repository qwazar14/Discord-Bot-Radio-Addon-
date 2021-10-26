from nextcord.ext import commands
from nextcord import FFmpegPCMAudio


class Radio(commands.Cog):

    def __init__(self, client, radio_url):
        self.client = client
        self.radio_url = radio_url
        self.player = None
        super().__init__()

    @commands.command(aliases=['radio'], pass_context=True)
    async def play(self, ctx):
        channel = ctx.message.author.voice.channel

        self.player = await channel.connect()
        self.player.play(FFmpegPCMAudio(self.radio_url))

    @commands.command(aliases=['stopradio'], pass_context=True)
    async def stop(self, ctx):
        self.player.stop()


def setup(client, url):
    client.add_cog(Radio(client, url))
