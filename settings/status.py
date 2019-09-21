async def rotate(discord, client):
    guild_count = str(len(client.guilds))
    guilds_message = guild_count + ' server'

    if guild_count != '1':
        guilds_message += 's'

    game = discord.Activity(**{
        'name': guilds_message,
        'type': discord.ActivityType.listening
    })

    await client.change_presence(status=discord.Status.online, activity=game)