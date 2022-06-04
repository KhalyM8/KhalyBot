import discord
from discord.ext import commands
from github import Github
from dotenv import load_dotenv
import os

load_dotenv("tokens.env")

GClient = Github(os.getenv("GITHUB_TOKEN"))

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is Online')

@client.command()
async def listRepos(ctx,arg):
    user = GClient.get_user(arg)
    for repo in user.get_repos():
        await ctx.send(repo.full_name)
        await ctx.send("https://github.com/"+ repo.full_name)

client.run(os.getenv("DISCORD_TOKEN"))