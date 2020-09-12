import discord
from discord.ext import commands
import requests

PREFIX = '.' # default prefix is .
SERVER_IP = '' # Enter server IP in the quatations
TOKEN = '' # Enter bot token in the quatations

client = commands.Bot(command_prefix = PREFIX)

@client.event
async def on_ready():
	print('Bot is running.')

@client.command()
async def status(ctx):
	r = requests.get('https://api.mcsrvstat.us/2/' + SERVER_IP)
	json_data = r.json()

	motd = str(json_data["motd"]["html"])
	players = str(json_data["players"]["online"])
	maxPlayers = str(json_data["players"]["max"])
	onlineBool = str(json_data["online"])
	version = str(json_data["version"])

	if onlineBool == 'True':
		online = 'Online'
	else:
		online = 'Offline'

	embed=discord.Embed(title="Server Status", color=0x00ff00)
	embed.set_thumbnail(url='https://api.mcsrvstat.us/icon/' + SERVER_IP)		
	embed.add_field(name="Status", value=online, inline=True)
	embed.add_field(name="Player Count", value=players + '/' + maxPlayers, inline=True)
	embed.add_field(name="Version", value=version, inline=True)
	embed.add_field(name="MOTD", value=motd, inline=True)

	await ctx.send(embed=embed)

client.run(TOKEN)