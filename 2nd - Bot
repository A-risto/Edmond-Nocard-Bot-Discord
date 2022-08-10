from discord.ext import commands
import discord
from discord.utils import get
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print("Bot prêt...")
    await bot.change_presence(activity=discord.Game("en build"))

@bot.command()
@commands.has_permissions(administrator=True)
async def init_lycee(ctx):
    embed = discord.Embed(title="__Lycée :__", description="""
        **``Berthelot``** : :regional_indicator_b:
        
        **``Schuman``** : :regional_indicator_s:
        
        **``Delacroix``** : :regional_indicator_d:
        
        **``Autre lycée``** : :regional_indicator_a:
        """)
    await ctx.send(embed=embed)


@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    member = payload.member
    guild = member.guild
    role_berthelot = guild.get_role(992444671949283398)
    role_schuman = guild.get_role(992444770817409074)
    role_delacroix = guild.get_role(992445325837082745)
    role_autre = guild.get_role(992448039706955826)
    message = payload.message_id
    channel = payload.channel_id
    if emoji == "🇧" and message == 1006910956229640243 and channel == 888414703754297375:
        await member.add_roles(role_berthelot)
        embed = discord.Embed(title="From **2nd - Serveur**", description="""
               Le rôle ``Berthelot`` vous a été ajouté !
               """)
        embed.set_thumbnail(
            url="https://pep-ak-47.000webhostapp.com/pp.gif")
        await member.send(embed=embed)

    if emoji == "🇸" and message == 1006910956229640243 and channel == 888414703754297375:
        await member.add_roles(role_schuman)
        embed = discord.Embed(title="From **2nd -S erveur**", description="""
               Le rôle ``Schuman`` vous a été ajouté !
               """)
        embed.set_thumbnail(
            url="https://pep-ak-47.000webhostapp.com/pp.gif")
        await member.send(embed=embed)

    if emoji == "🇩" and message == 1006910956229640243 and channel == 888414703754297375:
        await member.add_roles(role_delacroix)
        embed = discord.Embed(title="From **2nd - Serveur**", description="""
               Le rôle ``Delacroix`` vous a été ajouté !
               """)
        embed.set_thumbnail(url="https://pep-ak-47.000webhostapp.com/pp.gif")
        await member.send(embed=embed)

    if emoji == "🇦" and message == 1006910956229640243 and channel == 888414703754297375:
        await member.add_roles(role_autre)
        embed = discord.Embed(title="From **2nd - Serveur**", description="""
               Le rôle ``Autre lycée`` vous a été ajouté !
               """)
        embed.set_thumbnail(
            url="https://pep-ak-47.000webhostapp.com/pp.gif")
        await member.send(embed=embed)

@bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 1006910956229640243:
        guild_id = payload.guild_id
        emoji = payload.emoji.name
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        role_berthelot = discord.utils.get(guild.roles, name='Berthelot')
        role_schuman = discord.utils.get(guild.roles, name='Schuman')
        role_delacroix = discord.utils.get(guild.roles, name='Delacroix')
        role_autre = discord.utils.get(guild.roles, name='Autre lycée')
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

        if emoji == "🇦":
            await member.remove_roles(role_autre)
            embed = discord.Embed(title="From **2nd - Serveur**", description="""
                   Le rôle ``Autre lycée`` vous a été retiré !
                   """)
            embed.set_thumbnail(
                url="https://pep-ak-47.000webhostapp.com/pp.gif")
            await member.send(embed=embed)

        if emoji == "🇧":
            await member.remove_roles(role_berthelot)
            embed = discord.Embed(title="From **2nd - Serveur**", description="""
                   Le rôle ``Berthelot`` vous a été retiré !
                   """)
            embed.set_thumbnail(
                url="https://pep-ak-47.000webhostapp.com/pp.gif")
            await member.send(embed=embed)

        if emoji == "🇩":
            await member.remove_roles(role_delacroix)
            embed = discord.Embed(title="From **2nd - Serveur**", description="""
                   Le rôle ``Delacroix`` vous a été retiré !
                   """)
            embed.set_thumbnail(
                url="https://pep-ak-47.000webhostapp.com/pp.gif")
            await member.send(embed=embed)

        if emoji == "🇸":
            await member.remove_roles(role_schuman)
            embed = discord.Embed(title="From **2nd - Serveur**", description="""
                   Le rôle ``Schuman`` vous a été retiré !
                   """)
            embed.set_thumbnail(
                url="https://pep-ak-47.000webhostapp.com/pp.gif")
            await member.send(embed=embed)
TOKEN = ""
bot.run(TOKEN)
