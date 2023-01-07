import random

from lhes.game.world.terrain_type import TerrainType


class Terrain:
    """Terrain consists of the map's walking surface, terrain features, and mountain areas. Terrain affects things
    including walking speed, where plants can grow, and may prohibit construction.
Natural surface terrain includes soil, rich soil, marshy soil, marsh, mud, sand, lichen-covered dirt, gravel,
rough stone (granite, marble, etc.), rough-hewn stone, shallow water, and deep water.
Terrain features include steam geysers and mountains. The steam from a geyser produces heat and an enclosed area
around it will heat up unless unroofed. A mountain cannot be destroyed, even if all of its stone and ore has been
mined out. What remains are terrain tiles listed as 'overhead mountain'."""

    @staticmethod
    def get_random():
        return Terrain(random.randint(1, 20), random.choice([True, False]), random.choice([True, False]))

    def __init__(self,
                 terrain_type_id: int,
                 mountain: bool = False,
                 geyser: bool = False):
        self._terrain_type: TerrainType = TerrainType()
        self._terrain_type_id: int = terrain_type_id
        self._is_mountain: bool = mountain
        self._is_geyser: bool = geyser
        """Steam geysers are terrain features that allow the placement of a geothermal generator on them and also 
        output a significant amount of heat when sealed in a roofed room.
        The steam geyser sprays after a random delay between 500 ticks (8.33 secs) and 2,000 ticks (33.33 secs). 
        It will then spray for between 200 ticks (3.33 secs) and 500 ticks (8.33 secs). 
        While spraying, it will output 40 heat every 20 ticks (0.33 secs). 
        Thus, it averages 16.15 heat per second, with no maximum temperature.
        Besides their use in power generation, they can also be used to heat bases and greenhouses without the need 
        for electricity or fuel by sealing them in. Like any means of temperature regulation, geysers require an 
        enclosed and enroofed room to actually cause a change in heat. If you don't want heat, keep the geothermal 
        room without a roof."""
        # TODO: Filth masks, proper terrain affordance, driesTo, extinguishesFire, beauty, cleanliness, deterioration,
        #  special attacks, traversedThought, perceived path costs vs path costs

    def get_terrain_type(self) -> dict[str, str]:
        return self._terrain_type.get(self._terrain_type_id)

    def get_terrain_type_name(self) -> str:
        return self._terrain_type.get_name(self._terrain_type_id)

    def get_move_speed_modifier(self) -> int:
        return self._terrain_type.get_move_speed_modifier(self._terrain_type_id)

    def get_fertility(self) -> int:
        return self._terrain_type.get_fertility(self._terrain_type_id)

    def get_terrain_support(self) -> str:
        return self._terrain_type.get_terrain_support(self._terrain_type_id)

    def get_color(self) -> str:
        return self._terrain_type.get_color(self._terrain_type_id)
