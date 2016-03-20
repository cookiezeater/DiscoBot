# -*- coding: utf-8 -*-

import logging, random, json

from disco.config import Config
from discord import Message, Channel, Member, Server, Role, VoiceClient
from discord.ext import commands
from discord import utils, opus

logger = logging.getLogger("disco")

class Music:

    def __init__(self, bot):
        self.bot = bot
        self.key = self.__class__.__name__

        self.follow = True
        self.vclients = {}
        self.listeners = []
        self.rtv = None
        self.playlist = []
        self.loop = False

    async def on_ready(self):
        logger.info("Opus loaded: {}".format(opus.is_loaded()))

        if self.follow:
            logger.info("Follow enabled.")
            for server in self.bot.servers:
                await self.join_member(server, Config.OWNER_ID)

    async def join_member(self, server, user_id):
        """Given a server, seek out the owner and join
        the current voice channel he is in, if it exists.
        """
        member = utils.get(server.members, id=user_id)
        if member is not None:
            logger.debug("Found member: {}".format(member.name))
            vchan = member.voice_channel
            if vchan is not None:
                logger.info("Joining voice channel: {}".format(vchan.name))
                if server.id not in self.vclients:
                    logger.debug("Creating voice client with ID: {}".format(server.id))
                    self.vclients.update({ server.id: { "client": None, "player": None }})
                self.vclients[server.id]["client"] = await self.bot.join_voice_channel(vchan)
                logger.debug("Voice connectd: {}".format(self.vclients[server.id]["client"].is_connected()))
            else:
                logger.debug("No voice channel found.")
        else:
            logger.debug("Member not found.")

    def get_player(self, ctx):
        voice = self.vclients[ctx.message.server.id]
        return voice["player"]

    def get_client(self, ctx):
        voice = self.vclients[ctx.message.server.id]
        return voice["client"]

    async def init_player_with_url(self, server, url):
        voice = self.vclients[server.id]
        voice["player"] = await voice["client"].create_ytdl_player(url)
        logger.info("Created new player ({}).".format(voice.channel.name))
        return voice["player"]

    @commands.command(pass_context=True, no_pm=True)
    async def follow(self, ctx):
        await self.join_owner_on_server(ctx.message.server, ctx.message.author.id)

    @commands.command(pass_context=True, no_pm=True)
    async def play(self, ctx, url : str):
        player = await self.init_player_with_url(ctx.message.server, url)
        player.start()

    @commands.command(pass_context=True, no_pm=True)
    async def stop(self, ctx):
        player = get_player(ctx)
        player.stop()

    @commands.command(pass_context=True, no_pm=True, aliases=["q", "que"])
    async def queue(self, ctx, url : str):
        player = get_player(ctx)
        if player.is_playing():
            player.stop()
            logger.debug("Stopping player in progress")
        voice["player"] = await voice["client"].create_ytdl_player(url)
        voice["player"].start()

def setup(bot):
    bot.add_cog(Music(bot))
