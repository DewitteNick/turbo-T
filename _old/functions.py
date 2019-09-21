from _old import text_generator, response_submitter, commands


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

    # Youtube search
    elif message.content.startswith('$yt'):
        await commands.yt_search(client, message)

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
    command = message.content.split(' ')[0] + ' '
    command_data = message.content[len(command):]
    return command_data
