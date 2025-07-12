import aiohttp  # A library for asynchronous HTTP requests
import random

class Pokemon:
    pokemons = {}
    # Object initialisation (constructor)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.power = random.randint(30,60)
        self.hp = random.randint(200,400)
        self.exp = 0
        self.level = 0
        self.defense = 0
        self.name = None
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def attack(self, enemy):
        if isinstance(enemy, magic):
            chance = random.randint(1, 5)
            if chance == 1:
                return "Pokemon Penyihir menggunakan perisai dalam pertarungan"
            
        if enemy.hp > self.power:
            self.power -= enemy.defense
            enemy.hp -= self.power
            return f"Pertempuran @{self.pokemon_trainer} dengan @{enemy.pokemon_trainer}\nKesehatan @{enemy.pokemon_trainer} sekarang {enemy.hp}"
        else:
            enemy.hp = 0
            self.exp + 1
            if self.exp == 10:
                self.level + 1
                self.power + 20
                self.hp + 43
                self.defense + 13
                return f"@{self.pokemon_trainer} mencapai level{self.level},mendapat bonus 21 damage,43 hp,dan 13 ketahanan!"
            return f"@{self.pokemon_trainer} menang dari @{enemy.pokemon_trainer}!"
            
            

    async def get_name(self):
        # An asynchronous method to get the name of a pokémon via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data['forms'][0]['name']  # Returning a Pokémon's name
                else:
                    return "Pikachu"  # Return the default name if the request fails

    async def info(self):
        # A method that returns information about the pokémon
        if not self.name:
            self.name = await self.get_name()  # Retrieving a name if it has not yet been uploaded
        return f"""The name of your Pokémon: {self.name}
                HP:{self.hp}
                DAMAGE:{self.power}
                DEFENSE:{self.defense}"""

    async def show_img(self):
        # An asynchronous method to retrieve the URL of a pokémon image via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data['sprites']['front_default']  # Returning a Pokémon's name
                else:
                    return None  # Return the default name if the request fails
class magic(Pokemon):
    pass
class fighter(Pokemon):
    async def attack(self, enemy):
        super_power = random.randint(5,50)
        self.power += super_power
        result = await super().attack(enemy)
        self.power -= super_power
        return result + f"\npengguna menggunakan damage booster sebesar:{super_power}"
