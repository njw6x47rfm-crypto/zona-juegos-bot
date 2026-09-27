import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Zona de Juegos conectado como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 ¡Pong! Zona de Juegos está funcionando.")

@bot.command()
async def hola(ctx):
    await ctx.send(f"👋 ¡Hola {ctx.author.mention}! Bienvenido a Zona de Juegos.")

if not TOKEN:
    raise RuntimeError("Falta configurar DISCORD_TOKEN")

bot.run(TOKEN)
