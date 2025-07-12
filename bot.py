import discord
from discord.ext import commands
from config import token
from logic import Pokemon , magic , fighter
import random

# Setting up intents for the bot
intents = discord.Intents.default()  # Getting the default settings
intents.messages = True              # Allowing the bot to process messages
intents.message_content = True       # Allowing the bot to read message content
intents.guilds = True                # Allowing the bot to work with servers (guilds)

# Creating a bot with a defined command prefix and activated intents
bot = commands.Bot(command_prefix='!', intents=intents)

# An event that is triggered when the bot is ready to run
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')  # Outputs the bot's name to the console

# The '!go' command
@bot.command()
async def go(ctx):
    author = ctx.author.name  # Getting the name of the message's author
    # Check whether the user already has a Pokémon. If not, then...
    if author not in Pokemon.pokemons.keys():
        chance = random.randint(1,3)
        if chance == 1:
            pokemon = Pokemon(author)
        elif chance == 2:
            pokemon = magic(author)
        elif chance == 3:
            pokemon = fighter(author)
        await ctx.send(await pokemon.info())  # Sending information about the Pokémon
        image_url = await pokemon.show_img()  # Getting the URL of the Pokémon image
        if image_url:
            embed = discord.Embed()  # Creating an embed message
            embed.set_image(url=image_url)  # Setting up the Pokémon's image
            await ctx.send(embed=embed)  # Sending an embedded message with an image
        else:
            await ctx.send("Failed to upload an image of the pokémon.")
    else:
        await ctx.send("You've already created your own Pokémon.")  # A message that is printed whether a Pokémon has already been created

@bot.command()
async def attack(ctx):
    target = ctx.message.mentions[0] if ctx.message.mentions else None
    if target:
        if target.name in Pokemon.pokemons and ctx.author.name in Pokemon.pokemons:
            enemy = Pokemon.pokemons(target.name)
            attacker = Pokemon.pokemons(ctx.author.name)
            result = await attacker.attack(enemy)
            await ctx.send(result)
        else:
            await ctx.send("kedua trainer harus punya pokemon yang akan digunakan!")
    else:
        await ctx.send("pilih lawan mu!,sebutkan nama usernya!")
# Running the bot
bot.run(token)
