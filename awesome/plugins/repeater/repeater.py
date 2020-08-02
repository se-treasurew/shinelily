import nonebot
from mycontext.mycontext import md


# 获取当前cqhttp对象
bot = nonebot.get_bot()


# 解析所有指令
@bot.on_message('group')
async def handle_msg(context):
    # 去除消息首尾字符串，并且用空格隔开
    s = str(context['message']).strip()
    print(s)
    if len(md.msg) > 0 and s == md.msg[-1] and s != md.last_msg:
        md.last_msg = s
        print('y')
        print(md)
        return {'reply': s, 'at_sender': False}
    else:
        md.msg.append(s)


