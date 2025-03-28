import discord
from bot_mantik_1 import gen_pass
from bot_mantik_2 import yazi_tura
from bot_mantik3 import emoji_olusturucu
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith("/yazı mı tura mı"):
        await message.channel.send(yazi_tura())
    elif message.content.startswith("/şifre oluştur"):
        await message.channel.send( gen_pass(10))
    elif message.content.startswith("/emoji oluştur"):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith("/yardım"):
        await message.channel.send("Yazı tura oynamak için /yazı mı tura mı yazın. Şifre oluşturmak için /şifre oluştur yazın. Emoji oluşturmak için /emoji oluştur yazın. Bota selam vermek için /merhaba yazın.")





client.run("token")
