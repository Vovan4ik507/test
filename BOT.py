import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import time

prefix = 'r!'

Bot = commands.Bot(command_prefix = prefix)

@Bot.command()
async def join(ctx):
	voice = ctx.author.voice
	if voice == None:
		await ctx.send('You need to be in a voice chat to use that')
	else:
		client = await voice.channel.connect(timeout = 5)
		await ctx.send(client.endpoint)

@Bot.command()
async def leave(ctx):
	voice = ctx.author.voice
	if voice == None:
		await ctx.send('You need to be in a voice chat to use that')
	else:
		client = await voice.channel.connect(timeout = 5)
		await client.disconnect()

@Bot.command()
async def say(ctx, channel = None, *, word = None):
	stop = False
	guild = ctx.guild
	channel_list = guild.text_channels
	for i in range(0, len(channel_list)):
		if channel == channel_list[i].name or channel == channel_list[i].id or channel == channel_list[i].mention:
			if word == None:
				stop = True
				await ctx.send('You don\'t wrote what to say')
			else:
				stop = True
				channel = channel_list[i]
				await channel.send(word)
	else:
			if channel == None:
				await ctx.send('You don\'t wrote what to say')
			else:
				if stop == False:
					if word == None:
						await ctx.send(channel)
					else:
						await ctx.send(channel + f' {word}')

@Bot.command()
async def user(ctx, member: discord.Member):
	emb = discord.Embed(title = str(member), description = member.mention, color = member.top_role.color)
	emb.add_field(name = "ID", value = member.id, inline = False)
	emb.add_field(name = "Joined server at", value = str(member.joined_at)[:19], inline = False)
	emb.add_field(name = "Created account at", value = str(member.created_at)[:19], inline = False)
	if member.top_role == member.roles[0]:
		emb.add_field(name = "Highest role", value = member.top_role, inline = False)
	else:
		emb.add_field(name = "Highest role", value = member.top_role.mention, inline = False)
	emb.set_thumbnail(url = member.avatar_url)
	emb.set_footer(text = f"Caused by: {str(ctx.author)}", icon_url = ctx.author.avatar_url)
	await ctx.send(embed = emb)
	
@Bot.event
async def on_ready():
	print('Bot is ready!')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Я слежу за вами, рабы Купола. Без моего разрешения вы не можете ничего!!!'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
