# Discord RSS Bot

Ce bot Discord récupère les dernières entrées de flux RSS à partir de liens spécifiés et les envoie sur un serveur Discord.

## Fonctionnalités

- Ajout de liens RSS avec la commande `!setrss`.
- Récupération périodique des entrées des flux RSS.
- Affichage des informations du bot avec les commandes `!name` et `!version`.

## Configuration

1. Installez les dépendances :
   ```bash
   pip install discord.py feedparser
Remplacez les valeurs suivantes dans le script par les vôtres :

'YOUR_DISCORD_BOT_TOKEN': Le token de votre bot Discord.
'YOUR_DISCORD_GUILD_ID': L'ID de votre serveur Discord.
'YOUR_DISCORD_CHANNEL_ID': L'ID du canal Discord où les entrées seront envoyées.
Exécutez le script :

python main.py

## Commandes Discord
!setrss [lien]: Ajoute un nouveau lien RSS à surveiller.
!name: Affiche le nom du bot.
!version: Affiche la version du bot.
## Auteur

# Valentin B.

