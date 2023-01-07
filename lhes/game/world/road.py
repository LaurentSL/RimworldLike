class Road:
    """There are many roads throughout the world. They double the speed of any caravans using them, and factions
    tend to settle near roads. Visitors, caravans, traders or raiders are also tend to arrive and leave on a road.
    Roads are generated independent from the world seed, so even if you generate a world using the same seed,
    you might not get the same road layout. Ancient asphalt roads are generated through an ancient civilization
    simulation, while modern dirt and stone roads are generated connecting faction bases to main roads.
    They come in 5 types: path, dirt road, stone road, ancient asphalt road and ancient asphalt highway.
    They are functionally the same, with difference only being appearance when generated on a map.
    Dirt roads use packed dirt, stone roads use flagstones of the local stone and ancient asphalt roads use
    broken asphalt. None of these can be disassembled for resources.
    Sometimes other objects will generate alongside roads, for example the ancient concrete barrier or
    ancient lamppost alongside the ancient asphalt highway.
    These serve no function except cover or disassembly for steel."""

    class RoadType:
        PATH = "path"
        DIRT_ROAD = "dirt road"
        STONE_ROAD = "stone road"
        ANCIENT_ASPHALT_ROAD = "ancient asphalt road"
        ANCIENT_ASPHALT_HIGHWAY = "ancient asphalt highway"

    def __init__(self):
        pass
        # TODO: Road
