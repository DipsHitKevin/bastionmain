
import discord
import asyncio
import logging
logging.basicConfig()

bot = discord.Client()
killmyself = "http://66.media.tumblr.com/68ec4239d93af1da5880375be6d145ee/tumblr_mjnrtvogEK1rgjglno1_500.gif"


def logout():
    bot.logout()


async def bastion(author, message):
    await bot.send_message(message.channel, "FUCK YOU %s, POTG IS MINE" % author, tts=True)


@bot.event
async def on_message(message):
    author = message.author
    if message.content.startswith("!bastion"):
        bastion(author, message)
    if message.content.startswith("test"):
        await bot.send_message(message.channel, "THIS IS A TEST BEEP BOOP", tts=True)
    if "kill myself" in message.content:
        await bot.send_message(message.channel, killmyself)
    if "bastion" in message.content:
        await bot.send_message(message.channel, "PLAY OF THE GAME FAGGOT", tts=True)


@bot.event
async def on_voice_state_update(before, after):
    bot.send_message(before.channel, "HAHAHA {} IS A FAGGOT")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('---------')


@bot.event
async def typing():
    print('typing detected')

token = "MjA1MjIzMzg0MDE4MDU5Mjc1.CnDK6g.Y8Zl9cKLnOkIYSYTUw7K6clMUd8"
bot.run(token)

