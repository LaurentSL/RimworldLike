from lhes.game import settings
from lhes.tools import utils
from lhes.tools.singleton_decorator import SingletonDecorator


@SingletonDecorator
class TerrainType:

    def __init__(self):
        self._data: dict[str, dict[str, str]] = self._load()

    @staticmethod
    def _load():
        filename = settings.TERRAIN_TYPE_CSV_FILENAME
        return utils.load_csv_as_dict(filename, settings.CSV_SEPARATOR)

    def get(self, terrain_type: int) -> dict[str, str]:
        return self._data[str(terrain_type)]

    def get_name(self, terrain_type: int) -> str:
        return self.get(terrain_type)['Name']

    def get_move_speed_modifier(self, terrain_type: str) -> int:
        return int(self.get(terrain_type)['Move Speed Modifier'])

    def get_fertility(self, terrain_type: str) -> int:
        return int(self.get(terrain_type)['Fertility'])

    def get_terrain_support(self, terrain_type: str) -> str:
        return self.get(terrain_type)['Terrain Support']

    def get_color(self, terrain_type: str) -> str:
        return self.get(terrain_type)['Color']
