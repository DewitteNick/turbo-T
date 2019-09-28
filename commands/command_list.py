commands = {
    'help': {
        'name': '$help',
        'help_message': 'Display help about a command.',
        'usage': '$help <command>'
    },
    'add_bot': {
        'name': '$add_bot',
        'help_message': 'Generate a link to add this bot to a server you own.',
        'usage': '$add_bot'
    },
    'ban': {
        'name': '$ban',
        'help_message': 'Ban an user. Users can\'t rejoin when banned. Requires the ban user permission. Can be a username (+ optional discriminator) or nickname. username + discriminator is preferred.',
        'usage': '$ban <username> OR $ban <nickname>'
    },
    'broadcast': {
        'name': '$broadcast',
        'help_message': 'Send a message to all text channels in the current category. Requires send messages permission.',
        'usage': '$broadcast <text you want to broadcast>'
    },
    'dice': {
        'name': '$dice',
        'help_message': 'Roll a dice with a specified # of sides. The number should be 2 or more. If no # of sides is specified, 20 is assumed',
        'usage': '$dice <number>'
    },
    'unban': {
        'name': '$unban',
        'help_message': "Unban an user. They need to be invited afterwards. Requires the ban user permission. Nicknames don't work",
        'usage': '$ban <username>'
    },
}

async def get_commands():
    command_list = []
    for command in commands:
        command_list.append(commands[command]['name'])
    return command_list

async def get_command_help(command):
    info = None
    if command_exists(command.strip('$')):
        info = commands[command.strip('$')]
    return info

def command_exists(command):
    return command.strip('$') in commands
