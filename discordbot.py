from discord import channel, colour, message
import discord
from discord.embeds import Embed
from discord.ext import commands 
from random import *
from time import*
import calendar as ii

token = 'MTA1OTg2NTg5Mzk4MDYwMjQ0OA.GjNRnC.Gqpd9GajktaE8Kglvv3tsOPDg1gG7f6ogLN6JQ'
 

b = randint(1,10) 
n = choice(str(b))
client = commands.Bot(intents=discord.Intents.all() , command_prefix= "." , description='Hả ai bik j đâu :))')

#time function
hour = strftime("%H")
minutes = strftime("%M")
seconds = strftime("%S")
moment = strftime("%p")
if str(moment) == "PM":
    moment = "tối" 
else:
    moment = "sáng"


@client.event
async def on_ready():
    tactivity = discord.Game(name="Ngân Lê")
    await client.change_presence(status=discord.Status.online, activity=tactivity)
    print('ready')

#@client.command()
#async def hello(ctx):
    #await ctx.send(f'hello {round(client.latency * 1000)}ms' )    


@client.event
async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel
    i = 1
    print('{}: {}'.format(author,content))
    

   
    if message.content.startswith('khen Ngân Lê') or message.content.startswith('Khen Ngân Lê'): 
        await channel.send('Ngân Lê xinh vllllllllllll:shit:\n'*2) 
    if message.content.startswith('chửi Ngân Lê') or message.content.startswith('Chửi Ngân Lê'):
        await channel.send("Má con Ngân Lê cận thận tau á")    
    if message.content.startswith('Chào Ngân Lê đi NPD5.0'):
        await channel.send('Chàoooooooooooooooo') 
    if message.content.startswith('.help'):
        await channel.send('help :smile:')
    if message.content.startswith('Thỉu năng'):
        await channel.send('Thỉu năng ',)
    if message.content.startswith('Thiểu năng'):
        await channel.send('nothing',)     
    if message.content.startswith('.time'):
        await channel.send('bây giờ là: {} giờ {} phút {} giây {}'.format(hour,minutes,seconds, moment))
    for i in range(1,13):  
        if message.content.startswith('.Lịch của năm 2022'):
            await channel.send(':))))') 
            await channel.send(ii.month(2022, i ))    
    if message.content.startswith('.info' + str(author)):
        pass
    
    if message.content.startswith('$'):
        msg = message.content.split()
        output = ''
        for word in msg[1:]:
            output += word
            output += ' '
        await channel.send(output)    

@client.event
async def on_message_add(reaction, user):
    channel = reaction.message.channel
    await channel.send('{} đã thêm biểu tượng {} ở tin nhắn {}'.format(user.name,reaction.emoji,reaction.message.content))

@client.event
async def on_message_remove(reaction, user):
    channel = reaction.message.channel
    await channel.send('{} đã xóa biểu tượng {} ở tin nhắn {}'.format(user.name,reaction.emoji,reaction.message.content))

@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await channel.send('{}: đã xóa tin nhắn: {}'.format(author,content))


client.run(token)    
