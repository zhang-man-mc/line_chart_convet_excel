# coding:utf-8
# 模拟登陆后将cookie保存下来
import os
import re
import sys

sys.path.append(os.path.dirname(__file__))
sys.path.append("../fugitive_dust")

from request.dust_url import UrlConfig
from request.request import MyRequest


def web_login() -> bool:
    # 请求的初始化工作
    # 构建session
    # 请求头
    session = MyRequest().get_session()
    url_login = UrlConfig().url_login
    # 请求原始登陆页面
    # 获取token
    # 获取跳转的url
    # 正则表达式提取token 和url
    playload = {
        "a": "ZHp6d3B0",
        "allParams": "cC+QXA6lzRK6JXTjS+yCpCXg2UJDTgNW9viPDZ0O0tQMarNhIeFaCk8Jbsicxv7ZKLlX3J80r8ewAT12zsRsk0e3XdHIiSRrJG5bDrQtqQ8T+bazgbxAdeC3jEQDG3k5pFyPUONlyEh1OU2kwKHI8V7mp7RfZpz1DeYDoAtVFcX7bh3fzQs2wEKLjeggMj7fahAX4U3s9JfNl2DQCSGQX4q7iyKnDhf4ok8u8yuv8q3XkvP3k1/vqpZRmQ1v16/KAsKPgDXtrbBq9q8yjNaMOC2Jz1FxBundI7Sip/6J6bOUNHikbGGueW+V5Q9462Dt30IYmjVXupSnK0FfUqxuV3JcZgP6ZPTs",
    }
    r2 = session.post(url_login, data=playload, verify=False)
    if r2.status_code != 200:
        return False

    r = r2.content.decode("utf-8", errors="ignore")

    token = re.findall('name="allParams" value="(.*?)"/>', r)[0]
    url_jump = re.findall('action="..(.*?)"', r)[0]

    # 请求跳转的url
    # 构造跳转的url
    # 构造表单
    # 发生请求

    url = UrlConfig().login_url + url_jump

    playload = {
        "allParams": token,
        "a": "ZHp6d3B0",
        "needLogin": "true",
        "user.account": "zhangxiaowei",
        "user.password": "a1de872a313c7dc91cf428d5ebb5d749",
        "timestamp": "",
    }
    r1 = session.post(url, data=playload, verify=False)
    # print(r1.text)
    # 个人验证
    # 重定向测试
    if r1.status_code == 200:
        # 持久化cookie
        # ck = session.cookies.get_dict()
        ck = session.cookies
        print(ck)
        # my_cookie.cookie = ck
        return True
    else:
        return False
