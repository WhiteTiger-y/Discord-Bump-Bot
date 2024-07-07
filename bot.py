import asyncio
import discord
from discord.ext import commands, tasks
import json
import os
from dotenv import load_dotenv


# Load the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CLIENT_ID = os.getenv('DISCORD_CLIENT_ID')  # Add this line to get the client ID from

# Set up the bot
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Dictionary to store guild-specific channel IDs
bump_channels = {}

# Load bump channels from file
if os.path.exists('bump_channels.json'):
    with open('bump_channels.json', 'r') as f:
        bump_channels = json.load(f)

def save_bump_channels():
    with open('bump_channels.json', 'w') as f:
        json.dump(bump_channels, f)

@bot.event
async def on_ready():
    # Ensure the bot is ready before accessing bot.user
    if bot.user:
        print(f'{bot.user.name} has connected to Discord!')
        for guild_id in bump_channels:
            bump.start(guild_id)

@bot.event
async def on_guild_join(guild):
    def check(m):
        return m.author == guild.owner and m.channel in guild.text_channels

    try:
        permissions_int = 92184  # The calculated permissions integer
        invite_url = f"https://discord.com/oauth2/authorize?client_id={CLIENT_ID}&scope=bot&permissions={permissions_int}"
        await guild.owner.send(
            f"Hi! Please invite the bot with the necessary permissions using this link: {invite_url}"
        )
        await guild.owner.send(
            "Which channel would you like to use for the /bump command? "
            "Please mention the channel."
        )
        msg = await bot.wait_for('message', check=check, timeout=300)  
        channel_id = int(msg.content[2:-1])
        bump_channels[guild.id] = channel_id
        save_bump_channels()
        await guild.owner.send(f"Bump command will be sent in "
              f"<#{channel_id}> every 130 minutes.")
        bump.start(guild.id)
    except asyncio.TimeoutError:
        await guild.owner.send(
            "You didn't mention a channel in time. "
            "Please use the `!setbumpchannel` command to set it later."
        )

@bot.command(name='setbumpchannel')
async def set_bump_channel(ctx, channel: discord.TextChannel):
    bump_channels[ctx.guild.id] = channel.id
    save_bump_channels()
    await ctx.send(f"Bump command will be sent in {channel.mention} every 130 minutes.")
    bump.start(ctx.guild.id)

@tasks.loop(minutes=130)
async def bump(guild_id):
    channel_id = bump_channels.get(guild_id)
    if channel_id:
        channel = bot.get_channel(channel_id)
        if channel:
            if isinstance(channel, discord.TextChannel):  # Check if it's a text channel
                await channel.send('/bump')
            else:
                print(f"Channel with ID {channel_id} is not a text channel")
        else:
            print(f"Channel with ID {channel_id} not found")
    else:
        print(f"No bump channel set for guild with ID {guild_id}")

if TOKEN is None:
    print("Error: DISCORD_TOKEN environment variable not found.")
    exit()
else:
    bot.run(TOKEN)
