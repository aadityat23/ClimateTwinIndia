from dataclasses import dataclass


@dataclass
class ClimateState:
    date: str
    latitude: float
    longitude: float
    rainfall_mm: float
    max_temperature_c: float