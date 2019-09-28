# Import Python libraries
import random
import discord
# Import local files
from commands import command_list

async def bot_activity_list(client):
    types = discord.ActivityType
    guild_count_message = str(len(client.guilds)) + ' servers'

    return [
        {
            'weight': 5,
            'activity': discord.Activity(**{
                'name': '$help',
                'type': types.listening
            })
         },
        {
            'weight': 1,
            'activity': discord.Activity(**{
                'name': guild_count_message,
                'type': types.listening
            })
        },
    ]

async def help_message():
    response = 'Try `$help <command>` for info about a command.'
    response += '\nList of valid commands:\n'
    response += '```AsciiDoc\n'
    for existing_command in await command_list.get_commands():
        response += '\n' + existing_command.replace('_', '＿')       # Hack to disable multiline italics in asciidoc.
    response += '```'

    return response

async def help_command_message(command_data):
    response = '```AsciiDoc\n'
    response += command_data['name'] + ':: ' + command_data['usage']
    response += '\n== ' + command_data['help_message']
    response += '```'
    response = response.replace('_', '＿')                           # Hack to disable multiline italics in asciidoc.
    return response

async def invalid_command():
    response = 'Unable to process this command.'
    return response

async def dice_roll(message, sides):
    if sides is None:
        return 'Please provide a valid dice size.'
    else:
        response = message.author.display_name
        response += ' rolls '
        response += str(random.randint(1, sides))
        response += ' out of ' + str(sides)
        return response

async def generate_add_bot_link(message):
    permissions = '2146958583'
    id = str(message.guild.me.id )
    link = 'https://discordapp.com/api/oauth2/authorize?client_id=' + id + '&permissions=' + permissions + '&scope=bot'
    return link

async def get_permission_denied(message, permission):
    if permission == 'user_cant_ban':
        return message.author.mention + ', you seem to be a little out of your league here...'
    elif permission == 'bot_cant_ban':
        return message.author.mention + ', It seems I cannot be of assistance right now.\nhttps://tenor.com/view/arrowhead-australia-aussie-scifi-movie-gif-5657314'
