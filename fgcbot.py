
# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.

import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform


# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Basic Bot by Habchy#1665", command_prefix="^", pm_help = False)



# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	print('Support Discord Server: https://discord.gg/FNNNgqb')
	print('Github Link: https://github.com/Habchy/BasicBot')
	print('--------')
	print('You are running BasicBot v2.1') #Do not change this. This will really help us support you, if you need support.
	print('Created by Habchy#1665')
	return await client.change_presence(game=discord.Game(name='PLAYING STATUS HERE')) #This is buggy, let us know if it doesn't work.



# This is a basic example of a call and response command. You tell it do "this" and it does it.

@client.command()
async def commands(*args):
	await client.say("\r\n"+"ping"+"\r\n"+
					 "whoami"+"\r\n"+
					 "okay"+"\r\n"+
					 "notokay"+"\r\n"+
					 "twitter"+"\r\n"+
					 "facebook"+"\r\n"+
					 "tournament"+"\r\n")

@client.command()
async def ping(*args):
	await client.say(":ping_pong: Pong!")

@client.command()
async def whoami(*args):
	await client.say("I am a bot being developed for CIFGC")

@client.command()
async def okay(*args):
	await client.say(":thumbsup:")

@client.command()
async def notokay(*args):
	await client.say(":thumbsdown:")

@client.command()
async def facebook(*args):
	await client.say("https://www.facebook.com/groups/CentralIllinoisFGC/")

@client.command()
async def twitter(*args):
	await client.say("https://www.twitter.com/CIFGCGaming/")

@client.command()
async def tournament(*args):
	await client.say("In development: Show stats for current tournament")


#run the client
client.run('NDA1Nzk3NDkxOTM4Njg5MDI1.DUpn9Q.uEs3GLRyT2mSajGk58Bk5Ec1uo0')