import discord
from discord import member
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="pp/", intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Bot listo para usar')
    print("------------------")

@client.event
async def on_member_join(member):
    print(f'{member} se ha unido al servidor.')
    chanel = client.get_channel(1231688761218433065)
    await chanel.send(f'{member} se ha unido al servidor.')
@client.event
async def on_member_remove(member):
    print(f'{member} se ha ido al servidor.')
    chanel = client.get_channel(1231688761218433065)
    await chanel.send(f'{member} se ha ido al servidor.')

@client.event
async def on_message(message):
    if message.content == "negro" or message.content == "puto" or message.content == "puta" or message.content == "boliviano" or message.content == "pito" or message.content == "gay":
        await message.delete()
        await message.channel.send("nah ah")
    else:
        await client.process_commands(message)


"----------------------------------------------------------------------------------------"




@client.command(pass_context=True)
async def instagram(ctx):
    embed = discord.Embed(title="Instagram de Pato El Pez", url="https://www.instagram.com/patoelpez/", color=0x00ffff)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def facebook(ctx):
    embed = discord.Embed(title="Facebook de Pato El Pez", url="https://www.facebook.com/patoelpez", color=0x00ffff)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def twitter(ctx):
    embed = discord.Embed(title="Twitter de Pato El Pez", url="https://twitter.com/PatoElPez", color=0x00ffff)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def youtube(ctx):
    embed = discord.Embed(title="Youtube de Pato El Pez", url="https://www.youtube.com/channel/UCnT0p3XGjw0P7aKp0cWkQkA", color=0x00ffff)
    await ctx.send(embed=embed)


@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="incumplimiento de las reglas"):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} fue baneado")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        embed = discord.Embed(title="No tienes permisos para usar este comando", color=0x00ffff)
        await ctx.send(embed=embed)

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="incumplimiento de las reglas"):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} fue expulsado")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        embed = discord.Embed(title="No tienes permisos para usar este comando", color=0x00ffff)
        await ctx.send(embed=embed)

@client.command(pass_context=True)
async def reglas(ctx):
    embed = discord.Embed(title="Reglas del server", color=0x00ffff)
    embed.set_author(name="el owner")
    embed.add_field(name="respeto", value="respetar a todos", inline=False)
    embed.add_field(name="no spam", value="no hacer spam", inline=False)
    embed.add_field(name="no acoso", value="no hacer acoso o bullying", inline=False)
    embed.add_field(name="privacidad", value="no publicar informacion personal", inline=False)
    embed.set_footer(text="Creador: Pato El Pez")
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def comandos(ctx):
    embed = discord.Embed(title="Comandos del bot Pato El Pez (usando pp/)", description="reglas, comandos, instagram, facebook, twitter, youtube", color=0x00ffff)
    await ctx.send(embed=embed)


wafflehoe = 'MTIzMDg4MjE3MzcwNDIxMjUyMQ.G8MVGl.XMWJ64lXHYDOyWNwTXjRV0sC2_ck-y3R8bXzqA'    

client.run(wafflehoe)