token = "NzE2MjI5ODA3NTg2OTM0ODM2.XtIvKQ.BQMEdASb7gaEkDg8vY6fRHpBSyw" 
userid = "582630359028727809" #You own UserID
prefix = "~" #Prefix for command


import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
from random import randrange

print("Snooze")

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Do " + prefix + " to run Snooze.")

try:
    async def self_check(ctx):
        if bot.user.id == userid or ctx.message.author.id:
            return True
        else:
            return False
        
    @bot.command(pass_context=True)
    async def join(ctx):
        try:
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.send(f"`Snooze has joined {channel} at your request: {ctx.message.author}`")
        except:
            await ctx.send(f"You are not connected to any Voice Channel: {ctx.message.author}")
        
    @bot.command(pass_context=True)
    async def leave(ctx):
        try:
            await ctx.voice_client.disconnect()
        except:
            await ctx.send(f"Snooze is already disconnected from the Voice Channels: {ctx.message.author}")
            
    @bot.command(pass_context=True)
    async def about(ctx):
        await ctx.send(f"```Snooze is a revolutionary music bot. Easily play your Spotify playlist with Snooze and much more!```")

  
except:
    pass

bot.run(token)