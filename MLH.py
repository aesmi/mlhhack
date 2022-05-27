
import discord
import random as r
from discord.ext import commands

# make a function that pulls the token, because this github is public
def read_token() -> str:
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

# set the function equal to a variable, put this anywhere you need the token
TOKEN = read_token()


# initialize the client
client = commands.Bot(command_prefix = "!")


# outputs a message in local terminal confirming connection
@client.event
async def on_ready():
    #print('we have logged in as {0.user}'.format(client))
    print('yeet')

bot_output = "botspam"

#99 command
@client.command(name = "99")
async def quotes99(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'I\'m the human form of the 💯 emoji.'
    ]
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)
    return

#sus command
@client.command(name = "sus")
async def sus(ctx):
    await ctx.send("ඞ")
    return

#hello command
@client.command(name = "hello")
async def hello(ctx):
    await ctx.send(f'Hello, ' + ctx.message.author.display_name + '!')
    return

#bye command
@client.command(name = "bye")
async def bye(ctx):
    await ctx.send(f'See you later, ' + ctx.message.author.display_name + '!')
    return


#Random command
@client.command(name = "random")
async def random(ctx):
    randNum = r.randrange(0, 1000)
    res = 'This is your random number: ' + str(randNum)
    await ctx.send(res)
    return

#Anywhere command
@client.command(name = "anywhere")
async def random(ctx):
    await ctx.send('this can be used anywhere')
    return


'''
@client.event
async def on_message(message):
    # simplifies input
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    # this prints all user bot and user input in local output terminal
    # helps with debugging
    print(f'{username}:{user_message}({channel})')

    # important to always include this
    # it prevents the bot from responding to itself
    # (which would make an infinite loop)
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'I\'m the human form of the 💯 emoji.'
    ]

    if message.content == '!99':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
        return

    if message.content == "!sus":
        await message.channel.send("ඞ")
        return

    # general responses
    # this ensures the bot works only in desired channel
    if message.channel.name == bot_output:
        if user_message.lower() == '!hello':
            await message.channel.send(f'Hello, {username}!')
            return

        elif user_message.lower() == '!bye':
            await message.channel.send(f'See you later, {username}!')
            return

        elif user_message.lower() == '!random':
            response = f'This is your random number: {random.randrange(1000)}'
            await message.channel.send(response)
            return

    if user_message.lower() == '!anywhere':
        await message.channel.send('this can be used anywhere')
        return

'''


# run our bot by providing the token
client.run(TOKEN)
