from urllib.request import urlopen
from dataclasses import dataclass
import json

@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_coordinates() -> Coordinates:
    """Returns current coordinates using IP address"""
    latitude = 56.8575
    longitude = 60.6125

    return Coordinates(latitude=latitude, longitude=longitude)


