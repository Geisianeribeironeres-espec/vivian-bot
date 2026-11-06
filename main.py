import os
import discord
from discord.ext import commands
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Vivian Bot Online!"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

threading.Thread(target=run_web).start()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logado como {bot.user}')

@bot.command()
async def oi(ctx):
    await ctx.send('Oi! Sou a Vivian, bot do Free Fire! 🔥')

bot.run(os.environ.get("DISCORD_TOKEN"))
