from discord.ext import commands
import discord
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print("Ready !")
    await bot.change_presence(activity=discord.Game("encore en dev j'ai pas trop le temps là"))


@bot.command()
async def info(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfPerson = server.member_count
    serverName = server.name
    message = f"Le serveur **{serverName}** contient **{numberOfPerson}** personnes ! \nLa description du serveur est {serverDescription}. \nCe serveur possède {numberOfTextChannels} salons écrit et {numberOfVoiceChannels} salon vocaux."
    await ctx.send(message)


@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.User, *, reason = "Aucune raison n'a été donné"):
    #await ctx.guild.ban(user, reason = reason)
    embed = discord.Embed(title = "**Banissement**", description = "Un modérateur a frappé !", color=0xfa8072)
    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    embed.set_thumbnail(url = "https://discordemoji.com/assets/emoji/BanneHammer.png")
    embed.add_field(name = "Membre banni", value = user.name, inline = True)
    embed.add_field(name = "Raison", value = reason, inline = True)
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason=reason)
    await ctx.send(embed = embed)


@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason=reason)
            await ctx.send(f"{user} à été unban.")
            return
    # Ici on sait que lutilisateur na pas ete trouvé
    await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")


@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user: discord.User, reason ="aucune raison n'a été donné"):
    embed = discord.Embed(title="**Expulsion**", description="La justice a frappé !", color=0xfa8072)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://www.agn-avocats.fr/wp-content/uploads/2021/02/Expulser-son-locataire-ou-un-squatter.jpg")
    embed.add_field(name="Membre expulsé ! ", value=user.name, inline=True)
    embed.add_field(name="Raison", value=reason, inline=True)
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason=reason)
    await ctx.send(embed=embed)


@bot.command()
async def clear(ctx, nombre: int):
    messages = await ctx.channel.history(limit=nombre + 1).flatten()
    for message in messages:
        await message.delete()
    await ctx.send(f"{nombre} message ont été supprimé ! ")

@bot.command()
async def regles(ctx):
    await ctx.send(""""
    1. Aucune discrimination, forme de racisme, sexisme etc ne sera accepté
    2. Le droit à la vie privé doit être respecté
    3. J'ai pas finit de faire les règles mais tkt ça arrive tu sais cb de temps ça me prend de faire ce bot hein ? ba bcp je fais tout à la main ok donc si t'es pas content fait le à ma place
    """)


@bot.command()
@commands.has_permissions(administrator=True)
async def classe(ctx):
    embed = discord.Embed(title="__Classe :__", description="""

    **3eA** : :regional_indicator_a:

    **3eB** : :regional_indicator_b: 

    **3eC** : :regional_indicator_c:

    **3eD** : :regional_indicator_d:

    **Hors collège** : :negative_squared_cross_mark:   
    """)
    await ctx.send(embed=embed)

@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    print(emoji)
    member = payload.member
    guild = member.guild
    role_3eA = guild.get_role(888166725177188413)
    role_3eB = guild.get_role(888166892504760360)
    role_3eC = guild.get_role(888167077960106015)
    role_3eD = guild.get_role(888167145857499146)
    hors_college = guild.get_role(924297493624274944)
    role_espagnol = guild.get_role(918575305923379211)
    role_italien = guild.get_role(918575465436950578)
    role_latin = guild.get_role(929756586543566919)
    role_grec = guild.get_role(929756308092096522)
    if emoji =="🇦":
        await member.add_roles(role_3eA)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
               Le rôle 3eA vous a été ajouté !
               """)
        await member.send(embed=embed)
    if emoji == "🇨":
        await member.add_roles(role_3eC)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
               Le rôle 3eC vous a été ajouté !
               """)
        await member.send(embed=embed)
    if emoji == "🇩":
        await member.add_roles(role_3eD)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
               Le rôle 3eD vous a été ajouté !
               """)
        await member.send(embed=embed)
    if emoji == "🇧":
        await member.add_roles(role_3eB)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
               Le rôle 3eB vous a été ajouté !
               """)
        await member.send(embed=embed)
    if emoji =="❎":
        await member.add_roles(hors_college)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
               Le rôle 'Hors-collège' vous a été ajouté !
               """)
        await member.send(embed=embed)
    if emoji == "🇪🇸":
        await member.add_roles(role_espagnol)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
                       Le rôle 'Espagnol' vous a été ajouté !
                       """)
        await member.send(embed=embed)
    if emoji == "🇮🇹":
        await member.add_roles(role_italien)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
                               Le rôle 'italien' vous a été ajouté !
                               """)
        await member.send(embed=embed)
    if emoji == "🔤":
        await member.add_roles(role_latin)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
                                       Le rôle 'latin' vous a été ajouté !
                                       """)
        await member.send(embed=embed)
    if emoji == "🇬🇷":
        await member.add_roles(role_grec)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
                                               Le rôle 'grec' vous a été ajouté !
                                               """)
        await member.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def LV2(ctx):
    embed = discord.Embed(title="__LV2/Option :__", description="""

    **Espagnol** : 🇪🇸

    **Italien** : 🇮🇹

    **Latin** : 🔤

    **Grec** : 🇬🇷

    """)
    await ctx.send(embed=embed)
@bot.event
async def on_raw_reaction_remove(payload):
    emoji = payload.emoji.name
    if emoji == "🍔":
        print("Grade enlevé ")

token = "OTQ1NzMxMTg5NDI2MjQxNTQ2.YhUazg.986DfqBPyppnKXdzUbyjVCUGFcA"
bot.run(token)
