from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import random


class Season(Enum):
    SPRING = 0
    SUMMER = 1
    AUTUMN = 2
    WINTER = 3


class Weather(Enum):
    CLEAR = 0
    RAIN = 1
    SNOW = 2
    CLOUDY = 3


@dataclass
class WeatherSystem:
    """Track season, weather and temperature."""

    day: int = 0
    season: Season = Season.SPRING
    weather: Weather = Weather.CLEAR
    temperature: float = 15.0

    def advance_day(self, seed: int | None = None) -> None:
        """Advance one day updating season, weather and temperature."""
        if seed is not None:
            random.seed(seed)
        self.day += 1
        if self.day % 30 == 0:
            self.season = Season((self.season.value + 1) % 4)
        self._update_weather()
        self._update_temperature()

    def _update_weather(self) -> None:
        if self.season == Season.WINTER:
            choices = [Weather.SNOW, Weather.CLOUDY, Weather.CLEAR]
        elif self.season == Season.SUMMER:
            choices = [Weather.CLEAR, Weather.RAIN, Weather.CLOUDY]
        else:
            choices = [Weather.CLEAR, Weather.RAIN, Weather.CLOUDY]
        self.weather = random.choice(choices)

    def _update_temperature(self) -> None:
        base = {
            Season.SPRING: 15.0,
            Season.SUMMER: 25.0,
            Season.AUTUMN: 10.0,
            Season.WINTER: 0.0,
        }[self.season]
        if self.weather == Weather.SNOW:
            offset = -5.0
        elif self.weather == Weather.RAIN:
            offset = -2.0
        else:
            offset = 0.0
        self.temperature = base + offset
