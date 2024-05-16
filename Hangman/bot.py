import discord
from discord.ext import commands
import os
import asyncio

client=commands.Bot(command_prefix="$", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is osnline!")

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename[:-3]} is loaded")

async def main():
    async with client:
        await load()
        with open("./token.txt") as file:
            token=file.read()
        await client.start(token)

asyncio.run(main())

# @bot.command(aliases=["hi"])
# async def hello(ctx):
#     await ctx.send(f"Hi there! {ctx.author.mention}")

# @bot.command()
# async def ping(ctx):
#     ping_embed=discord.Embed(title="Ping", description="Latency in ms", color=discord.Color.blue())
#     ping_embed.add_field(name=f"{bot.user.name}'s latency:", value=f"{(round(bot.latency*1000))} ms", inline=True)
#     ping_embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
#     await ctx.send(embed=ping_embed)


# bot.run(token)