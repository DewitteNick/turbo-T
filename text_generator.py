import random
import command_list


async def generate_response(words):
    if 'hi' in words:
        response = 'Greetings {0.author.mention}'
    else:
        response = 'I don\'t really know what to say...'

    return response


async def generate_help(command):
    response = '```AsciiDoc\n'
    response += command['name'] + ':: ' + command['usage']
    response += '\n== ' + command['help_message']
    response += '```'
    return response


async def command_not_found(response):
    # if (invalid_command):
    #     response = 'Command could not be found.'
    # else:
    #     response = 'No command specified.'
    response += '\nTry `$help <command>` for info about a command.'
    response += '\nList of valid commands:\n'
    response += '```AsciiDoc\n'
    for existing_command in await command_list.get_commands():
        response += '\n' + existing_command.replace('_', '＿')       #TODO temp hack to disable multiline italics in asciidoc
    response += '```'
    return response


async def get_eight_ball_reply():       #TODO actual 8ball answers --> https://en.wikipedia.org/wiki/Magic_8-Ball#Possible_answers
    options = {
        0: 'Unlock the EAnswer for $3.99 only!',
        1: 'My 8ball says you should.',
        2: 'My sources say no.',
        3: 'As certainly as terry loves yoghurt.',
        4: 'I can\'t make a woman\'s choice for her.',
        5: 'You should go for it, ful Boyle style.',
        6: 'See \'Rules of the internet\' #17',
        7: 'Yes. Sure. Go ahead.'
    }
    return options[random.randint(0, len(options) - 1)]


async def get_eight_ball_error():
    error = 'You need to ask me something, dummy!'
    return error


async def get_permission_denied(message, permission):
    if permission == 'ban':
        return message.author.mention + ', leave banning to the big guys...'


async def get_banned_message(banned_member):
    return banned_member.mention + ', you just got https://www.tenor.co/JZWk.gif'


async def get_invalid_member_ban_error():
    return '*Swings banhammer at non-existant member*'
