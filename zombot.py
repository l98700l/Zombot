# Work with Python 3.6
import random
import player
#import zombie
import asyncio
import discord


BOT_PREFIX = "!"
TOKEN = "NDk4NjAxNDU2NzM2MTQxMzEy.DpwGxg.wy7GUYQTsQYMvYKzNMHAtI7kBeQ"

client = discord.Client()
myChan = []

@client.event
async def on_ready():
    print("Logged in as " + client.user.name)
    print("ver: " +str(discord.__version__))

@client.event
async def on_message(message):
    print(message.content)
    if message.content[0] != '!':
        return
    
    args = message.content.split(' ')
    print(args[0])
    if args[0] == '!clear': #!clear (clears all messages)
        deleted = await message.channel.purge()
        await message.channel.send('Deleted {} message(s)'.format(len(deleted)))
        
    if message.content.startswith('!new'): #!new (creates a new Player)
        myPlayer = player.Player()
        print("Created Character " + myPlayer.name)
    if message.content.startswith('!del'):
        await message.guild.delete_channel(discord.utils.get(client.get_all_channels(), name="test"))
        print("Deleted Channel")
        
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print("-" + server.name)
        await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run(TOKEN)
