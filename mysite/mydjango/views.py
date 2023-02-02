from django.shortcuts import render
from mydjango.models import Item

# Create your views here.
from django.http import HttpResponse

# 클라이언트의 요청을 처리하는 함수
# 이 함수의 매개변수는 HttpRequest 타입인데
# 이 타입은 클라이언트의 정보를 가진 클래스

def index(request):
    # 클라이언트에게 문자열 응답을 전송
    #return HttpResponse("Hello Django");

    #msg = 'use first Template Engine'
    # template 디렉토리에 있는 index.html 파일로 출력하는데
    # 데이터를 message 라는 이름으로 전달
    # request 와 함께 전달해서 화면을 만드는 것을 forwarding 이라고 한다

    success = False
    name = "lee"
    data = Item.objects.all()
    print(data)
    ar = ["Developer","Operator","DevOps","MLOps"]
    return  render(request, 'index.html',{"data":data})

def detail(request,itemid):
    # itemid를 가진 데이터 찾아옴
    item = Item.objects.get(itemid=itemid)
    print(item)
    return render(request,'detail.html',{'item':item})

