import requests
import json

url = 'https://oapi.dingtalk.com/robot/send?access_token=8bb1803cefd8b2409bfaf7786b626c2b168bbc1f6624ca9283e228bbdd58f1f5'
headers = {'Content-Type': 'application/json; charset=UTF-8'}
# data = {
#     "msgtype": "text",
#     "text": {
#         "content": "sb 好好学习天天向上"
#     },
#     "at": {
#         "atMobiles": [
#             #"156xxxx8827",
#             #"189xxxx8325"
#         ],
#         "isAtAll": False
#     }
# }
data = {
    "msgtype": "markdown",
    "markdown": {
        "title":"Offer",
        "text": """看美女!!!
看链接:[meimei](https://pic.sogou.com/)![screenshot](https://img03.sogoucdn.com/app/a/100520020/26318d2e544620e7099f836a2fc29943)
好好学习天天向上"""
    },
    "at": {
        "atMobiles": [
            #"150XXXXXXXX"
        ],
        "isAtAll": False
        }
    }
r = requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())