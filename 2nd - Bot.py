from discord.ext import commands
import discord, random, time
from discord.utils import get
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print("Bot prêt...")
    await bot.change_presence(activity=discord.Game("?help"))

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
@commands.has_permissions(manage_messages=True)
async def clear(ctx, nombre: int):
    messages = await ctx.channel.history(limit=nombre + 1).flatten()
    if nombre <= 30:
        for message in messages:
            await message.delete()
    else:
        await ctx.send("Trop de message a supprimer !")
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
        await ctx.send("ouais tu fais le fou un peu")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("Oups vous ne pouvez iutilisez cette commande.")

@bot.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == 888163341174992966:
        channel = after.channel
        try:
            if before.channel.members == [] and not before.channel.id == 1007029040688922745 and not before.channel.id == 947832541660983306:
                if before.channel.category_id == 888163341174992968:
                    await before.channel.delete()
        except:
            pass

        if channel.id == 1007029040688922745:
            guild = after.channel.guild
            private_channels = discord.utils.get(guild.categories, id=888163341174992968)
            voice_channel = await guild.create_voice_channel("Salon de "+member.name, overwrites=None, category=private_channels)
            time.sleep(1)
            await member.move_to(voice_channel)
            await voice_channel.set_permissions(member, connect=True, speak=True, move_members=True, manage_channels=True, view_channel=True)


async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role


@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason="Aucune raison n'a été renseigné"):
    if not member.bot:
        if ctx.author.name == member.display_name:
            await ctx.send("Vous ne pouvez pas vous mute vous-même ! ")
        else:
            if member.top_role >= ctx.author.top_role:
                await ctx.send("Vous ne pouvez pas mute une personne égale ou supérieure à vous !")
            else:
                mutedRole = await getMutedRole(ctx)
                await member.add_roles(mutedRole, reason=reason)
                embed = discord.Embed(title="",
                                      description=f"le membre {member.mention} a été mute\n\nRaison : {reason}")
                embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                embed.set_thumbnail(
                    url="https://media.discordapp.net/attachments/945963368441843727/947233844094988338/stfu.png")
                await ctx.send(embed=embed)
    else:
        await ctx.send("Pk tu veux mute un bot ?")


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

@bot.command()
async def repete(ctx, *texte):
    await ctx.send(" ".join(texte))
    await ctx.message.delete()
@bot.command()
async def unmute(ctx, member: discord.Member, *, reason="Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason=reason)
    await ctx.send(f"{member.mention} a été unmute !")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="**__Commande du bot__**", description='''
    Préfixe : ``?``
    
    __Commande générale :__
    info : donne des infos sur le serv
    pf : fait un pile ou face
    ping : verif que le bot fonctionne et est on
    repete <message> : fait répéter votre phrase à un bot
    jaccepte <@user> : provoque votre adversaire en octogone
    jaccepte_random : provoque un random en octogone
    
    __Commande Admin :__
    ban/unban <@user> : ban le mec 
    mute/unmute <@user> : mute le mec
    kick <@user> : dégage le mec du serv mais sans le ban
    clear <nb message> : suppr le nb de message indiqué (<30)
    ''', inline=False)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Question_mark_%28black%29.svg/640px-Question_mark_%28black%29.svg.png")
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
TOKEN = ""
bot.run(TOKEN)
