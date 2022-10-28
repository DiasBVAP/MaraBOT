import discord
import os
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        load_dotenv()
        print(f'Logged on as {self.user}!')   
        for member in self.get_all_members():
            if ((member.name == os.environ.get('USER_NAME')) and (member.status == discord.Status.online)):
                channel = client.get_channel(int(os.environ.get('CHANNEL_ID')))
                await channel.send(member.mention)
                

    async def on_presence_update(self, before, after):
        load_dotenv()
        if ((after.name == os.environ.get('USER_NAME')) and (after.status == discord.Status.online)):
            channel = client.get_channel(int(os.environ.get('CHANNEL_ID')))
            await channel.send(after.mention)

load_dotenv()
token = os.environ.get('TOKEN')

intents = discord.Intents.all()
client = MyClient(intents=intents)

client.run(token)