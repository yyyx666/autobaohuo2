# encoding: utf-8
import os

import requests

# 示例调用
if __name__ == "__main__":
    url = os.environ.get("URL")
    resp = requests.request("get", url)

    if resp.status_code == 200:
        print("状态正常")
    else:
        raise Exception("状态异常：" + str(resp.status_code))


