import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print("The Bot is ready")


@bot.command()
async def ping(ctx):
    await ctx.send(f'Hello! I am there and my latency is {round(bot.latency*1000)}ms ')


@bot.command(name='Bulk delete Messages', help='Bulk delete messages by specifying number of messages to delete')
async def clear(ctx, ammount=4):
    await ctx.channel.purge(limit=ammount)


@bot.command(name='Math Calcualtor', help='Use math n1 operation n2, for using the math calculator.', aliases=['math', 'calc'])
async def math(ctx, ni, oper, ns):
    if oper == '+':
        await ctx.send(int(ni)+int(ns))
    if oper == '-':
        await ctx.send(int(ni)-int(ns))
    if oper == '*':
        await ctx.send(int(ni)*int(ns))
    if oper == '/':
        await ctx.send(int(ni)/int(ns))


@bot.command()
async def hyd(ctx):
    embed = discord.Embed(title="Hydrerabad To-Do", url="https://rebrand.ly/hydtodo",
                          description="The website link for Hydrerabad To-Do is **rebrand.ly/hydtodo**", color=discord.Color.blue())
    embed.set_author(name=ctx.author.name,
                     url="https://rebrand.ly/bunny-website", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@bot.command(name='discord.py Help', aliases=['pyhelp', 'helppy', 'py'], help='All the help websites for python discord.py')
async def py(ctx):
    embed = discord.Embed(
        tittle='discord.py Help websites', description='Help for discord.py with different websites', colour=discord.Color.blue())
    embed.set_author(name=ctx.author.name,
                     url="https://rebrand.ly/bunny-website", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url='https://bit.ly/3styBZX')
    embed.add_field(
        name='Bot Embed', value='https://medium.com/python-in-plain-english/send-an-embed-with-a-discord-bot-in-python-61d34c711046', inline=False)
    embed.add_field(name='Repl.it Cloud',
                    value='https://repl.it/@BunnyPranav/Bunnys-Bot#main.py', inline=False)
    embed.add_field(name="Techraj Discord",
                    value="https://discord.com/channels/654884606750752778/654884606750752781", inline=False)
    await ctx.send(embed=embed)


@bot.command(aliases=['len', 'length'], name='Length of word char', help='Use this command to get the length of char in a word')
async def _len(ctx, text='example'):
    await ctx.send(f'The length of {text} is {len(text)}')


@bot.command(name='Roll Dice', aliases=['diceroll', 'dice'], help='Roll your own dice and get the number you get on your dice')
async def dice(ctx):
    dice_no = random.randint(1, 6)
    await ctx.send(f'You have got {dice_no} in the dice!!!')


@bot.command(name='Random Numbers', aliases=['random', 'rand'], help='Use rand n1 n2 and number of random numbers')
async def rand(ctx, ni, ns, number):
    i = 0
    rand_numbers = []
    int_num = int(number)
    while i < int_num:
        rand_numbers.append(random.randint(int(ni), int(ns)))
        i += 1
    await ctx.send(f"The 10 random numbers are {', '.join([str(i)for i in rand_numbers])}")

bot.run('')
