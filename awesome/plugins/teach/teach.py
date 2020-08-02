from nonebot import on_command, CommandSession

from awesome.plugins.teach import myDict


# teach关键词，不用at


@on_command('teach', only_to_me=False)
async def teach(session: CommandSession):
    q = session.get('q', prompt='你想教我的问题是什么呢？')
    a = session.get('a', prompt='答案是什么呢？')

    # 添加并保存新的键值对
    msg = myDict.md.add_kv(q, a)
    await session.send(msg)


# delete关键词，不用at
@on_command('delete', only_to_me=False)
async def delete(session: CommandSession):
    q = session.get('q', prompt='你想要删除什么呢？')

    # 删除并保存现有键值对
    msg = myDict.md.delete_k(q)
    await session.send(msg)


# delete参数解析器
@delete.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['q'] = stripped_arg.split()[0]
        return

    if not stripped_arg:
        session.pause('要忘记什么呢？')

    session.state[session.current_key] = stripped_arg


# teach参数解析器
@teach.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg.strip()

    if session.is_first_run:
        if stripped_arg:
            sa = stripped_arg.split()
            if len(sa) > 1:
                session.state['q'] = sa[0]
                session.state['a'] = sa[1]
            else:
                session.state['q'] = sa[0]
                session.pause('答案是什么呢？')
        return

    if not stripped_arg:
        session.pause('要教我什么呢？')

    session.state[session.current_key] = stripped_arg


