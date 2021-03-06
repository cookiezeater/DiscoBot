# -*- coding: utf-8 -*-
"""
DiscoBot the Amazing Chat Companion
"""

import logging, json
from disco import checks
from .config import Config
from .utils import configure_logger, get_destination

import discord, asyncio
from discord.ext import commands
from discord.ext.commands import Context
from discord import Message, Channel, Member, Server, Role

configure_logger("disco", stream=True, level=Config.LOGGING_LEVEL)
configure_logger("discord", stream=False, level=Config.LOGGING_LEVEL)

logger = logging.getLogger("disco")


#class DiscoBot(commands.Bot):
#	"""DiscoBot the Amazing Chat Companion"""
#
#	def __init__(self, *args, **kwargs):
#		super().__init__(*args, **kwargs)
#
#		missing_token = Config.DISCORD_TOKEN is None
#		if missing_token:
#			raise AttributeError("Missing token.")
#
#		self.lockdown = False
#
#	#async def go(self):
#	#	"""Go, go, go"""
#		#logger.debug(Config.DISCORD_TOKEN)
#		#await self.login(Config.DISCORD_TOKEN)
#	#	super().run()
#
#	def register_extensions(self, extension: [str]):
#		"""Register the required cogs"""
#		logger.info("Loading extension...")
#		try:
#			for ext in extensions:
#				logger.info(" loaded cog: {0}".format(ext))
#				self.load_extension(ext)
#		except Exception as e:
#			logger.error("Error loading extension \'{0}\': {1}".format(ext, e))


desc = """Disco the Amazing Chat Companion.
The number one Discord bot for useless things.

Written by Syntox32 with Python 3.5.1 and the discord.py API wrapper by rapptz
DiscoBot at GitHub: github.com/Syntox32/DiscoBot

Find me on discord @syn


List of commands by category:
"""

extensions = [
	"disco.cogs.meme",
	"disco.cogs.reddit",
	"disco.cogs.misc",
	"disco.cogs.tags",
	"disco.cogs.mood",
	"disco.cogs.music",
]

if Config.DISCORD_TOKEN is None:
	raise AttributeError("Missing token.")

bot = commands.Bot(command_prefix=["!", "?"], description=desc)
bot.lockdown = False

def register_extensions(extension: [str]):
	"""Register the required cogs"""
	logger.info("Loading extension...")
	try:
		for ext in extensions:
			logger.info(" loaded cog: {0}".format(ext))
			bot.load_extension(ext)
	except Exception as e:
		logger.error("Error loading extension \'{0}\': {1}".format(ext, e))

register_extensions(extensions)


@bot.event
async def on_ready():
	"""On ready message"""
	logger.info("Connected!")
	logger.info("Username: {0}".format(bot.user.name))
	logger.info("ID: {0}".format(bot.user.id))

	bot.commands_executed = 0
	bot.verbose = True if Config.LOGGING_LEVEL is logging.DEBUG else False
	logger.info("High verbosity set to {}".format(str(bot.verbose)))

@bot.event
async def on_command(command, ctx: Context):
	"""Called whenever a command is called"""
	bot.commands_executed += 1
	dest = get_destination(ctx.message)
	logger.info("{0.author.name} in {1}: {0.content}".format(ctx.message, dest))

@bot.event
async def on_message(message: Message):
	"""Called when a message is created and sent to a server."""

	# If we're in lockdown, just answer to the owner
	if bot.lockdown:
		if message.author.id != Config.OWNER_ID:
			return

	# if we override the on message we need to
	# make sure the bot sees the message if we want
	# any other on_message events to fire
	await bot.process_commands(message)

@bot.command(pass_context=True, no_pm=True)
async def id(ctx):
	"""Send a message with the user id of the author."""
	await bot.say("Your user ID is: {0}".format(ctx.message.author.id))

@bot.command(pass_context=True, no_pm=True, hidden=True)
async def servid(ctx):
	"""Send a message with the user id of the author."""
	await bot.say("This server ID is: {0}".format(ctx.message.server.id))

@bot.command(pass_context=True, hidden=True)
@checks.is_owner()
async def change_game_status(ctx, game : str):
	"""Change the playing status to a given label"""
	# if the name is equal to None, the playing status is removed
	if game == "":
		game = None
	await ctx.bot.change_status(discord.Game(name=game))

@bot.command(name="lockdown", pass_context=True, hidden=True)
@checks.is_owner()
async def _lockdown(ctx):
	"""Locks down the bot to only respond to commands from the owner"""
	bot.lockdown = not bot.lockdown
	if bot.lockdown:
		await bot.say("I'm now in lockdown mode.")
	else:
		await bot.say("I'm now out of lockdown mode.")

@bot.command(pass_context=True, hidden=True)
@checks.is_owner()
async def verbose(ctx):
	"""Toggle logging level between info and debug."""
	if bot.verbose:
		logger.setLevel(logging.INFO)
		bot.verbose = False
		await bot.say("Set log verbosity to INFO.")
	else:
		logger.setLevel(logging.DEBUG)
		bot.verbose = True
		await bot.say("Set log verbosity to DEBUG.")

@bot.command(pass_context=True, hidden=True, aliases=["quit"])
@checks.is_owner()
async def shutdown(ctx):
	bot.say("Sutting down.")
	await bot.logout()

@bot.command(pass_context=True, hidden=True)
@checks.is_owner()
async def debug(ctx, *, code : str):
	"""Evaluates code"""
	# Shamelessly stolen from Danny
	code = code.strip('` ')
	python = '```py\n{}\n```'
	result = None

	try:
		result = eval(code)
	except Exception as e:
		await bot.say(python.format(type(e).__name__ + ': ' + str(e)))
		return

	if asyncio.iscoroutine(result):
		result = await result

	await bot.say(python.format(result))

@bot.command(pass_context=True, no_pm=True, hidden=True)
@checks.is_owner()
async def rescue(ctx, count : int):
	"""Saves the the last n messages from the log in a file"""
	with open("shitsave.txt", "w") as f:
		async for message in bot.logs_from(ctx.message.channel, limit=count):
			obj = {
				"auth": message.author.name,
				"msg": message.content
			}
			f.write(json.JSONEncoder().encode(obj)+ "\n")

@bot.event
async def on_command_error(error, ctx):
	"""Called when a command raises an error"""
	if isinstance(error, commands.NoPrivateMessage):
		await ctx.bot.say("This command cannot be used in private messages.")

# Other events, uncomment as needed
# Having them uncommented all the time might
# cause some wierd behaviour with overrides sometimes(?)

#@bot.event
#async def on_error():
#	"""Override normal error handling behaviour"""
#	pass


#@bot.event
#async def on_channel_update(before: Channel, after: Channel):
#	"""Called whenever a channel is updated. e.g. changed name, topic, permissions."""
#	msg = "Channel changed name from {0} to {1}".format(before.name, after.name)
#	await self.bot.send_message(after, msg)

#@bot.event
#async def on_member_update(before: Member, after: Member):
#	"""Called when a Member updates their profile."""
#	pass

#@bot.event
#async def on_server_role_update(before: Role, after: Role):
#	"""Called when a Role is changed server-wide."""
#	pass

#@bot.event
#async def on_voice_state_update(before: Member, after: Member):
#	"""Called when a Member changes their voice state."""
#	pass
