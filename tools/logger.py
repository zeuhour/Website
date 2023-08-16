import time,logging,os,datetime,traceback
from functools import wraps
from django.http import HttpRequest, JsonResponse
import re

path = './logs'

class Logger:
    def __init__(self):
        self.format = logging.Formatter('%(asctime)s-%(levelname)s: %(message)s')
        # self.stream_handler = logging.StreamHandler()
        # self.stream_handler.setLevel(logging.DEBUG)
        # self.stream_handler.setFormatter(self.format)
        if not os.path.exists(path):
            os.mkdir(path)
        

    def getlog(self, filename):
        filename = f"{filename}-{datetime.date.today()}"
        _log = logging.getLogger(filename)
        if _log.hasHandlers():
            return _log
        else:
            _log.setLevel('DEBUG')
            self.file_handler = logging.FileHandler(
                filename=f"{path}/{filename}.log", mode='a')
            self.file_handler.setLevel(logging.DEBUG)
            self.file_handler.setFormatter(self.format)
            _log.addHandler(self.file_handler)
            #_log.addHandler(self.stream_handler)
            return _log


def logger_request(fname):
    _log = Logger().getlog(fname)
    def out_log(func):
        @wraps(func)
        def infunc(request: HttpRequest):
            res = func(request)             
            _log.info(f"源IP: {request.META.get('HTTP_X_FORWARDED_FOR') if 'HTTP_X_FORWARDED_FOR' in request.META else request.META.get('REMOTE_ADDR')}\t"\
                      f"路径: {request.get_full_path()}\t"\
                      f"参数: {request.method} {getattr(request, request.method)}\t"\
                      f"返回：{res.content if hasattr(res, 'content') else None}"
                      )                   
            return res
        return infunc
    return out_log

def logger_func(fname):
    _log = Logger().getlog(fname)
    def out_log(func):
        @wraps(func)
        def inner(*args, **kwargs):
            t_start = time.time()
            try:
                res = func(*args, **kwargs)
                t_end = time.time()
                _log.debug(f"执行完成: {func.__name__} 调用参数: {args if len(args) > 0 else 'None'} {kwargs if len(kwargs) > 0 else 'None'} 返回值: {res} 执行耗时: {t_end-t_start} 秒")
                return res
            except Exception as e:
                _log.error(f"执行异常: {func.__name__} 调用参数: {args if len(args) > 0 else 'None'} {kwargs if len(kwargs) > 0 else 'None'} 异常信息: {e}"
                           f"\n{traceback.format_exc()}")
        return inner
    return out_log