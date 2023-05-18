import discord
import os
import random
from difflib import SequenceMatcher
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("d_token")

gifs = [
"https://media.giphy.com/media/WS3FLDbYaPQGY/giphy.gif",
"https://tenor.com/view/watch-your-mouth-watch-your-profanity-watch-it-gif-5600117",
"https://media.giphy.com/media/3o7TKwmnDgQb5jemjK/giphy.gif",
"https://media.giphy.com/media/vyTnNTrs3wqQ0UIvwE/giphy.gif",
"https://media.giphy.com/media/STfLOU6iRBRunMciZv/giphy.gif",
"https://media.giphy.com/media/3o6ZsYwfTnoKWREaY0/giphy.gif",
"https://media.giphy.com/media/5HyVZlZYxJPy7IC5Cz/giphy.gif",
"https://tenor.com/view/pakistan-cricket-fan-pakistan-fan-cricket-angry-fan-angry-fan-angry-man-gif-19825067",
"https://tenor.com/view/anger-annoyed-dwight-schrute-gif-11782657",
"https://tenor.com/view/why-whatever-gif-23592041",
"https://tenor.com/view/nacho-why-confused-jack-black-gif-8714598",
"https://tenor.com/view/why-friends-ross-geller-why-would-you-do-that-gif-4484708",
"https://tenor.com/view/why-asking-confused-gif-4593721",
"https://tenor.com/view/over-it-leave-me-alone-fuckoff-stressed-gif-15243809",
"https://tenor.com/view/stressed-face-im-right-im-on-the-verge-of-nervous-breakdown-nervous-breakdown-gif-4425233",
"https://tenor.com/view/deadpool-ryan-reynolds-shocked-shocking-omg-gif-7719836",
"https://tenor.com/view/you-were-nicer-as-a-kid-good-nicer-past-ryan-reynolds-gif-13034863",
"https://tenor.com/view/we-dont-do-that-here-black-panther-tchalla-bruce-gif-16558003",
"https://tenor.com/view/michael-scott-the-office-nope-no-disapprove-gif-5418568",
"https://tenor.com/view/critical-role-matt-mercer-matthew-mercer-allura-allura-vysoren-gif-15300593",
"https://tenor.com/view/absolutely-not-nope-no-no-way-no-chance-gif-17243246",
"https://tenor.com/view/nuh-uh-randy-marsh-south-park-s15e11-broadway-bro-down-gif-23115392",
"https://tenor.com/view/no-nope-non-rick-rick-and-morty-gif-20999440",
"https://tenor.com/view/denied-barney-legendary-stinson-st-legend-challenge-accepted-gif-17940726",
"https://tenor.com/view/request-denied-colonel-sharp-gi-joe-a-real-american-hero-the-synthoid-conspiracy-deny-gif-17529846",
"https://tenor.com/view/simon-cowell-thats-a-no-its-a-no-its-a-no-from-me-gif-7663264",
"https://tenor.com/view/not-gonna-happen-mackelmore-nope-nada-no-way-gif-15549117",
"https://tenor.com/view/invader-zim-gir-why-cry-tears-gif-12386135",
]

swearwords = [
	"fuck",
	"fucking",
	"fucken",
	"fuck!",
	"fucking!",
	"fucken!",
	"fck",
	"fck!",
	"fucker",
	"fucker!",
	"fuckers",
	"fuckers!",
	"fckuer",
	"fucka",
	"fucka!",
	"fuka!",
	"fuka",
	"shit",
	"shit!",
	"shitting",
	"shitting!",
	"cunt",
	"cunt!",
	"fag",
	"fag!",
	"faggot",
	"faggot!",
	"nigger",
	"nigger!",
	"nigga",
	"nigga!",
	"piel",
	"piel!",
	"p1el"
	"p1el!",
	"p1el",
	"p0es",
	"p0es!",
    "pussy",
	"poes",
	"poes!",
    "gay",
    "cock",
    "ass",
]


def check(word, blacklist):
    return SequenceMatcher(None, word, blacklist).ratio()




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

