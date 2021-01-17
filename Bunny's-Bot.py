import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("The Bot is ready")


@bot.command()
async def ping(ctx):
    await ctx.say(f'Hello! I am there and my latency is {round(bot.latency*1000)}ms ')


@bot.command()
async def clear(ctx, ammount=4):
    await ctx.channel.purge(limit=ammount)


@bot.command()
async def math(ctx, oper, ni, ns):
    if oper == '+':
        await ctx.send(int(ni)+int(ns))
    if oper == '-':
        await ctx.send(int(ni)-int(ns))
    if oper == '*':
        await ctx.send(int(ni)*int(ns))
    if oper == '/':
        await ctx.send(int(ni)/int(ns))


@bot.command
async def hyd(ctx):
    await ctx.send('The website link for Hydrerabad is **rebrand.ly/hydtodo**')


bot.run('Nzk4MTk4MzYxMDY0NjAzNzEx.X_xiJw.JRqsIZ3lV1SvuhGEuKaMrOJEo4Q')
