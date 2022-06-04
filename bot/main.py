import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user: 
        return
    
    if message.content.lower() in ['hello', 'hi', 'buna']:
        await message.channel.send(f'Hi {message.author.mention}')
    if message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author.mention}')
    # 
    if message.content.lower() == 'poza':
        await message.channel.send(f'https://media.giphy.com/media/TR0FU9ushLPUX9E6zQ/giphy.gif')


    await bot.process_commands(message)
    
if __name__ == "__main__":
    bot.run(TOKEN)
