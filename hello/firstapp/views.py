from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def index (request):
 #return HttpResponse ("Hello wird! это мой первый проект на Django!")
  #  return HttpResponse("<h2>Главная</h2>")
def about(request):
    return HttpResponse("<h2>о сайте</h2>")
def contact(request):
    return HttpResponse("<h2>Контакты</h2>")


def products (request, productid=1):
    output ="<h2> Продукт №{0}<h2>".format(productid)
    return HttpResponse (output)
def users (request, id, name):
    output = "<h2>Пользователь</h2><h3>id:{0}Имя:{1}</h3>".format(id, name)
    return HttpResponse(output)
from django.http import *
from django.shortcuts import render
from .forms import UserForm

def index (request):
  #  data={"age":50}
    #return render(request, "firstapp/home.html")
    #data={"header":"Передача параметра в шаюлон Django","massage":"загпужен шаблон templates/fistapp/index_app1.html"}
    #return render(request,"firstapp/index_app1.html", context=data)
   # header="Персональные данные"
   # langs=["Английский","немецкий","Испанский"]
   # user= {"name":"Максим,","age":30}
   # addr =("Втноградная",23,45)
   # data={"header": header,"langs": langs,"user": user,"address":addr}
  # return render(request,"index.html",context=data)
# return render(request,"firstapp/home.html")
    #return render(request, "firstapp/index.html",context=data)
    #cat = ["Ноутбуки", "Принтеры","Сканеры","Диски","Шнуры"]
    #cat = []
    #return render(request, "firstapp/index.html",
                 # context={"cat": cat})
    userform = UserForm()
    return render(request, "firstapp/index.html",
      {"form": userform})



