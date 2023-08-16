from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from tools.logger import logger_request
# Create your views here.
from .reqapp import req
from tools.resp import JsonResponse_zh
from django.views.decorators.csrf import csrf_exempt

@logger_request('replite')
def WOAcover(request: HttpRequest):
    if request.method == 'POST':
        data = request.POST
        url = data.get("url")
        print(data)
        try:
            resp = req.getcover(url)
            return JsonResponse(resp)
        except Exception as e:
            return JsonResponse({"code" : 400, 'msg' : str(e)})

@csrf_exempt
@logger_request('replite')
def gettopic(request: HttpRequest):
    if request.method=='GET':
        res = req.get_topic()
        # res = {'reason': 'success', 'result': [{'q': '你认为自己是一个', 'a': '较为有条理的人', 'b': '较为随兴所至的人', 'ia': 'dLcT', 'ib': 'x7yp'}, {'q': '当你有一份特别的任务，你会喜欢', 'a': '开始前小心组织计划', 'b': '边做边须做什么', 'ia': 'dXd5', 'ib': '7I6q'}, {'q': '下面每一对词语中，哪个词语更合你心意', 'a': '有条不紊', 'b': '不拘小节', 'ia': '6l7h', 'ib': '22K'}, {'q': '假如你是以为老师，你会选教', 'a': '以事实为主的课程', 'b': '涉及理论的课程', 'ia': 'WhX4', 'ib': 'D1C9'}, {'q': '你会跟哪些人做朋友', 'a': '常提出新主意的', 'b': '脚踏实地的', 'ia': 'QxRx', 'ib': 'rysT'}, {'q': '下面每一对词语中，哪个词语更合你心意', 'a': '合情合理', 'b': '令人着迷', 'ia': 'kejr', 'ib': 'sdrh'}, {'q': '你是否', 'a': '容易让人了解', 'b': '难于让人了解', 'ia': 'AKzF', 'ib': '2g3b'}, {'q': '与很多人一起会', 'a': '令你活力倍增', 'b': '常常令你心力交瘁', 'ia': 'ReQ9', 'ib': 'pMqH'}, {'q': '你能否滔滔不绝地与人聊天', 'a': '只限于跟你有共同兴趣的人', 'b': '几乎跟任何人', 'ia': 'bMaD', 'ib': '20V'}, {'q': '你宁愿替哪一类上司（或者老师）工作？', 'a': '天性淳良，但常常前后不一的', 'b': '言词尖锐但永远合乎逻辑的 ', 'ia': 'HoIs', 'ib': '4f5t'}, {'q': '要作决定时，你认为比较重要的是', 'a': '据事实衡量', 'b': '考虑他人的感受和意见 ', 'ia': 'TESq', 'ib': '8175'}, {'q': '哪一个答案最贴切描绘你一般的感受或行为', 'a': '公正的', 'b': ' 有关怀心', 'ia': 'ZdXZ', 'ib': 'nyoy'}], 'error_code': 0}
        return JsonResponse_zh(res)
    elif request.method=='POST':
        res = req.get_topic(request.POST['answers'])
        # res = {'reason': 'success', 'result': {'alphabet': 'ESTJ', 'vocabulary': 'Executive', 'occupation': '管理人员', 'summarize': ['管理人员（ESTJ）是具有外向、观察、思考和判断人格特征的人。他们有很强的毅力，坚决遵循自己的明智判断。它们通常充当稳定力量，能够在逆境中提供坚实的方向。'], 'desc': ['高管是传统和秩序的代表，利用他们对正确、错误和社会可接受的理解将家庭和社区团结在一起。拥有诚实、奉献和尊严的价值观，具有行政人格类型的人因其清晰的建议和指导而受到重视，他们乐于在艰难的道路上引领潮流。高管们以将人们聚集在一起而自豪，他们经常担任社区组织者的角色，努力将每个人聚集在一起，庆祝当地的珍贵活动，或捍卫将家庭和社区团结在一起的传统价值观。'], 'characteristic': [{'title': '以身作则', 'desc': ['民主社会对这种领导力的需求很高，占人口的比例不少于 11%，难怪美国的许多总统都是高管。坚信必须赢得的法治和权威，执行人员以身作则，表现出奉献精神和有目的的诚实，并且完全拒绝懒惰和作弊，尤其是在工作中。如果有人宣称艰苦的体力劳动是塑造性格的好方法，那就是高管。', '高管们了解他们的周围环境，并生活在一个清晰、可验证的事实的世界中——他们对知识的保证意味着即使面对巨大的阻力，他们也会坚持自己的原则，并推动对什么是可接受的和不可接受的事情的清晰愿景。他们的意见也不仅仅是空谈，因为高管们更愿意潜入最具挑战性的项目，改进行动计划并在此过程中整理细节，即使是最复杂的任务也看起来容易平易近人。', '然而，高管们不会独自工作，他们希望自己的可靠性和职业道德得到回报——具有这种性格类型的人会兑现他们的承诺，如果合作伙伴或下属因无能或懒惰，或者更糟糕的是不诚实而危及他们，他们会这样做毫不犹豫地表现出他们的愤怒。这可以为他们赢得不灵活的名声，这是所有 Sentinel 人物共有的特征，但这并不是因为高管们武断固执，而是因为他们真正相信这些价值观是社会运转的原因。']}, {'title': '更大的责任', 'desc': ['高管面临的主要挑战是认识到并非每个人都遵循相同的道路或以相同的方式做出贡献。真正的领导者会认识到个人以及团队的力量，并帮助将个人的想法带到桌面上。这样一来，高管们就真的掌握了所有的事实，并且能够领导对每个人都有效的方向。']}]}, 'error_code': 0}
        return JsonResponse_zh(res)