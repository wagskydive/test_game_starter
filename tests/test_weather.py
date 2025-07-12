from src.weather import WeatherSystem, Season, Weather


def test_season_cycles_every_30_days():
    w = WeatherSystem()
    for _ in range(30):
        w.advance_day(seed=0)
    assert w.season == Season.SUMMER


def test_temperature_follows_season_and_weather():
    w = WeatherSystem(season=Season.WINTER)
    w.advance_day(seed=1)
    assert w.weather == Weather.SNOW
    assert w.temperature == -5  # base 0 -5 for snow
