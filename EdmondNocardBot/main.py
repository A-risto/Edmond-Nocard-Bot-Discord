from discord.ext import commands
import discord, time, random
from discord.utils import get
import keep_alive
keep_alive.keep_alive()
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
    nb_txt_channel = len(server.text_channels)
    nb_voice_channel = len(server.voice_channels)
    serveur_description = server.description
    nb_personne = server.member_count
    nom_server = server.name
    message = f"Le serveur **{nom_server}** contient **{nb_personne}** personnes !" \
              f" \nLa description du serveur est {serveur_description}. " \
              f"\nCe serveur possède {nb_txt_channel} salons écrit et {nb_voice_channel} salon vocaux."
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
    user_name, user_id = user.split("#")
    ban_user = await ctx.guild.bans()
    for i in ban_user:
        if i.user.name == user_name and i.user.discriminator == user_id:
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
@commands.has_permissions(administrator=True)
async def clear(ctx, nombre: int):
    messages = await ctx.channel.history(limit=nombre + 1).flatten()
    if nombre <= 30:
        for message in messages:
            await message.delete()
    else:
        await ctx.send("Trop de message a supprimer !")


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


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="__Commandes du bot : __", description="""
    ?info = donne des informations sur le serveur.

    ?regles = montre les règles du serveur.

    """, url="https://github.com/A-risto/Edmond-Nocard-Bot-Discord/blob/main/main.py")
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://lachroniquefacile.fr/wp-content/uploads/2018/07/%EF%BC%9F.png")
    embed.add_field(name="__Admins commandes :__ ", value="""

    ?ban <@utilisateur> = Ban l'utilisateur (vous pouvez spécifier une raison)

    ?unban <@utilisateur> = Debann l'utilisateur

    ?clear <nombre de message> = efface le nombre de message donné.

    ?kick <@utilisateur> = Expulse l'utilisateur (vous pouvez spécifier une raison)

    ?mute <@utilisateur> = Mute l'utilisateur (vous pouvez spécifier une raison)

    ?tempmute <@utilisateur> = Mute l'utilisateur pour une certaine durée (à spécifier)
    """, inline=False)
    embed.add_field(name="'__Funcommandes :'__", value="""
    ?wanted <montant de la prime> <@de l'utilisateur> <message qui accompagne la prime>
    ?jaccepte <@ de l'utilisateur> : accepte la demande d'octogone. Le gagnant sera désigné au hasard.
    """)
    embed.set_footer(text="Les prochaines commandes arrivent bientôt tkt")
    await ctx.send(embed=embed)




@bot.command()
async def ping(ctx):
    await ctx.send("https://media3.giphy.com/media/LZ2eNVqxJ7cP8VO90B/200.gif")

@bot.event
async def on_member_join(member):
    embed = discord.Embed(title="__Nouveau membre :__",
                          description=f"Bienvenue {member.mention} sur le serveur ! Tu peux prendre tes rôles dans le salon #Classe-LV2 !")
    embed.set_thumbnail(
        url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
    channel = member.guild.get_channel(888163341174992970)
    await channel.send(embed=embed)
    role = get(member.guild.roles, id=931283703299178566)
    await member.add_roles(role)


@bot.event
async def on_member_remove(member):
    channel = member.guild.get_channel(888163341174992970)
    embed = discord.Embed(title="__Départ d'un membre :__",
                          description=f" {member.mention} a quitté le serveur ! Il ne manquera a personne...")
    embed.set_thumbnail(
        url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
    await channel.send(embed=embed)


@bot.command()
async def repete(ctx, *texte):
    await ctx.send(" ".join(texte))
    await ctx.message.delete()


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
            embed.set_thumbnail(
                url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
            await member.send(embed=embed)

        if emoji == "🇪🇸":
            await member.remove_roles(role_espagnol)
            embed = discord.Embed(title="From **3e-Serveur**", description="""
            Le role 'Espagnol' vous a été retiré !""")
            embed.set_thumbnail(
                url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
            await member.send(embed=embed)

        if emoji == "🇮🇹":
            await member.remove_roles(role_italien)
            embed = discord.Embed(title="From **3e-Serveur**", description="""
            Le role 'Italien' vous a été retiré !""")
            embed.set_thumbnail(
                url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
            await member.send(embed=embed)

        if emoji == "🔤":
            await member.remove_roles(role_latin)
            embed = discord.Embed(title="From **3e-Serveur**", description="""
            Le role 'latin' vous a été retiré !""")
            embed.set_thumbnail(
                url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
            await member.send(embed=embed)

        if emoji == "🇬🇷":
            await member.remove_roles(role_grec)
            embed = discord.Embed(title="From **3e-Serveur**", description="""
            Le role 'Grec' vous a été retiré !""")
            embed.set_thumbnail(
                url="https://www.leparisien.fr/resizer/TJlbwM0ThlMmkTRk0SsUwMLDSf8=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/XIRP55G6MRR5VOFC3BQLEGZ6BA.jpg")
            await member.send(embed=embed)


@bot.command()
async def jaccepte(ctx, user: discord.Member = None):
    list = (ctx.author.mention, user.mention)
    list = random.choice(list)
    embed = discord.Embed(title="",
                          description=f"**{ctx.author.mention}** a accepté la proposition d'octogone de **{user.mention}**.\n La victoire revient a {list} qui a goumé son advresaire !")
    embed.set_thumbnail(url="https://i.ytimg.com/vi/tnROsP2MqQE/maxresdefault.jpg")
    embed.set_image(url="https://c.tenor.com/bwSiTUtbZrMAAAAd/mma-fight.gif")
    await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Il manque un argument.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Reste a ta place stp ta pas le droit de faire ça !")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("Oups vous ne pouvez iutilisez cette commande.")


async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role



@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason="Aucune raison n'a été renseigné"):
    if ctx.author.name == member.display_name:
        await ctx.send("Vous ne pouvez pas vous mute vous-même ! ")
    else:
        mutedRole = await getMutedRole(ctx)
        await member.add_roles(mutedRole, reason=reason)
        embed = discord.Embed(title="", description=f"le membre {member.mention} a été mute\n\nRaison : {reason}")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/945963368441843727/947233844094988338/stfu.png")
        await ctx.send(embed=embed)


@bot.command()
async def unmute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été unmute !")


@bot.command()
async def jaccepte_random(ctx):
    a = str(random.choice(ctx.channel.guild.members))
    a = a.split("#")
    liste = [a[0], ctx.author.name]
    choice = random.choice(liste)
    embed = discord.Embed(title="",
                          description=f"Cette octogone verra s'affronter ``{ctx.author.name}`` et ``{a[0]}``.\nLa victoire revient a **{choice}** qui a goumé son adversaire !")
    embed.set_thumbnail(url="https://i.ytimg.com/vi/tnROsP2MqQE/maxresdefault.jpg")
    embed.set_image(url="https://c.tenor.com/bwSiTUtbZrMAAAAd/mma-fight.gif")
    await ctx.send(embed=embed)

@bot.command()
async def pf(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://www.cliqueduplateau.com/wordpress/wp-content/uploads/2015/12/flip.gif")
    msg = await ctx.send(embed=embed)
    time.sleep(3)
    await msg.delete()
    choice = random.choice([True, False])
    if choice:
        embed2 = discord.Embed(title=" ", description="C'est **pile** ! ")
        embed2.set_image(url="https://jaimelesmots.com/wp-content/uploads/2019/10/pile.jpeg")
        await ctx.send(embed=embed2)
    else:
        embed2 = discord.Embed(title=" ", description="C'est **face** ! ")
        embed2.set_image(url="https://jaimelesmots.com/wp-content/uploads/2019/10/face.jpeg")
        await ctx.send(embed=embed2)
      
token = 'TOKEN'
bot.run(token)
