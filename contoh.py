import discord
from discord.ext import commands
import random, os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command("sampah")
async def saran_daur_ulang(ctx, item: str):
    # Daftar barang yang bisa bernilai harganya
    nama_sampah = ['kertas', 'plastik', 'logam', 'kaca', 'elektronik bekas', 'minyak jelanta', 'sampah organik', 'bahan tekstil', 'karet']
    
    if item.lower() in nama_sampah:
        await ctx.send(f"Baiklah! {item.capitalize()} barang sampah bernilai")
    else:
        await ctx.send(f"Baiklah! {item.capitalize()} sampah ini tidak bernilai.")


bot.run("")