from discord.ext import commands
import discord
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import os

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents, help_command=None)


@bot.event
async def on_ready():
    print("Bot prêt...")
    await bot.change_presence(activity=discord.Game("?help"))


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
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.User, *, reason="Aucune raison n'a été donné"):
    await ctx.guild.ban(user, reason=reason)
    embed = discord.Embed(title="**Banissement**", description="Un modérateur a frappé !", color=0xfa8072)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://discordemoji.com/assets/emoji/BanneHammer.png")
    embed.add_field(name="Membre banni", value=user.name, inline=True)
    embed.add_field(name="Raison", value=reason, inline=True)
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason=reason)
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason=reason)
            await ctx.send(f"{user} à été unban.")
            return
    await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User, reason="aucune raison n'a été donné"):
    embed = discord.Embed(title="**Expulsion**", description="La justice a frappé !", color=0xfa8072)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url="https://www.agn-avocats.fr/wp-content/uploads/2021/02/Expulser-son-locataire-ou-un-squatter.jpg")
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
    message = payload.message_id
    channel = payload.channel_id
    if emoji == "🇦" and message == 945968620935192607 and channel == 888414703754297375:
        await member.add_roles(role_3eA)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
               Le rôle 3eA vous a été ajouté !
               """)
        embed.set_thumbnail(
            url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
        await member.send(embed=embed)

    if emoji == "🇨" and message == 945968620935192607 and channel == 888414703754297375:
        await member.add_roles(role_3eC)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
               Le rôle 3eC vous a été ajouté !
               """)
        embed.set_thumbnail(
            url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
        await member.send(embed=embed)
    if emoji == "🇩" and message == 945968620935192607 and channel == 888414703754297375:
        await member.add_roles(role_3eD)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
               Le rôle 3eD vous a été ajouté !
               """)
        await member.send(embed=embed)

    if emoji == "🇧" and message == 945968620935192607 and channel == 888414703754297375:
        await member.add_roles(role_3eB)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
               Le rôle 3eB vous a été ajouté !
               """)
        embed.set_thumbnail(
            url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
        await member.send(embed=embed)

    if emoji == "❎" and message == 945968620935192607 and channel == 888414703754297375:
        await member.add_roles(hors_college)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
               Le rôle 'Hors-collège' vous a été ajouté !
               """)
        embed.set_thumbnail(
            url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
        await member.send(embed=embed)

    if emoji == "🇪🇸" and channel == 888414703754297375:
        await member.add_roles(role_espagnol)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
                       Le rôle 'Espagnol' vous a été ajouté !
                       """)
        embed.set_thumbnail(
            url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
        await member.send(embed=embed)

    if emoji == "🇮🇹" and channel == 888414703754297375:
        await member.add_roles(role_italien)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
                               Le rôle 'italien' vous a été ajouté !
                               """)
        embed.set_thumbnail(
            url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
        await member.send(embed=embed)

    if emoji == "🔤" and channel == 888414703754297375:
        await member.add_roles(role_latin)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
                                       Le rôle 'latin' vous a été ajouté !
                                       """)
        embed.set_thumbnail(
            url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
        await member.send(embed=embed)

    if emoji == "🇬🇷" and channel == 888414703754297375:
        await member.add_roles(role_grec)
        embed = discord.Embed(title="From **3e-Serveur**", description="""
                                               Le rôle 'grec' vous a été ajouté !
                                               """)
        embed.set_thumbnail(
            url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
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


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="__Commandes du bot : __", description="""
    ?info = donne des informations sur le serveur.

    ?clear <nombre de message> = efface le nombre de message donn.

    ?regles = montre les règles du serveur.

    """, url="https://github.com/A-risto/Edmond-Nocard-Bot-Discord/blob/main/main.py")
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://lachroniquefacile.fr/wp-content/uploads/2018/07/%EF%BC%9F.png")
    embed.add_field(name="__Admins commandes :__ ", value="""

    ?ban <@utilisateur> = Ban l'utilisateur (vous pouvez spécifier une raison)

    ?unban <@utilisateur> = Debann l'utilisateur

    ?kick <@utilisateur> = Expulse l'utilisateur (vous pouvez spécifier une raison)

    ?mute <@utilisateur> = Mute l'utilisateur (vous pouvez spécifier une raison)

    ?tempmute <@utilisateur> = Mute l'utilisateur pour une certaine durée (à spécifier)
    """, inline=False)
    embed.add_field(name="'__Fun'commandes :__", value="""
    ?wanted <montant de la prime> <@de l'utilisateur> <message qui accompagne la prime>
    """)
    embed.set_footer(text="Les prochaines commandes arrivent bientôt tkt")
    await ctx.send(embed=embed)


@bot.command()
async def wanted(ctx, prix, user: discord.Member = None, *message):
    if message == None:
        txt = " "
    else:
        txt = " ".join(message)
    img = Image.open('Screenshot 2022-02-24 15.19.32 (1).jpg')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("BERNHC.TTF", 40)
    font_prime = ImageFont.truetype("BERNHC.TTF", 60)
    asset = user.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((350, 350))
    draw.text((50, 730), txt, (0, 0, 0), font=font)
    draw.text((60, 660), ("$" + str(prix)), (0, 0, 0), font=font_prime)
    img.paste(pfp, (120, 235))
    img.save("txt.png")
    await ctx.send(file=discord.File('txt.png'))
    os.remove('txt.png')


async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role


@bot.command()
async def mute(ctx, member: discord.Member, *, reason="Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason=reason)
    embed = discord.Embed(title="", description=f"le membre {member.mention} a été mute\n\nRaison : {reason}")
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def unmute(ctx, member: discord.Member):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole)
    embed = discord.Embed(title="", description=f"Le membre {member.mention} a été unmute")
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.send("Pong !")

@bot.event
async def on_member_join(member):
    salon = 945965595554381835
    embed = discord.Embed(title="__Nouveau membre :__", description=f"Bienvenue {member.mention} sur le serveur ! Tu peux prendre tes rôles dans le salon #Classe-LV2 !")
    embed.set_thumbnail(url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
    channel = member.guild.get_channel(945963368441843727)
    await channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    channel = member.guild.get_channel(945963368441843727)
    embed = discord.Embed(title="__Départ d'un membre :__", description=f" {member.mention} a quitté le serveur ! Il ne manquera a personne...")
    embed.set_thumbnail(url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
    await channel.send(embed=embed)


@bot.command()
async def repete(ctx, *texte):
    await ctx.send(" ".join(texte))
""""""
@bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 945968620935192607 or message_id == 945982510481940500:
        guild_id = payload.guild_id
        emoji = payload.emoji.name
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        role_3eA = discord.utils.get(guild.roles, name='3e A')
        role_3eB = discord.utils.get(guild.roles, name='3e B')
        role_3eC = discord.utils.get(guild.roles, name='3e C')
        role_3eD = discord.utils.get(guild.roles, name='3e D')
        role_hors_college = discord.utils.get(guild.roles, name='Hors-collège')
        role_espagnol = discord.utils.get(guild.roles, name='🇪🇸 Espagnol 🇪🇸')
        role_italien = discord.utils.get(guild.roles, name='🇮🇹 Italien 🇮🇹')
        role_latin = discord.utils.get(guild.roles, name='🔤 Latin 🔤')
        role_grec = discord.utils.get(guild.roles, name='🏛 Grec 🏛')
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

        if emoji == "🇦":
            await member.remove_roles(role_3eA)
            embed = discord.Embed(title="From **3e-Serveur**", description="""
                   Le rôle 3eA vous a été retiré !
                   """)
            embed.set_thumbnail(
                url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
            await member.send(embed=embed)

        if emoji == "🇧":
            await member.remove_roles(role_3eB)
            embed = discord.Embed(title="From **3e-Serveur**", description="""
                       Le rôle 3eB vous a été retiré !
                       """)
            embed.set_thumbnail(
                url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
            await member.send(embed=embed)

        if emoji == "🇩":
            await member.remove_roles(role_3eD)
            embed = discord.Embed(title="From **3e-Serveur**", description="""
                       Le rôle 3eD vous a été ajouté !
                       """)
            embed.set_thumbnail(
                url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
            await member.send(embed=embed)

        if emoji == "🇨":
            await member.remove_roles(role_3eC)
            embed = discord.Embed(title="From **3e-Serveur**", description="""
                                                   Le rôle '3eC' vous a été retiré !
                                                   """)
            embed.set_thumbnail(
                url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
            await member.send(embed=embed)

        if emoji == "❎":
            await member.remove_roles(role_hors_college)
            embed = discord.Embed(title="From **3e-Serveur**", description="""
            Le role 'Hors-Collège' vous a été retiré !""")
            embed.set_thumbnail(url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
            await member.send(embed=embed)

        if emoji == "🇪🇸":
            await member.remove_roles(role_espagnol)
            embed = discord.Embed(title="From **3e-Serveur**", description="""
            Le role 'Espagnol' vous a été retiré !""")
            embed.set_thumbnail(url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
            await member.send(embed=embed)

        if emoji == "🇮🇹":
            await member.remove_roles(role_italien)
            embed = discord.Embed(title="From **3e-Serveur**", description="""
            Le role 'Italien' vous a été retiré !""")
            embed.set_thumbnail(url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
            await member.send(embed=embed)

        if emoji == "🔤":
            await member.remove_roles(role_latin)
            embed = discord.Embed(title="From **3e-Serveur**", description="""
            Le role 'latin' vous a été retiré !""")
            embed.set_thumbnail(url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
            await member.send(embed=embed)

        if emoji == "🇬🇷":
            await member.remove_roles(role_grec)
            embed = discord.Embed(title="From **3e-Serveur**", description="""
            Le role 'Grec' vous a été retiré !""")
            embed.set_thumbnail(url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
            await member.send(embed=embed)

token = 'TOKEN'
bot.run(token)
