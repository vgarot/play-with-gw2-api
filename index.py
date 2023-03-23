# This example requires the 'message_content' intent.

import discord
import json
with open('settings.json','r') as f:
    data = f.read()
settings = json.loads(data)

bot = discord.Bot()

cogs_list = [
    'greetings'
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

bot.run(settings['bot_token'])
