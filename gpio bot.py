import discord
from gpiozero import LED

client = discord.Client()

TOKEN = 'Your token here. If you will reveal your token to anyone, then regenerate it, because your bot will be immmediatly hacked.'

PREFIX = 'rpi!'

led = LED(17)

@client.event
async def on_ready():
    print('Sucessful login as {0.user}'.format(client))


@client.event
async def on_message(message):
    msg = message.content
    msg = msg.lower()
    if msg.startswith(PREFIX + 'led-on'):
        led.on()

    elif msg.startswith(PREFIX + 'led-off'):
        led.off()


client.run(TOKEN)
