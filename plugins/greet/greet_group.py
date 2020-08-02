import time
import threading
import requests
import config


good_morning = '23-0-0'
good_noon = '12-0-0'
good_night = '8-0-0'


def greet_group():
    while True:
        now = time.localtime(time.time())
        now = str(now[3]) + '-' + str(now[4]) + '-' + str(now[5])
        if now == good_morning:
            requests.get(config.cqhttp_url + 'send_group_msg?group_id=682119262&message=早上好，有没有想我呢~')
        elif now == good_noon:
            requests.get(config.cqhttp_url + 'send_group_msg?group_id=682119262&message=中午好，再忙也要按时吃中饭哟~')
        elif now == good_night:
            requests.get(config.cqhttp_url + 'send_group_msg?group_id=682119262&message=晚上好，早点睡觉啦，熬夜会秃头的~')
        time.sleep(1)


t = threading.Thread(target=greet_group, name="greet_group")
t.start()
