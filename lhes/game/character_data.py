import datetime
from dataclasses import dataclass

import pygame


@dataclass
class CharacterData:
    name: str
    position: pygame.Vector2
    birthdate: datetime.date
    race: str
