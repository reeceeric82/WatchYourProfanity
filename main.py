import discord
import os
import random
from dotenv import load_dotenv
from resources import gifs, swearwords
from checker import censor_text, is_safe

load_dotenv()
TOKEN = os.getenv("d_token")


class myClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")

    async def on_message(self, message):
        message_safe = True
        gif = random.choice(gifs)
        test = str(message.content)

        print(f"Message from {message.author}: {test}")

        if message.author == self.user:
            return

        text = message.content.lower()

        message_safe = is_safe(text, swearwords)
            
        censored_message = censor_text(text, swearwords)

        if not message_safe:

            await message.reply(f"@{message.author} said: {censored_message}\n" + gif, mention_author=True)
            await message.delete(delay=None)

intents = discord.Intents.default()
intents.message_content = True

client = myClient(intents=intents)

if __name__ == "__main__":
    print(swearwords)
    print(gifs)
    client.run(TOKEN)

