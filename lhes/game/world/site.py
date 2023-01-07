import logging

import pygame

from lhes.game.biome.biome import Biome
from lhes.game.biome.temperature import Temperature
from lhes.game.world.location import Location
from lhes.game.world.map_size import MapSize
from lhes.game.world.quadrums import Quadrums
from lhes.game.world.river import River
from lhes.game.world.road import Road
from lhes.game.world.site_terrain import SiteTerrain
from lhes.game.world.terrain import Terrain


class Site:

    def __init__(self):

        self._map_size: MapSize = MapSize.DEV

        self._biome: Biome = None

        self._elevation: int = 0
        """A map tile's distance above sea level is its elevation. Higher elevation brings with it colder weather."""

        self._latitude = None
        """The coordinates of a map tile includes its latitude which affects its temperature range and amount of 
        daylight. In polar latitudes the sun may not set or rise completely for a long time."""

        self.rainfall: int = 100
        """Each map tile has a certain amount of rainfall, given in average number of millimeters per year. 
        It determines how often it will rain, not counting the automatic rain after a certain number of fire tiles 
        are on the map."""

        self._site_terrain: SiteTerrain = SiteTerrain.SMALL_HILLS
        self._temperature: Temperature = None
        self._quadrums: Quadrums = Quadrums.APRIMAY
        self._road_type: Road.RoadType = None
        self._river_size: River.RiverSize = None

        self._overall_weather = None

        self._growing_period = None

        self._location_group: pygame.sprite.Group = pygame.sprite.Group()
        self._size: pygame.Vector2 = pygame.Vector2(self._map_size, self._map_size)
        self._grid: list[list[Location]] = []

        self.generate()

    # TODO: Caves
    #  Caves are sometimes found in mountains and may contain harvestable mushrooms or dormant insectoid hives with
    #  a small group of insectoids. Dormant hives won't spawn additional hives or insectoids.
    #
    # TODO: Dormant hives
    #  Hives can be a good source of food and/or a valuable trade commodity if you steal their jelly while the
    #  defenders are asleep. If an insectoid is asleep on a stack of jelly or other item, do not try to take it or
    #  you may awake them and put your colonist in peril. Colonists' default threat response may activate upon
    #  seeing insectoids, even if the insectoids are asleep. Be careful that your jelly harvesters are not set to
    #  "Attack" by default. If their default response is "Flee," you will need to manually prioritize them to haul
    #  the jelly. Otherwise it's possible for them to get stuck repeatedly trying to enter the cave, then fleeing,
    #  which could leave them too close to the cave when the insectoids wake up.
    #  Take note of what time the insectoids on your map fall asleep each night and wake up in the morning.
    #  It may be helpful to create an allowed area which excludes the insectoid cave. You can switch your hauler
    #  to "Unrestricted" temporarily and have them manually prioritize collecting the jelly when you are certain
    #  the insectoids are asleep. Another method might be to wall in the entrance to the cave and forbid the door,
    #  only unforbidding it to send in your jelly harvester. This will prevent your hunters, plant cutters,
    #  animal tamers and haulers from wandering into the cave while the insectoids are awake.
    #  The hive and its insectoids can be harmed without any colonist actions. Insectoids may suffer from extreme
    #  temperatures; cold snaps will kill the weaker ones. Insectoids will be aggressive towards humans,
    #  but mutually non-hostile with wildlife. A wild human counts as wildlife. Walls can be built which may guide
    #  raiders into the cave if the raiders spawn in the right locations. However, if the raiders destroy the hive,
    #  you will lose your supply of jelly.
    #  Hungry predators may also try to hunt insectoids. Most of the time the predator will be killed, but may down
    #  some insectoids by wounding them. When the insectoids die, you can unforbid and collect the corpses for
    #  butchering, by the same method used to harvest insect jelly.
    # TODO: Cave flora
    #  You may find Agarilux, Bryolux or Glowstool in these caves. Instead of needing light to grow, they die when
    #  exposed to excess sunlight.

    def generate(self):
        logging.debug("Start generating map")
        for row in range(int(self._size.y)):
            locations = []
            for column in range(int(self._size.x)):
                position = pygame.Vector2(column, row)
                terrain = Terrain.get_random()
                locations.append(Location([self._location_group], position, terrain))
            self._grid.append(locations)
        logging.debug("End generating map")

    def get_location_group(self):
        return self._location_group

    def _debug(self):
        for row in range(int(self._size.y)):
            for column in range(int(self._size.x)):
                print(f"location: {self._grid[row][column].rect}")

    def get_map_size(self):
        return self._map_size
