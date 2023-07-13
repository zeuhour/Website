import requests,re
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