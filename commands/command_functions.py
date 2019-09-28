import discord
# Import local files
from responses import response_submitter
from responses import response_generator
from . import command_list

async def help(message):
    subject = str.strip(str.replace(message.content, '$help', ''))

    # User wrote "$help".
    if subject == '':
        await response_submitter.respond_channel(message, await response_generator.help_message())
    # User called the help command with arguments.
    elif command_list.command_exists(subject):
        command_data = await command_list.get_command_help(subject)

        await response_submitter.respond_channel(message, await response_generator.help_command_message(command_data))
    # User wrote gibberish starting with $.
    else:
        await response_submitter.respond_channel(message, await response_generator.invalid_command())

async def dice(message):
    size = str.strip(str.replace(message.content, '$dice', ''))

    if size == '':
        response = await response_generator.dice_roll(message, 20)
    elif size.isdigit():
        response = await response_generator.dice_roll(message, int(size))
    else:
        response = await response_generator.dice_roll(message, None)

    await response_submitter.respond_channel(message, response)

async def broadcast(message):
    text = str.strip(str.replace(message.content, '$broadcast', ''))
    await response_submitter.respond_server_channels(message, text)

async def add_bot(message):
    await response_submitter.respond_channel(message, await response_generator.generate_add_bot_link(message))

async def ban(message):
    # The user doesn't have permission to ban others.
    if not message.author.permissions_in(message.channel).ban_members:
        await response_submitter.respond_channel(message, await response_generator.get_permission_denied(message, 'user_cant_ban'))
    else:
        name_to_ban = str.strip(str.replace(message.content, '$ban', ''))
        member_to_ban = message.guild.get_member_named(name_to_ban)

        try:
            # Check if we're allowed to ban members.
            if message.guild.me.permissions_in(message.channel).ban_members:
                await member_to_ban.ban()
            else:
                raise discord.Forbidden()
        # Some members can't be banned.
        except discord.Forbidden:
            await response_submitter.respond_channel(message, await response_generator.get_permission_denied(message, 'bot_cant_ban'))
