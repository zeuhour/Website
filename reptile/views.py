from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from tools.logger import logger_request
# Create your views here.
from .reqapp import req

@logger_request('replite')
def WOAcover(request: HttpRequest):
    if request.method == 'POST':
        data = request.POST
        url = data.get("url")
        print(url)
        try:
            resp = req.getcover(url)
            return JsonResponse(resp)
        except Exception as e:
            return JsonResponse({"code" : 400, 'msg' : str(e)})
