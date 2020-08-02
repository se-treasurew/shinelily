from os import path

import nonebot
from config import nonebot_config

if __name__ == '__main__':
    # 读取配置文件并初始化
    nonebot.init(nonebot_config)

    # 加载rainbow插件
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'awesome', 'plugins', 'rainbow'),
        'awesome.plugins.rainbow',
    )

    # 加载weather插件
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'awesome', 'plugins', 'weather'),
        'awesome.plugins.weather',
    )

    # 加载repeater插件
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'awesome', 'plugins', 'repeater'),
        'awesome.plugins.repeater',
    )

    # 加载teach插件
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'awesome', 'plugins', 'teach'),
        'awesome.plugins.teach',
    )

    # 加载greet插件
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'awesome', 'plugins', 'greet'),
        'awesome.plugins.greet',
    )

    # 运行bot
    nonebot.run()
