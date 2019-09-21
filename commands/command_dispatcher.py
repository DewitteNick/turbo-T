from . import command_functions
from . import command_list

# This command checks the message for commands, and takes care of calling it + handling the message.
async def dispatch_command(message):
    text = str.split(message.content, ' ')

    # Display help & abort if the command is not found.
    if not command_list.command_exists(text[0]):
        await command_functions.help(message)
        return

    # Invoke the help command.
    if text[0] == '$help':
        await command_functions.help(message)
    # Invoke the dice command.
    elif text[0] == '$dice':
        await command_functions.dice(message)
    # Invoke the broadcast command.
    elif text[0] == '$broadcast':
        await command_functions.broadcast(message)
    # Invoke the add_bot command.
    elif text[0] == '$add_bot':
        await command_functions.add_bot(message)
