import discord
from discord import guild
from discord import member
import datetime 

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Over this Server"))
    print("Dev Bot is active")

# main function
@client.event
async def on_member_join(member):
    guild = client.get_guild('server_id_here')
    channel = guild.get_channel('channel_id_here')
    await channel.send(f"Welcome to the developer's server  {member.mention} ! :partying_face:")
    await member.send(f"Welsome to the {guild.name} server, {member.name}! :partying_face:")

@client.event
async def on_message(message):
    if message.content == 'hi':
        await message.channel.send(f"Hi!")

token = 'app_token'
client.run(token)
