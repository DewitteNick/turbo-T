import response_submitter
import asyncio
import text_generator
import commands
import config


async def execute_command(client, message):
    # Help command
    if message.content.startswith('$help '):
        await commands.help(client, message)

    # 8ball command
    elif message.content.startswith('$8ball'):
        await commands.eight_ball(client, message)
        # 8ball should not delete the question
        return

    # Ban command
    elif message.content.startswith('$ban'):
        await commands.ban(client, message)

    # Unban command
    elif message.content.startswith('$unban'):
        await commands.unban(client, message)

    # Server invite
    elif message.content.startswith('$server_invite'):
        await commands.server_invite(client, message)

    # Add bot to server
    elif message.content.startswith('$add_bot'):
        await commands.add_bot_to_server(client, message)

    # Broadcast an announcement to all text channels on the server
    elif message.content.startswith('$broadcast'):
        await commands.broadcast(client, message)

    # N-sided die
    elif message.content.startswith('$dice'):
        await commands.dice(client, message)

    # Voice channel music playback
    elif message.content.startswith('$radio'):
        await commands.radio(client, message)

    # Default message when command is not found.
    else:
        await response_submitter.reply_channel(client, message, await text_generator.command_not_found())

    #remove the command the user entered to keep chat a bit cleaner
    await client.delete_message(message)


async def respond_to_words(client, message, words):
    response = await text_generator.generate_response(words)
    word_in_message = False

    for word in words:
        if word in message.content.split():
            word_in_message = True

    if word_in_message:
        await response_submitter.reply_channel(client, message, response)


async def strip_command(message):
    command = message.split(' ')[0] + ' ' #TODO changed message.content.split to message.split. check for occurences in code.
    command_data = message[len(command):]
    return command_data


async def update_status(client):        # Limit of ~ 5 changes per minute
    while True:
        # Display current server goal
        if len(client.servers) >= config.get_server_target():
            await commands.set_status(client, 'Reached ' + str(len(client.servers)) + ' active servers!')
        else:
            await commands.set_status(client, 'Almost ' + str(config.get_server_target()) + ' active servers!')
        await asyncio.sleep(10)
        # Display current users
        users = 0
        for server in client.servers:
            for user in server.members:
                if not user.bot:
                    users += 1
        await commands.set_status(client, 'Serving ' + str(users) + ' users')
        await asyncio.sleep(10)
        # Display help
        await commands.set_status(client, 'start commands with $')
        await asyncio.sleep(20)


async def get_voice_client(client, message):
    voice_client = None
    for vc in client.voice_clients:
        if message.server is vc.server:
            voice_client = vc
    return voice_client
