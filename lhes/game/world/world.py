import pygame

from lhes.game.world.globe_coverage_percent import GlobeCoveragePercent
from lhes.game.world.overall_rainfall import OverallRainfall
from lhes.game.world.overall_temperature import OverallTemperature
from lhes.game.world.season import Season
from lhes.game.world.settlement import Settlement
from lhes.game.world.site import Site


class World:

    def __init__(self):
        self._site_group = pygame.sprite.Group()
        self._current_site: Site = None

        # TODO: Time zones are also modelled as the world actually physically exists and is fully interactive.

        self._seed: int = 1
        """A random seed is provided, but you may enter your own. 
        A given seed always produces the same geographical features such as land masses, rivers and mountains. 
        The locations of human-built features such as roads and NPC faction towns may persist on multiple uses 
        of the same seed, or they may vary somewhat from one use to the next."""

        self._globe_coverage: GlobeCoveragePercent = GlobeCoveragePercent.FIVE
        """ What percentage of the overall globe is generated. Larger globe coverage generates a fuller world, 
        but takes a longer time to load up, and can also impact performance on lower-end systems."""

        self._overall_rainfall: OverallRainfall = OverallRainfall.NORMAL
        """Choose among wetter, drier, or normal range of biomes to generate across the planet."""

        self._overall_temperature: OverallTemperature = OverallTemperature.NORMAL
        """Choose among cooler, hotter, or normal range of biomes to generate across the planet."""
        # TODO: Temperatures in regards to proximity from the equator are also correct; with hotter biomes being
        #  more central and colder biomes being closer to the poles.
        # TODO: The seasonal differences are also less pronounced near the equator, with there being a permanent
        #  summer in it.

        self._population_density: int = 20
        """Choose desired density of faction sites to generate on the planet. 
        This will largely affect your base's possible proximity to a number of faction bases and the time 
        to reach them by caravan. 
        This does not affect the frequency of friendly visits or enemy raids as that is instead affected by 
        the chosen AI and difficulty."""

        self._number_of_factions: int = 4
        """Choose the desired numbers of each type of faction to spawn in the world, including outright disabling 
        certain faction types by selecting zero of that type. The total faction count is limited to 11, with 
        the Empire Content added by the Royalty DLC, Mechanoid, and Insect Hive factions restricted to only one. 
        Removing the Empire means deactivating empire quests, and removing mechanoid and insectoids prevents 
        mechanoid raids and infestations respectively."""

        self._season: Season = Season.SPRING

        self._settlements: list[Settlement] = []

        self._sites: list[Site] = []

        self.generate()

    def generate(self):
        # TODO: When generating the world, the land masses form first, followed by rivers. An ancient society is then
        #  shallowly simulated to generate ancient roads, and modern settlements and roads are generated
        #  (often alongside ancient roads).
        self._current_site = Site()
        self._sites.append(self._current_site)
        # self._site_group

    def show_site(self):
        # TODO: Clicking a tile will show its information including its biome, terrain, overall weather,
        #  and growing period.
        pass

    def get_location_group(self):
        return self._current_site.get_location_group()

    def get_current_site_map_size(self):
        return self._current_site.get_map_size()
