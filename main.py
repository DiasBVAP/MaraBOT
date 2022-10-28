import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')   

    async def on_presence_update(self, before, after):
        if (after.name == 'Maragamer' and after.status == discord.Status.online):
            channel = client.get_channel(538755995611168772)
            await channel.send(f'Me mama {after.mention}')

intents = discord.Intents.all()
client = MyClient(intents=intents)
client.run()