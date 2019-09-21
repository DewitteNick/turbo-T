import discord
import functions
import time
from settings import localsettings

print('Version:\t' + discord.__version__ + '\n')


TOKEN = localsettings.get_token()

client = discord.Client()


@client.event
async def on_message(message):
    # Prevent the bot from responding to any bot. This also prevents the bot from responding to itself.
    if message.author.bot:
        return

    # Respond to commands starting with '$'
    if message.content.startswith('$'):
        await functions.execute_command(client, message)
        return

    #Execute these last, they should not be executed if a response is already sent.
    await functions.respond_to_words(client, message, ['hi', 'hello', 'hey', 'hola', 'aloha', 'hallo'])


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('ID', client.user.id, sep=': ')
    print('ready timestamp', time.time(), sep=': ')
    print('------')
    # await commands.set_status(client, 'use $help for info')


client.run(TOKEN)
