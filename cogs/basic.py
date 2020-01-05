import time
import config
import discord
from discord.ext import commands
from discord.ext.commands import Cog

class Basic(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """Says hello. Duh."""
        await ctx.send(f"Hello {ctx.author.mention}!")
        
    @commands.command(aliases=['es', "piracy"])
    async def patches(self, ctx):
        """Yeet"""
        await ctx.send("For pirated eshop-games you need ES signature patches. As their only purpose is to allow piracy we\'re not providing any help with installation of said patches or pirated games afterwards")

    @commands.command(aliases=["fat32"])
    async def exfat(self, ctx):
        """Displays a helpful message on why not to use exFAT"""
        embed = discord.Embed(title="GUIFormat",
                              url="http://www.ridgecrop.demon.co.uk/guiformat.exe",
                              description="A useful tool for formatting SD cards over 32GB as FAT32 on Windows.")
        message_text=("The exFAT drivers built into the Switch has been known "
                      "to corrupt SD cards and homebrew only makes this worse. "
                      "Backup everything on your SD card as soon as possible "
                      "and format it to FAT32. On Windows, if your SD card is "
                      "over 32GB then it will not let you select FAT32 from "
                      "the built-in format tool, however you can use a tool "
                      "like GUIFormat to format it.")
        await ctx.send(content=message_text,
                       embed=embed)
        
    @commands.guild_only()
    @commands.command()
    async def communitycount(self, ctx):
        """Prints the community member count of the server."""
        community = ctx.guild.get_role(config.named_roles["community"])
        await ctx.send(f"{ctx.guild.name} has "
                       f"{len(community.members)} community members!")

    @commands.guild_only()
    @commands.command()
    async def membercount(self, ctx):
        """Prints the member count of the server."""
        await ctx.send(f"{ctx.guild.name} has "
                       f"{ctx.guild.member_count} members!")

    @commands.command(aliases=["robocopng", "robocop-ng"])
    async def robocop(self, ctx):
        """Shows a quick embed with bot info."""
        embed = discord.Embed(title="Komet",
                              url=config.source_url,
                              description=config.embed_desc)

        embed.set_thumbnail(url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(aliases=['p', "ddos"])
    async def ping(self, ctx):
        """Shows ping values to discord.

        RTT = Round-trip time, time taken to send a message to discord
        GW = Gateway Ping"""
        before = time.monotonic()
        tmp = await ctx.send('Calculating ping...')
        after = time.monotonic()
        rtt_ms = (after - before) * 1000
        gw_ms = self.bot.latency * 1000

        message_text = f":ping_pong:\n"\
                       f"rtt: `{rtt_ms:.1f}ms`\n"\
                       f"gw: `{gw_ms:.1f}ms`"
        self.bot.log.info(message_text)
        await tmp.edit(content=message_text)


def setup(bot):
    bot.add_cog(Basic(bot))
