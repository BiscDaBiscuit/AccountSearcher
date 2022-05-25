#The first version was made by Splazz Benni#8350 (My Friend)
from colorama import Fore, Back, Style
import time
print(Fore.RED)


Base = '[+] '
Repl = 'repl.it:  https://replit.com/@'
About = 'About.me:  https://about.me/'
Github = 'Github:  https://www.github.com/'
Codecademy = 'Codecademy: https://www.codecademy.com/profiles/'
Roblox = 'Roblox:  https://www.roblox.com/user.aspx?username='
Slack1 = 'Slack: https://'
Slack2 = '.slack.com'
Spotify = 'Spotify:  https://open.spotify.com/user/'
Scratch = 'Scratch:  https://scratch.mit.edu/users/'
PokemonShowdown = 'Pokemon Showdown: https://pokemonshowdown.com/users/'
Pastebin = 'Pastebin:  https://pastebin.com/u/'
Patreon = 'Patreon: https://www.patreon.com/'
Steam = 'Steam:  https://steamcommunity.com/id/'
TikTok = 'TikTok: https://tiktok.com/@'
Twitch = 'Twitch: https://www.twitch.tv/'
Giphy = 'Giphy: https://giphy.com/'
FortniteTracker = 'FortniteTracker: https://fortnitetracker.com/profile/all/'
Facebook = 'Facebook:  https://www.facebook.com/'
Duolingo = 'Duolingo:  https://www.duolingo.com/profile/'
YouTube = 'Youtube: https://www.youtube.com/'
Twitter = 'Twitter: https://twitter.com/'
Instagram = 'Instagram: https://www.instagram.com/'


print('What is the user name? ')
print(Fore.GREEN)
user = input()

print(Fore.RED)
print(Base + 'Finding accounts under the name of:  ' + user)
time.sleep(0.7)

print('Found!')
print()
print('Here are the account links with the user ' + user + ' accociated:  ')



print(Fore.BLUE)
Repl = (Base + Repl + user)
Github = (Base + Github + user)
About = (Base + About + user)
Codecademy = (Base + Codecademy + user)
Roblox = (Base + Roblox + user)
Slack = (Base + Slack1 + user + Slack2)
Spotify = (Base + Spotify + user)
Scratch = (Base + Scratch + user)
PokemonShowdown = (Base + PokemonShowdown + user)
Pastebin = (Base + Pastebin + user)
Patreon = (Base + Patreon + user)
Steam = (Base + Steam + user)
TikTok = (Base + TikTok + user)
Twitch = (Base + Twitch + user)
Giphy = (Base + Giphy + user)
FortniteTracker = (Base + FortniteTracker + user)
Facebook = (Base + Facebook + user)
Duolingo = (Base + Duolingo + user)
YouTube = (Base + YouTube + user)
Twitter = (Base + Twitter + user)
Instagram = (Base + Twitter + user)

print()
print(Repl)
print(Github)
print(About)
print(Codecademy)
print(Roblox)
print(Slack)
print(Spotify)
print(Scratch)
print(PokemonShowdown)
print(Pastebin)
print(Patreon)
print(Steam)
print(TikTok)
print(Twitch)
print(Giphy)
print(FortniteTracker)
print(Facebook)
print(Duolingo)
print(YouTube)
print(Twitter)
