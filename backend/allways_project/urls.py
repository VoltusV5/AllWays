from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hi")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # корень сайта — функция home
]
