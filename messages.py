from coordinates import get_coordinates
from api_service import get_weather

from ban_words import lst_ban_words
def help() -> str:
    help_msg = \
          (f"На данный момент доступно:\n" \
           f"/weather - Погода \n\n" \
           f"Работает Анти-флуд команд!!!")
    return help_msg

def weather() -> str:
    """Returns a message about the temperature and weather description"""
    wthr = get_weather(get_coordinates())
    description_id = wthr.id
    lst_id_description = [
           ["800"], #clear sky
           ["801"], #few clouds
           ["802", "803", "804"], #scattered and broken clouds
           ["300", "301", "302", "310", "311", "312", "313", "314", "321", "520", "521", "522", "531"], #shower rain
           ["500", "501", "502", "503", "504"], #rain
           ["200", "201", "202", "210", "211", "212", "221", "230", "231", "232"], #thunderstorm
           ["511", "600", "601", "602", "611", "612", "613", "615", "616", "620", "621", "622"], #snow
           ["701", "711", "721", "731", "741", "751", "761", "762", "771", "781"]] #mist
    list_emoji_index = ["{}".format(index1) for index1,value1 in enumerate(lst_id_description) for index2,value2 in enumerate(value1) if value2==description_id]
    emoji_index_weather = list_emoji_index[0]
    emoji_weather_description = ''
    lst_temperature = [[float('-inf'), -20], [-20, -5], [-5, 5], [5, 20], [20, float('inf')]]
    emoji_temperature = ''
    emoji_index_temperature = 0
    for arr in lst_temperature:
        if arr[0] <= wthr.temperature <= arr[1]:
            break
        emoji_index_temperature += 1

    match emoji_index_temperature:
        case 0:
            emoji_temperature = ' 🥶'
        case 1:
            emoji_temperature = ' 😕'
        case 2:
            emoji_temperature = ' 🙂'
        case 3:
            emoji_temperature = ' 😁'
        case 4:
            emoji_temperature = ' 🥵'

    match emoji_index_weather:
        case "0":
            emoji_weather_description = ' ☀'
        case "1":
            emoji_weather_description = ' ⛅'
        case "2":
            emoji_weather_description = ' ☁'
        case "3":
            emoji_weather_description = ' 🌧'
        case "4":
            emoji_weather_description = ' 🌦'
        case "5":
            emoji_weather_description = ' 🌩'
        case "6":
            emoji_weather_description = ' ❄'
        case "7":
            emoji_weather_description = ' 🌫'
    weather_msg = \
          (f'{wthr.location}, {wthr.description + emoji_weather_description}\n' \
           f'Температура: {round(wthr.temperature)}°C   ({round(wthr.temperature_feeling)}°C) {emoji_temperature}\n' \
           f'Скорость ветра: {wthr.wind_speed} м/с 💨')
    # weather_msg_translation = translator.translate(str(weather_msg), src='en', dest='ru')
    return weather_msg

