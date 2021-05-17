import re
import discord
import asyncio

class Command:
    func = None
    regex = None
    def __init__(self, regex: str, func=None):
        self.regex = regex
        if func is not None:
            if not asyncio.iscoroutinefunction(func):
                print('Function given to command isn\'t a coroutine.')
                func = None
        self.func = func

class CommandWrapper:
    client = None
    commands = set()
    def __init__(self, client: discord.Client, commands=None):
        if commands is None:
            commands = set()
        self.commands = commands
        self.client = client
        client.event(self.on_message)
    
    def register_command(self, command: Command):
        self.commands.add(command)
    
    async def process_commands(self, message: discord.Message):
        for comm in self.commands:
            if type(comm) == Command:
                reg = re.compile(comm.regex)
                search = reg.search(message.content)
                if search is not None and comm.func is not None:
                    if not asyncio.iscoroutinefunction(comm.func):
                        print('Function given to command isn\'t a coroutine. Command ignored')
                    else:
                        await comm.func(message, search.groupdict())
            else:
                print(f'Registered command {repr(comm)} is not a command. Ignored')

    async def on_message(self, message):
        await self.process_commands(message)