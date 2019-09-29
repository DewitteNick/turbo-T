# Import Python libraries
import discord
import time
# Import local files
from settings import localsettings
from commands import command_dispatcher
from settings import bot_status

print('booting turbo-T')
print('Version:\t' + discord.__version__ + '\n')

TOKEN = localsettings.get_token()
client = discord.Client()


@client.event
async def on_message(message):
    # Prevent the bot from responding to any bot. This also prevents the bot from responding to itself.
    if message.author == client.user:
        return

    # If a potential command is detected, launch the command dispatcher.
    if message.content.startswith('$'):
        await command_dispatcher.dispatch_command(message)
        # Don't continue executing this function.
        return
    # If no potential commands are detected, check if we should send a miscellaneous reply.
    else:
        await command_dispatcher.dispatch_miscelaneous(message)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('ID', client.user.id, sep=': ')
    print('ready timestamp', time.time(), sep=': ')
    print('------')
    client.loop.create_task(bot_status.action_rotate(client))

client.run(TOKEN)
