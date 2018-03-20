#coding=utf-8
import requests

headers = {'User-Agent': 'my custom user agent', 'Cookie': 'haha'}
response = requests.get('http://xueshu.baidu.com/usercenter/data/journal?cmd=journal_page&entity_id=003bf4eeb0ff997e155b192563d3a9d7',headers=headers)
response.encoding='utf-8'
print(response.text)
#FindPageDetailForZHYYGL()