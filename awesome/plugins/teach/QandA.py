import nonebot
from awesome.plugins.teach import myDict

# 获取当前cqhttp对象
bot = nonebot.get_bot()


# 解析所有指令
@bot.on_message()
async def handle_msg(context):
    # 去除消息首尾字符串，并且用空格隔开
    s = str(context['message']).strip()
    sp = s.split(' ')

    # 如果消息空格隔开多段，检测第一段是否为delete，若否，则第二段为指令
    if len(sp) > 1:
        if sp[0][0] == '@' and myDict.md.find_k(sp[1]):
            return {'reply': myDict.md.find_k(sp[1])}
    else:
        return {'reply': myDict.md.find_k(sp[0]), 'at_sender': False}
