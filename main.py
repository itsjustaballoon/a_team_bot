import discord
import os
import twitter

# Discord Client
client = discord.Client()
my_secret = os.environ['my_secret']

# Twitter Client

twitter_key = os.environ['twitter_key']
twitter_secret = os.environ['twitter_secret']

api = twitter.Api(
  # consumer_key=[consumer key],
  # consumer_secret=[consumer secret],
  access_token_key=[twitter_key],
  access_token_secret=[twitter_secret])

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(my_secret)