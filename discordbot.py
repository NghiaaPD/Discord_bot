from discord import channel, colour, message
import discord
from discord.embeds import Embed
from discord.ext import commands
from random import *
from time import *
import calendar as ii
import openpyxl
import pandas as pd
import asyncio
from discord.ext.commands import Bot

token = ''

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
    await client.change_presence(activity=discord.Game(name="Trùm khủng bố Trung Đông"))
    print(f'{client.user.name} has connected to Discord!')
    # Lấy danh sách các thành viên trong kênh
    server = client.guilds[0]
    members = server.members
    member_list = []
    for member in members:
        if not member.bot:
            member_list.append([member.name, member.id, member.display_name])
    df = pd.DataFrame(member_list, columns=['Name', 'ID', 'Display Name'])
    df.to_excel("members.xlsx", index=False)
    #############################################
    print('Bot is ready')


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
    # Điểm danh trong kênh discord
    if message.content.startswith('/attendance'):
        sheet.append([author.name])
        wb.save('UserList.xlsx')
        await channel.send('{} đã được thêm vào danh sách điểm danh'.format(author.name))


    if message.content.startswith('/ctf'):
        await channel.send('https://ctf.fptufia.me/')

    if message.content.startswith('muốn làm chủ nghiệm ko'):
        await channel.send('Muốn')

    if message.content.startswith('/time'):
        await channel.send('bây giờ là: {} giờ {} phút {} giây {}'.format(hour, minutes, seconds, moment))

    #Xác thực bằng token
    if message.content.startswith('/verify'):
        token = message.content.split()[1]
        if token == "FIA_CTF_trainning":
            role = discord.utils.get(message.guild.roles, name="Khủng bố")#set token ở names
            member = message.author
            await member.add_roles(role)
            await message.channel.send(
                "{} You have been verified and received the Verified {}".format(author.name, role))
        else:
            await message.channel.send("{} Sai token".format(author.name))

    await client.process_commands(message)

    #tính năng kích dành cho vai trò admin (có thể chưa hoàn thành)
    if message.content.startswith('!kick'):
        if 'admin' in [role.name for role in message.author.roles]:
            member = message.mentions[0]
            reason = " ".join(message.content.split()[2:])
            await member.kick(reason=reason)
            await message.channel.send(f"{member.mention} has been kicked.")
        else:
            await message.channel.send("You do not have the permission to use this command.")
    await client.process_commands(message)


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