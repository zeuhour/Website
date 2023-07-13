from django.http import JsonResponse

def JsonResponse_zh(Json: dict):
    #JSON序列化添加json_dumps_params={'ensure_ascii':False}参数以正确显示中文
    return JsonResponse(Json, json_dumps_params={'ensure_ascii':False}) 