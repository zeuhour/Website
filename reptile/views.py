from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
import requests
# Create your views here.
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .reqapp import req

@csrf_exempt
def WOAcover(request: HttpRequest):
    if request.method == 'POST':
        data = request.POST
        url = data.get("url")
        print(url)
        try:
            resp = req.getcover(url)
            return JsonResponse(resp)
        except Exception as e:
            return JsonResponse({"code" : 400, 'errmsg' : str(e)})
