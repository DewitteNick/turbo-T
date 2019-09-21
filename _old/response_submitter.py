import discord


async def reply_channel(client, message, response):
    msg = response.format(message)
    await client.send_message(message.channel, msg)


async def reply_broadcast(client, message, response):
    for channel in client.get_all_channels():
        if channel.type == discord.ChannelType.text:
            if message.author.permissions_in(channel).send_messages:
                msg = response.format(message)
                try:
                    await client.send_message(channel, msg)
                except Exception as e:
                    await reply_channel(client, message, '```Failed to broadcast to channel: ' + channel.name + '\n' + str(e) + '```')
            else:
                await reply_channel(client, message, message.author.mention + ' can\'t write to channel "' + channel.name + '"')
