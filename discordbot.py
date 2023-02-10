from discord import channel, colour, message
import discord
from discord.embeds import Embed
from discord.ext import commands
from random import *
from time import *
import calendar as ii
import openpyxl
import pandas as pd

token = 'MTA3MjE3OTkwMzEzNjU1MTA0NQ.GTRgIw.Kxok30TUWAoxpHhirsJp2GrRV_azzGtT50WNl8'

b = randint(1, 10)
n = choice(str(b))

client = commands.Bot(intents=discord.Intents.all(), command_prefix="!", description='Hả ai bik j đâu :))')

# time function
hour = strftime("%H")
minutes = strftime("%M")
seconds = strftime("%S")
moment = strftime("%p")
if str(moment) == "PM":
    moment = "tối"
else:
    moment = "sáng"
    
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'User List'
sheet['A1'] = 'Member Name'

@client.event
async def on_ready():
    server = client.guilds[0]
    members = server.members
    member_list = []
    for member in members:
        if not member.bot:
            member_list.append([member.name, member.id, member.display_name])
    df = pd.DataFrame(member_list, columns=['Name', 'ID', 'Display Name'])
    df.to_excel("members.xlsx", index=False)
    print('Bot is ready')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Trùm khủng bố Trung Đông"))    

@client.event
async def cog_check(self, ctx):
    if ctx.message.author.id == ctx.guild.owner.id and ctx.message.content.startswith('/hi'):
        await ctx.channel.send('hi')

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel
    i = 1
    print('{}: {}'.format(author, content))
    if message.content.startswith('/attendance'):
        sheet.append([author.name])
        wb.save('UserList.xlsx')
        await channel.send('{} đã được thêm vào danh sách điểm danh'.format(author.name))
    if message.content.startswith('.ctf'):
        await channel.send('https://ctf.fptufia.me/')
    if message.content.startswith('muốn làm chủ nghiệm ko'):
        await channel.send('Muốn')
    if message.content.startswith('.time'):
        await channel.send('bây giờ là: {} giờ {} phút {} giây {}'.format(hour, minutes, seconds, moment))
    for i in range(1, 13):
        if message.content.startswith('.Lịch của năm 2022'):
            await channel.send(':))))')
            await channel.send(ii.month(2022, i))
    if message.content.startswith('.info' + str(author)):
        pass


@client.event
async def on_message_add(reaction, user):
    channel = reaction.message.channel
    await channel.send(
        '{} đã thêm biểu tượng {} ở tin nhắn {}'.format(user.name, reaction.emoji, reaction.message.content))


@client.event
async def on_message_remove(reaction, user):
    channel = reaction.message.channel
    await channel.send(
        '{} đã xóa biểu tượng {} ở tin nhắn {}'.format(user.name, reaction.emoji, reaction.message.content))


@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await channel.send('{}: đã xóa tin nhắn: {}'.format(author, content))

    

client.run(token)