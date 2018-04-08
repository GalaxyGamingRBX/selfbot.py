import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import datetime

Client = discord.Client()
client = commands.Bot(command_prefix = ".")

@client.event
async def on_message(message):
    if message.author.id == "275050046955716609":
       if message.content == ".ping":
          await client.say("Ooooo")

await client.login('zaneaswierz@gmail.com', 'Zane0610')
