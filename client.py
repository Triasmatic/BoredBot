import discord
import secret

class client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {sef.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

cli = client(intents = intents)
cli.run(secret.BOT_ID)
