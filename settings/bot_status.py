import discord
import asyncio
import itertools
# Import local files
from responses import response_generator

async def action_rotate(client):
    bot_activity_list = await response_generator.bot_activity_list(client)
    bot_activities = itertools.cycle(bot_activity_list)

    while not client.is_closed():
        bot_activity = next(bot_activities)
        await client.change_presence(activity=bot_activity['activity'])
        await asyncio.sleep(bot_activity['weight'] * 12)
