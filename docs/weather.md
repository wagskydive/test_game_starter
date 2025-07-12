# Weather and Seasons

The `weather` module introduces a very small simulation for seasonal changes and
daily weather patterns. Use `WeatherSystem` to advance the current day and query
weather information.

```python
from src.weather import WeatherSystem, Season, Weather

w = WeatherSystem()
w.advance_day()
print(w.season, w.weather, w.temperature)
```

Seasons rotate every 30 days in the order Spring, Summer, Autumn and Winter.
`advance_day()` randomly chooses a weather state based on the season and updates
the temperature. Winter can produce snow while other seasons produce rain or
clear skies.

NPCs can react to the current temperature by passing the value from
`WeatherSystem.temperature` into `NPC.tick()` using the `weather_temperature`
parameter.
