from lhes.game.biome.biome import Biome
from lhes.game.biome.fauna.fauna import Fauna
from lhes.game.biome.flora.flora import Flora


class BiomeWarmTemperateForest(Biome):

    def __init__(self):
        super().__init__()

        self._biome_name = "Biome Warm - Temperate Forest"
        self._difficulty = Biome.Difficulty.EASY
        self._rate_flora: int = 100
        self._rate_fauna: int = 100
        self._growing_season: list[Biome.GrowingSeason] = [Biome.GrowingSeason.ALL_YEAR,
                                                           Biome.GrowingSeason.A_20_60_DAYS]
        self._temperature_average_min: int = 0
        self._temperature_average_max: int = 25
        self._temperature_variation_min: int = -25
        self._temperature_variation_max: int = 35
        self._with_river: bool = True
        self._with_road: bool = True
        self._movement_difficulty_average: int = 1
        self._movement_difficulty_min: int = 1
        self._movement_difficulty_max: int = 3
        self._forageability: int = 100
        self._grazable = 1  # ? ; only during growing season
        self._disease_frequency_by_year: int = 1.2
        self._growing_period = "year round"
        self._flora: list[Flora] = []
        # Anima tree, Berry bush, Brambles, Bush, Dandelions, Gauranlen tree, Grass,
        # Oak tree, Poplar tree, Tall grass, Timbershroom, Wild healroot
        self._fauna: list[Fauna] = []
        # Alpaca, Bison, Boomalope, Boomrat, Cougar, Deer, Donkey, Gazelle, Grizzly bear, Guinea pig, Hare, Horse, Ibex,
        # Lynx, Megasloth, Muffalo, Raccoon, Rat, Red fox, Rhinoceros, Squirrel, Timber wolf, Tortoise, Turkey, Warg,
        # Wild boar, Yak
