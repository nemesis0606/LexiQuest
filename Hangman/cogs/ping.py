import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping.py is ready")

    @commands.command()
    async def ping(self,ctx):
        ping_embed=discord.Embed(title="Ping", description="Latency in ms", color=discord.Color.blue())
        ping_embed.add_field(name=f"{self.client.user.name}'s latency:", value=f"{(round(self.client.latency*1000))} ms", inline=True)
        ping_embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        await ctx.send(embed=ping_embed)

async def setup(client):
    await client.add_cog(Ping(client))