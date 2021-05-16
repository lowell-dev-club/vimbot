# TO MAKE A DISCORD APPLICATION AND BOT GO TO THIS LINK:
# https://discord.com/developers/applications

# Here we're making our imports from discord
# Also getting our discord token which we have kept secret
# Important to hide key or else bad stuff happens
import discord
from discord.ext import commands
from secret import DISCORD_TOKEN # This is the token for our discord bot IMPORTANT
import random

# Here we're creating a client object for our bot
# Here we can create functions for when the user calls the bot with a specific command
# as you can see we can call the bot with the prefix '.'
client = commands.Bot(command_prefix=".")
token = DISCORD_TOKEN

# This is the initialization event for when the bot becomes active on the server
# There are specific events such as on_ready() and on_member_join()
# where the event will trigger a callback function that WE provide
@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
    print("I am online")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    # This is an important if statement
    # Guess what it does and why it's important
    if message.author == client.user:
        return

    quotes = ['General Kenobi', 'Hello There', 'Hi']

    if message.content == 'Hello there.':
        response = random.choice(quotes)
        await message.channel.send(response)

    # Await the client to process the commands
    # We wait because the commands are async functions and we don't know when they'll complete
    await client.process_commands(message) # This will send the message ot the process commands function which will handle our command identifiers

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