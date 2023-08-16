import requests,re,json
from tools.logger import logger_func

@logger_func('reqapp')
def getcover(url) -> dict:
    try:
        htm = requests.get(url)
        res = re.findall(r"var cdn_url_1_1 = \"(.+?)\";", htm.text)
        url = {}
        if res:
            url['url1'] = res[0]
        else:
            url['url1'] = None

        res = re.findall(r"msg_cdn_url = \"(.+?)\";", htm.text)
        if res:
            url['url'] = res[0]
        else:
            url['url'] = None
        return url
    except Exception as e:
        return {'err':e, 'code':4000}
    
@logger_func('reqapp')
def get_topic(answers:str = None):
    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded'
    }
    if answers is not None:
        url = 'http://apis.juhe.cn/fapig/character_test/analysis?key=cde6486f875b4d4febae24cf1c7ea0bc&answers='+answers
        return json.loads(requests.get(url=url, headers=headers).content)
    else:
        url = 'http://apis.juhe.cn/fapig/character_test/questions?key=cde6486f875b4d4febae24cf1c7ea0bc&level=senior'
        # paload = dict(key='cde6486f875b4d4febae24cf1c7ea0bc', level='senior')

        return json.loads(requests.get(url=url, headers=headers).content)