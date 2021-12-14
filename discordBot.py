import os
import discord
import json
import requests
import random

client = discord.Client()
intents = discord.Intents.all()
intents.members = True

botCommand = discord.commands.bot(intents=intents,)


@client.event
async def on_ready():
  print("weweweaweaw".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('=selam'):
    await message.channel.send('naber you? ay ay ay im your litle butterfly')

  if message.content.startswith('=mal kuday'):
    await message.channel.send('doru')

  if message.content.startswith("=allmembers"):
    memberss = ["```", ]
    for i in get_all_members():
      memberss.append(i)


my_secret = os.environ['showMustGoOn']

client.run(my_secret)
