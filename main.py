import discord
import os

client = discord.Client()

@client.event #when message is recieved
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event #when bot makes message
async def on_message():
    if message.author == client.user: #if the author of the message comes from the bit
        return #do nothing

    if message.content.startswith('$hello'): #test
        await message.channel.send('Hello!')


client.run(os.getenv('TOKEN'))