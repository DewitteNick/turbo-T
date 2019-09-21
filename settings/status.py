import time
import discord

async def rotate(client):
    bot_status = discord.Status.online

    # Display the startup message once for 10 seconds.
    guilds_message = 'bot startup'
    bot_state = 'Launching'

    bot_activity = discord.Activity(**{
        'name': guilds_message,
        'type': discord.ActivityType.playing,
        'state': bot_state,
    })

    await client.change_presence(status=bot_status, activity=bot_activity)
    time.sleep(10)

    # Change the type from playing to listening once.
    bot_activity.type = discord.ActivityType.listening

    while True:
        # Display the "Listening to x servers" message for 10 seconds.
        guild_count = str(len(client.guilds))
        guilds_message = guild_count + ' server'

        if guild_count != '1':
            guilds_message += 's'

        bot_activity.name = guilds_message

        await client.change_presence(status=bot_status, activity=bot_activity)
        time.sleep(10)

        # Display the "Listening to $help" message for 50 seconds.
        bot_activity.name = 'test'

        await client.change_presence(status=bot_status, activity=bot_activity)
        time.sleep(50)
