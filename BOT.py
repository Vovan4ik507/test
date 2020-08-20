import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import time

prefix = 'r!'

Bot = commands.Bot(command_prefix = prefix)

@Bot.command()
async def hello(ctx):
    	await ctx.send(f"Hello {ctx.author.mention}")
	
@Bot.command()
async def prefix(ctx, value):
	prefix = value

@Bot.command()
async def user(ctx, member: dicord.Member):
	emb = discrod.Embed(title = str(member), description = str(member))
	emb.colour = member.top_role.colour
	emb.add_field(name = 'Username', value = member.name)
	emb.set_thumbnail(member.avatar_url)
	emb.set_footer(text = f'Caused by {ctx.autor}', icon_url = ctx.autor.avatar_url)
	await ctx.send(embed = emb)
	
	
@Bot.event
async def on_ready():
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Playing with developer'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
