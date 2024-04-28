import discord
from discord.ext import commands
from discord import FFmpegPCMAudio



intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="avi/", intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Bot listo para usar')
    print("------------------")

@client.command(pass_context=True)
async def entrar(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("No estas en un canal de voz")

@client.command(pass_context=True)
async def salir(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Saliendo del canal de voz")
    else:
        await ctx.send("No estoy en un canal de voz")

@client.command(pass_context=True)
async def pausa(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if(voice.is_playing()):
        voice.pause()
    else:
        await ctx.send("No hay ninguna cancion reproduciendose")

@client.command(pass_context=True)
async def reanudar(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if(voice.is_paused()):
        voice.resume()
    else:
        await ctx.send("No hay ninguna cancion pausada")

@client.command(pass_context=True)
async def detener(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if(voice.is_playing()):
        voice.stop()
    else:
        await ctx.send("No hay ninguna cancion reproduciendose")

@client.command(pass_context=True)
async def cancion(ctx, arg):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio(arg + '.mp3')
    player = voice.play(source)

@client.command(pass_context=True)
async def comandos(ctx):
    embed = discord.Embed(title="Comandos del bot avi (usando avi/)", description="entrar, salir, pausa, reanudar, detener, cancion, comandos", color=0x00ffff)
    await ctx.send(embed=embed)

avi = "MTIzMTcwMzUwMTY3NjIxNjM0MA.G4aFyN.1_tptHOpXQRkdLD0EseslbRFdTkAc594sGRyuc"

client.run(avi)