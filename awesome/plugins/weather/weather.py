from nonebot import on_command, CommandSession

import requests
import json


# on_command修饰器用于匹配weather命令，aliases是别名，不用at
@on_command('weather', aliases=('天气', '天气预报', '查天气'), only_to_me=False)
async def weather(session: CommandSession):
    city = session.get('city', prompt='你想查询哪个城市的天气呢？')
    weather_report = await get_weather_of_city(city)
    await session.send(weather_report)


# weather函数参数解析器
@weather.args_parser
async def _(session: CommandSession):

    # 去除首尾空白
    stripped_arg = session.current_arg_text.strip()

    # 若为第一次调用，且参数不为空，那么city值为参数
    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg
        return

    # 若参数为空
    if not stripped_arg:
        session.pause('要查询的城市名称不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg


async def get_weather_of_city(city: str) -> str:
    """
    调用接口，获取城市location id
    再调用接口，获取城市天气
    :param city: 城市名称
    :return: 格式化后的天气数据
    """
    key = '2cecc953c7ae467081524bc64256e957'
    # 获取地理位置id
    weather_id_find_url = 'https://geoapi.heweather.net/v2/city/lookup?'
    para_id = {'location': city, 'key': key}
    r = requests.get(weather_id_find_url, params=para_id).text
    j = json.loads(r)
    location_id = j['location'][0]['id']

    # 获取城市天气预报
    weather_find_url = 'https://devapi.heweather.net/v7/weather/3d'
    para_find = {'location': location_id, 'key': key}
    r = requests.get(weather_find_url, params=para_find)
    r = r.text
    info = json.loads(r)
    ret = ""

    for i in range(3):
        j = info['daily'][i]

        fx_date = j['fxDate']
        temp_max = j['tempMax']
        temp_min = j['tempMin']
        text_day = j['textDay']
        text_night = j['textNight']
        wind_dir_day = j['windDirDay']
        wind_scale_day = j['windScaleDay']
        wind_dir_night = j['windDirNight']
        wind_scale_night = j['windScaleNight']
        humidity = j['humidity']
        pressure = j['pressure']
        ret += f'''{fx_date}:
                {city}温度{temp_min}-{temp_max}℃
                湿度{humidity}%
                气压{pressure}Mpa
                白天{text_day}，{wind_dir_day}{wind_scale_day}级
                夜晚{text_night}，{wind_dir_night}{wind_scale_night}级\n'''

    return ret

