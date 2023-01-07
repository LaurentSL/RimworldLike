class River:
    """There are rivers that flow towards the oceans and can merge with each other.
    They are more likely to generate in rainy areas.
    When a map is generated in a tile with a river, there will be a belt of flowing river dividing the map.
    The river cannot be pumped dry using the moisture pump.
    In version 1.0, rivers can now be built over using bridges.
    There is also a watermill generator, added in Beta 19, which requires research before it can be built.
    Watermill generators must be built adjacent to moving water.
    Rivers come in 4 sizes: huge river, large river, river, and creek.
    It affects the width of the river, and also the proportion of shallow moving water, which can be walked over,
    to deep moving water, which can't be walked over."""

    class RiverSize:
        HUGE_RIVER = "huge river"
        LARGE_RIVER = "large river"
        RIVER = "river"
        CREEK = "creek"

    def __init__(self):
        pass
        # TODO: River
