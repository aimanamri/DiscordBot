import discord
from dotenv import load_dotenv
import os
import requests
import json
import random

from requests.api import options

sad_words = ['sad','depressed',"unhappy","angry","miserable","depressing"]
starter_encouragements = [
    "Cheer up, mate !",
    "Hang in there.",
    "You are a great person."
]


load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')
client = discord.Client()

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)   # change json to python format
    quote = json_data[0]['q'] + '\n  - ' + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content
    # send hello message
    if msg.startswith('$hello'):
        await message.channel.send('Hello ! ')
     # send random quotes
    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    options = starter_encouragements

    # send encouragements
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

client.run(BOT_TOKEN)
