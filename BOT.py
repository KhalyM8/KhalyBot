import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        await message.channel.send("content")

client = MyClient()
client.run('OTgyNTU1NzIyMzQyNjA4OTc3.GdblAe.yfMu4K6Bv6vxBSho6rO0bKwjKLl4ArpQSOIbi8')