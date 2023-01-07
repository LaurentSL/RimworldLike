import logging

# game setup
DEBUG = False
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_HALF_WIDTH = SCREEN_WIDTH // 2
SCREEN_HALF_HEIGHT = SCREEN_HEIGHT // 2
SCREEN_TITLE = "RimworldLike"
FPS = 60
TILE_SIZE = 64

# Log format
LOG_FORMAT = "%(asctime)s - %(threadName)s - %(levelname)s - %(name)s - %(filename)s - %(module)s.%(funcName)s:%(lineno)s - %(message)s"
LOG_FILENAME = 'log/game.log'
LOG_LEVEL = logging.DEBUG

# Camera
CAMERA_MOVE_SPEED = 50
CAMERA_ZOOM_SPEED = 3

# Data files
CSV_SEPARATOR = ";"
TERRAIN_TYPE_CSV_FILENAME = "../data/terrain_type.csv"
