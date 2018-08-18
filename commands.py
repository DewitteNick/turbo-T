import text_generator
import response_submitter
import command_list
import random
import discord
import functions
import time
from ctypes.util import find_library
import os


players = {}


async def help(client, message):
    keyword = await functions.strip_command(message.content)
    if command_list.command_exists(keyword):
        command_help = await command_list.get_command_help(keyword)
        response = await text_generator.generate_help(command_help)
    else:
        response = await text_generator.command_not_found()
    await response_submitter.reply_channel(client, message, response)


async def eight_ball(client, message):
    if message.content == '$8ball':
        await response_submitter.reply_channel(client, message, await text_generator.get_eight_ball_error())
        return
    reply = await text_generator.get_eight_ball_reply()
    await response_submitter.reply_channel(client, message, reply)


async def ban(client, message):
    # Message if you don't have the ban permission
    if not message.author.server_permissions.ban_members:
        await response_submitter.reply_channel(client, message, await text_generator.get_permission_denied(message, 'ban'))
        return

    # get the user to ban by name
    name_to_ban = await functions.strip_command(message.content)
    banned_member = message.server.get_member_named(name_to_ban)

    # ban an existing user, or show a message the user doesn't exist
    if banned_member is not None:
        await response_submitter.reply_channel(client, message, await text_generator.get_banned_message(banned_member))
        time.sleep(5)
        await client.ban(banned_member, 7)
    else:
        await response_submitter.reply_channel(client, message, await text_generator.get_invalid_member_ban_error())


async def unban(client, message):
    # Message if you don't have the ban permission
    if not message.author.server_permissions.ban_members:
        await response_submitter.reply_channel(client, message,
                                               message.author.mention + ', leave unbanning to the big guys...')
        return

    # get the user to unban by name
    name_to_unban = await functions.strip_command(message.content)
    banned_list = await client.get_bans(message.server)
    for user in banned_list:
        if user.name == name_to_unban:
            try:
                await client.unban(message.server, user)
                await response_submitter.reply_channel(client, message, 'Unbanned ' + user.name)
            except Exception as e:
                await response_submitter.reply_channel(client, message, 'Failed to unban ' + user.name)
                print(e)  # TODO add logging.


async def server_invite(client, message):
    invite = await client.create_invite(message.channel)
    await response_submitter.reply_channel(client, message, invite.url)


async def add_bot_to_server(client, message):
    client_id = client.user.id
    permissions = '2146958583'
    link = 'https://discordapp.com/api/oauth2/authorize?client_id=' + client_id + '&permissions=' + permissions + '&scope=bot'
    await response_submitter.reply_channel(client, message, link)


async def broadcast(client, message):
    response = await functions.strip_command(message.content)
    await response_submitter.reply_broadcast(client, message, response)


async def dice(client, message):
    size = await functions.strip_command(message.content)
    try:
        sides = int(size)
        if sides < 2:
            raise ValueError('Dice size should be 2 or higher')
        await response_submitter.reply_channel(client, message, message.author.nick + ' rolls ' + str(
            random.randint(1, sides)) + ' out of ' + str(sides))
    except TypeError as e:
        print(e.args)
        sides = int(size)
        if sides < 2:
            raise ValueError('Dice size should be 2 or higher')
        await response_submitter.reply_channel(client, message, message.author.name + ' rolls ' + str(
            random.randint(1, sides)) + ' out of ' + str(sides))
    except Exception as e:
        print(e.args) #TODO log?
        await response_submitter.reply_channel(client, message, size + ' is an invalid dice size!')


async def set_status(client, status):
    await client.change_presence(game=discord.Game(name=status))


async def radio(client, message):
    command = await functions.strip_command(message.content)
    parameter = await functions.strip_command(command)
    # Join discord voice channel
    if command.startswith('join'):
        await radio_join(client, message, parameter)
    # Start playing music
    elif command.startswith('play'):
        await radio_play(client, message)
    # Pause music playback
    elif command.startswith('pause'):
        players[message.server.id]['player'].pause()
    # Leave discord voice channel
    elif command.startswith('leave'):
        # No parameter
        voice_client = await functions.get_voice_client(client, message)
        await voice_client.disconnect()
        players.pop(message.server.id)
    # Invalid radio option
    else:
        await response_submitter.reply_channel(client, message, 'Invalid argument')


async def radio_join(client, message, channel_name):
    channel = None
    # Check if the server has a channel matching the specified name
    for ch in message.server.channels:
        if channel_name == ch.name:
            channel = ch
    # Check if the user is in a voice channel
    if channel is None:
        for ch in message.server.channels:
            if message.author in ch.voice_members:
                channel = ch
    # Join the voice channel, if any is found
    if channel is not None:
        await client.join_voice_channel(channel)
        discord.opus.load_opus(find_library('opus'))
    else:
        await response_submitter.reply_channel(client, message, 'No valid channel found.')


async def radio_play(client, message):

