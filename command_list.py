


commands = {
    'help': {
        'name': '$help',
        'help_message': 'Display help about a command.',
        'usage': '$help <command>'
    },
    '8ball': {
        'name': '$8ball',
        'help_message': 'Answer a yes/no question.',
        'usage': '$8ball <yes/no question>'
    },
    'ban': {
        'name': '$ban',
        'help_message': 'Ban an user. Users can\'t rejoin when banned. Requires the ban user permission.',
        'usage': '$ban <username> OR $ban <nickname>'
    },
    'unban': {
        'name': '$unban',
        'help_message': 'Unban an user. They need to be invited afterwards. Requires the ban user permission.',
        'usage': '$ban <username>'
    },
    'server_invite': {
        'name': '$server_invite',
        'help_message': 'Generate a link to invite people to this server.',
        'usage': '$server_invite'
    },
    'add_bot': {
        'name': '$add_bot',
        'help_message': 'Generate a link to add this bot to a server you own.',
        'usage': '$add_bot'
    },
        'broadcast': {
            'name': '$broadcast',
            'help_message': 'Send a message to all text channels you have write permission in.',
            'usage': '$broadcast <text you want to broadcast>'
    },
    'dice': {
        'name': '$dice',
        'help_message': 'Roll a dice with a specified number of sides. The number should be 2 or more.',
        'usage': '$dice <number>'
    },
    'radio': {
        'name': '$radio',
        'help_message': 'Control the behaviour of the bot in voice channels. Requires the `turbo-T_commander` role.\n(once it\'s finished...)', #TODO
        'usage': '$radio <action>',
        'examples': {
            '$radio join <voice channel>': 'Join the mentioned channel. Must be a voice channel.',
            '$radio play': 'Start radio playback',
            '$radio stop': 'Stop radio playback',
            '$radio abort': 'Stop radio playback and leave channel'
        }
    }
}


def command_exists(command):
    return command.strip('$') in commands


async def get_command_help(command):
    info = None
    if command_exists(command.strip('$')):
        info = commands[command.strip('$')]
    return info


async def get_commands():
    command_list = []
    for command in commands:
        command_list.append(commands[command]['name'])
    return command_list
