# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.

import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import functions
import smashgg


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
async def tournament(*args):
    flag = args[0]
#    if flag == "add":
#        functions.tournament_add(str(args[1]))
#        await client.say("Added tournament: **" + args[1] + "**")
#    elif flag == "remove":
#        functions.tournament_remove(tournament)
#        await client.say("Removed tournament: **" + args[1] + "**")
    if flag == "list":
        await client.say(functions.tournament_list())
    elif flag =="results":
        eventids = functions.get_eventids(args[1])
        groupids = functions.get_groupids(eventids)
        results = functions.get_player_standing(groupids)
#async def tournament(*args):


#run the client
client.run('NDA1Nzk3NDkxOTM4Njg5MDI1.DUpn9Q.uEs3GLRyT2mSajGk58Bk5Ec1uo0')
