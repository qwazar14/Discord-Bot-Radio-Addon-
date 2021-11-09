import nextcord
from nextcord import FFmpegPCMAudio
from config.access_config import settings

from nextcord.ext import commands, tasks
from cog.radio import Radio

client = commands.Bot(command_prefix=settings['botPrefix'])
radio_ulitka = 'http://air.radioulitka.ru:8000/ulitka_128'


@client.event
async def on_ready():
    client.add_cog(Radio(client, radio_ulitka))
    print(f"[INFO] Bot with url {radio_ulitka} is ready! PREFIX = '{client.command_prefix}'")

# Setting `Streaming ` status




client.run(settings['botToken'])
