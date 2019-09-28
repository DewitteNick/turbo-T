async def respond_channel(message, reply):
    await message.channel.send(reply)

async def respond_server_channels(message, reply):
    broadcast_author = message.author
    guild = message.channel.guild

    for channel in guild.text_channels:
        author_can_write = channel.permissions_for(broadcast_author).send_messages
        bot_can_write = channel.permissions_for(guild.me).send_messages

        if author_can_write and bot_can_write:
            await channel.send(reply)
