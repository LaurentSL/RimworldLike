from lhes.game.biome.fauna.fauna import Fauna
from lhes.game.biome.flora.flora import Flora


class Biome:
    """There are different biomes in RimWorld. They each correspond to specific features.
    Each biome is more likely to include certain features based on its real world equivalent.

    Biomes are types of area on a planet, characterized by their terrain properties, climate, flora and fauna,
    diseases and special challenges.
    Each world tile has one particular biome.
    Oceans and lakes appear as world tiles but are not playable biomes.
    There are twelve playable biomes types in RimWorld, which can be divided into three categories: Warm, Hot and Cold.
    https://rimworldwiki.com/wiki/Biomes
    """

    class BiomeType:
        WARM_TEMPERATE_FOREST = "warm temperate forest"
        WARM_TEMPERATE_SWAMP = "warm temperate swamp"
        WARM_TROPICAL_RAINFOREST = "warm tropical rainforest"
        WARM_TROPICAL_SWAMP = "warm tropical swamp"
        HOT_ARID_SHRUBLAND = "hot arid shrubland"
        HOT_DESERT = "hot desert"
        HOT_EXTREME_DESERT = "hot extreme desert"
        COLD_BOREAL_FOREST = "cold boreal forest"
        COLD_BOG = "cold bog"
        COLD_TUNDRA = "cold tundra"
        COLD_ICE_SHEET = "cold ice sheet"
        COLD_SEA_ICE = "cold sea ice"

    class Difficulty:
        EASY = 1
        NORMAL = 2
        HARD = 3
        VERY_HARD = 4
        HOPELESS = 5

    class GrowingSeason:
        ALL_YEAR = "all year"
        A_20_60_DAYS = "20 / 60 days"

    def __init__(self):
        # TODO: Biome (https://rimworldwiki.com/wiki/Biomes)
        # TODO: Instancier tous les biomes (après avoir modélisé le premier)

        self._biome_name = "Generic Biome"
        self._difficulty = Biome.Difficulty.EASY
        self._rate_flora: int = 0
        self._rate_fauna: int = 0
        self._growing_season: list[Biome.GrowingSeason] = []
        self._temperature_average_min: int = 0
        self._temperature_average_max: int = 0
        self._temperature_variation_min: int = 0
        self._temperature_variation_max: int = 0
        self._with_river: bool = False
        self._with_road: bool = False
        self._movement_difficulty_average: int = 1
        self._movement_difficulty_min: int = 1
        self._movement_difficulty_max: int = 1
        self._forageability: int = 0  # Aptitude au fourrage
        self._grazable = 0  # ? ; only during growing season
        # TODO: Comprendre grazable
        self._disease_frequency_by_year: int = 0
        self._growing_period = ""
        self._flora: list[Flora] = []
        self._fauna: list[Fauna] = []
