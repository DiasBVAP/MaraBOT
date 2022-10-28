import discord
import os
from dotenv import load_dotenv

class MyClient(discord.Client):
    MAIN_CHANNEL = 538755995611168772
    async def on_ready(self):
        print(f'Logged on as {self.user}!')   
        for member in self.get_all_members():
            if ((member.name == 'Maragamer') and (member.status == discord.Status.online)):
                channel = client.get_channel(self.MAIN_CHANNEL)
                await channel.send(f'Cheguei. Me mama {member.mention}')
                

    async def on_presence_update(self, before, after):
        if ((after.name == 'Maragamer') and (after.status == discord.Status.online)):
            channel = client.get_channel(self.MAIN_CHANNEL)
            await channel.send(f'Me mama {after.mention}')

intents = discord.Intents.all()
client = MyClient(intents=intents)

load_dotenv()
token = os.environ.get('TOKEN')
client.run(token)