import discord
from discord.ext import commands
#import keep_alive
import time
#keep_alive.keep_alive()
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="§", intents=intents, help_command=None)


@bot.event
async def on_ready():
    print("Bot prêt...")
@bot.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == 888163341174992966:
        channel = after.channel
        try:
            if before.channel.members == [] and not before.channel.id == 947804187926863902 and not before.channel.id == 947832541660983306:
                if before.channel.category_id == 888163341174992968:
                    await before.channel.delete()
        except:
            pass

        if channel.id == 947804187926863902:
            guild = after.channel.guild
            private_channels = discord.utils.get(guild.categories, id=888163341174992968)
            voice_channel = await guild.create_voice_channel("Salon de "+member.name, overwrites=None, category=private_channels)
            time.sleep(1)
            await member.move_to(voice_channel)
            await voice_channel.set_permissions(member, connect=True, speak=True, move_members=True, manage_channels=True, view_channel=True)

token = 'TOKEN'
bot.run(token)
