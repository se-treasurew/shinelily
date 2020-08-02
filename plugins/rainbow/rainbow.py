from nonebot import on_command, CommandSession

import requests


# 接收rainbow指令，别名为夸我，不需要at
@on_command('rainbow', aliases=('夸我', '土味情话'), only_to_me=False)
async def rainbow(session: CommandSession):
    """
    发送rainbow字符串
    :param session: CommandSession类型的会话
    :return: None
    """
    rainbow_str = await get_rainbow()
    await session.send(rainbow_str)


async def get_rainbow() -> str:
    """
    返回调用api后的rainbow
    :return:
    """
    url = 'https://chp.shadiao.app/api.php?level='
    level = 511
    r = requests.get(url + str(level)).text
    return r
