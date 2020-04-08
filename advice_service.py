from weather_service import WeatherInfo


temperature_rules = [
    (-10, 'Очень холодно. Одевайте все самое теплое.'),
    (0, 'Холодно, стоит взять теплую куртку и шарф.'),
    (10, 'Прохладно, стоит одеться потеплее.'),
    (15, 'Приятная погода, но куртка не помешает.'),
    (20, 'Тепло. Легкая кофта подойдет.'),
    (27, 'Очень тепло. Футболка и шорты - то, что нужно.'),
    (50, 'Очень жарко, держитесь в тени и возьмите с собой воды.'),
    (5000, 'Скорее всего, вы на солнце.')
]


def get_temperature_advice(temperature: int) -> str:
    for rule, advice in temperature_rules:
        if temperature < rule:
            return advice

    return ''


def get_status_advice(weather: str) -> str:
    if 'дожд' in weather:
        return 'Возьмите зонтик.'
    return ''


def get_advice(weather: WeatherInfo) -> str:
    advice = get_temperature_advice(weather.temperature)
    advice += '\n'
    advice += get_status_advice(weather.status)
    return advice
