import discord
from discord.ext import commands, tasks
import feedparser

FILE = 'links.txt'
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
GUILD_ID = 'YOUR_DISCORD_GUILD_ID'
CHANNEL_ID = 'YOUR_DISCORD_CHANNEL_ID'

intents = discord.Intents.default()
intents.messages = True  # Activer la réception des événements de messages

bot = commands.Bot(command_prefix='!', intents=intents)

def create_instance(link):
    return feedparser.parse(link)

def save_links(file, links):
    with open(file, 'w') as file:
        for link in links:
            file.write(link + '\n')

def get_saved_links(file):
    links = []
    with open(file, 'r') as file:
        content = file.read()
        links = content.split('\n')
    links = [link.strip() for link in links if link.strip()]
    return links

def get_entries(news_feed):
    entries = []
    for i in range(0, len(news_feed.entries)):
        if i == (len(news_feed.entries)-1):
            entries.append((news_feed.entries[0]['title'], news_feed.entries[0]['id']))
    return entries

@tasks.loop(minutes=5)
async def fetch_entries():
    full_entries = []
    instance_list = []
    links = get_saved_links(FILE)

    for link in links:
        instance = create_instance(link)
        instance_list.append(instance)

    for instance in instance_list:
        entries = get_entries(instance)
        full_entries.append((entries, instance.feed.title))

    # Afficher les entrées (optionnel)
    for entries, title in full_entries:
        print(f"Titre du flux : {title}")
        for entry_title, entry_link in entries:
            print(f"  - {entry_title}: {entry_link}")

    # Envoyer les entrées à Discord
    guild = bot.get_guild(int(GUILD_ID))
    channel = guild.get_channel(int(CHANNEL_ID))
    await send_entries_to_discord(entries, channel)

async def send_entries_to_discord(entries, channel):
    for entry_title, entry_link in entries:
        await channel.send(f"**Titre :** {entry_title}\n**Lien :** {entry_link}")

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')
    # Lancer la tâche fetch_entries lorsque le bot est prêt
    fetch_entries.start()

@bot.command(name="name")
async def get_bot_name(ctx):
    await ctx.send(f"Je m'appelle {bot.user.name}")

@bot.command(name="version")
async def get_bot_version(ctx):
    await ctx.send(f"Version du bot : {bot.version}")

@bot.command(name="setrss")
async def set_rss_sources(ctx, link):
    # Ajouter le nouveau lien RSS au fichier
    links = get_saved_links(FILE)
    links.append(link)
    save_links(FILE, links)
    await ctx.send(f"Flux RSS ajouté\n{link}")

# Lancer le bot
bot.run(TOKEN)
