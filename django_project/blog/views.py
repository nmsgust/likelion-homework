from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html') 
    #페이지 하나에 뷰 함수 하나. def 나 파일 만들었으니 이파일 읽어줘, 사용자에게 보여줘 
