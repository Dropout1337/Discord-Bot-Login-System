import discord, asyncio, requests
from discord.ext import commands

token = 'Token'

client = commands.Bot(command_prefix = '++')
client.remove_command('help')

@client.event
async def on_ready():
    print('Online')

@client.command()
async def login(ctx, username, password):
  r = requests.get('https://pastebin.com/raw/jB285Hxc').text
  if username and password in r:
    await ctx.send('Success')
  else:
    await ctx.send('Invalid Username Or Password')

    
client.run(token, bot = True)
