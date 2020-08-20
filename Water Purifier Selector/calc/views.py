from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
from django.contrib.auth import authenticate


quality = 0
bacteria = 0
electricity = 0
budget = 0

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
# def index(request):
#     dests = Destination.objects.all()
    # return render(request,"index.html",{'dests':dests}) #Fetch the data from database
def home(request):
    return render(request,"home.html")

# # def add(request):

# #     val2 = int(request.POST['num2']) #Double quotes mei na krna yeh
# #     res = val1 + val2
# #     return render(request, 'result.html',{'result':res})
#     #JSON FORMAT
def next(request):
    return render(request,'q1.html')
def q2(request):
    global quality
    quality = request.POST.get("quality")
    return render(request,'q2.html')
def q3(request):
    global bacteria
    bacteria = request.POST.get("bacteria")
    return render(request,'q3.html')
def q4(request):
    global electricity
    electricity = request.POST.get("electricity")
    return render(request,'q4.html')
def q5(request):
    global budget
    budget = request.POST.get("budget")
    return render(request,'q5.html')
def result(request):
    ans = Destination.objects.filter(quality=quality).filter(bacteria=bacteria).filter(electricity = electricity).filter(budget=budget)
    # .get(bacteria = bacteria).get(electricity = electricity).get(budget = budget)
    # num = list(num)
    answer = ans.values('purifier')
    num = ans.values('id')
    num = list(num)
    num = dict(num[0])
    num = int(num.get("id"))
    answer = list(answer)
    answer_1,answer_2 = str(answer).split(":")
    answer,answer_2 = answer_2.split("}")
    image = Destination.objects.get(id=num)
    water = int(request.POST['members'])
    water = water*2

    # user = authenticate(quality= quality, bacteria = bacteria, electricity = electricity, budget = budget)

    # members = int(request.POST.get("members"))
    # water = 2*members

    # for key in answer:
    #     for value in answer:
    #         result = value
    # ,{'img':image}
    # 'image':image

    return render(request,'result.html',{'result':answer,'image':image,'water':water})
def darcy(request):
    return render(request,'darcy.html')
#Now , a template so http response nhi use krenge
# Create your views here.
