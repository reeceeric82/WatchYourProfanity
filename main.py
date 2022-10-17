import discord
import os
import random
from dotenv import load_dotenv
from resources import gifs, swearwords

load_dotenv()
TOKEN = os.getenv("d_token")

# with open("swears.txt", "r") as wordlist:
#     swearwords = list(wordlist.read().split())


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

        user_message = message.content.lower().split()

        for index, word in enumerate(user_message):
            for swear in swearwords:
                if user_message[index] == swear:
                    message_safe = False
                    user_message[index] = "▂" * len(word)
                    censored_message = " ".join(user_message)

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
