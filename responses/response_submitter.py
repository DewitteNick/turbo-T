async def respond_channel(message, reply):
    await message.channel.send(reply)

async def respond_server_channels(message, reply):
    guild = message.channel.guild

    for channel in guild.text_channels:
        await channel.send(reply)