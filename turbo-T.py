# Import Python libraries
import discord
import time
# Import local files
from settings import localsettings
from commands import command_dispatcher

print('booting turbo-T')
print('Version:\t' + discord.__version__ + '\n')

TOKEN = localsettings.get_token()
client = discord.Client()


@client.event
async def on_message(message):
    # Prevent the bot from responding to any bot. This also prevents the bot from responding to itself.
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        await command_dispatcher.dispatch_command(message)
        # Don't continue executing this function.
        return

    # If no commands are detected, check if we should check a miscellaneous reply.

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('ID', client.user.id, sep=': ')
    print('ready timestamp', time.time(), sep=': ')
    print('------')

client.run(TOKEN)
