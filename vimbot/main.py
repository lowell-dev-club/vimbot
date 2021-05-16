# TO MAKE A DISCORD APPLICATION AND BOT GO TO THIS LINK:
# https://discord.com/developers/applications

# Here we're making our imports from discord
# Also getting our discord token which we have kept secret
# Important to hide key or else bad stuff happens
import discord
from discord.ext import commands
from secret import DISCORD_TOKEN # This is the token for our discord bot IMPORTANT

# Here we're creating a client object for our bot
# Here we can create functions for when the user calls the bot with a specific command
# as you can see we can call the bot with the prefix '.'
client = commands.Bot(command_prefix=".")
token = DISCORD_TOKEN

# This is the initialization event.
# 
@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
    print("I am online")

@client.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@client.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)


client.run(token)