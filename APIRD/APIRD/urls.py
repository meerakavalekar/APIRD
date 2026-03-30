#MainAPP/urls.py 

from django.urls import path
from  drinks import views


urlpatterns = [
    path('',views.drinks),
    path('admin/', admin.site.urls),
    path('drinks/',views.drinks_list), #localhost:8000/drinks/,
    path('drinks/<int:id>/',views.drink_detail) 
    # https//:127:0:0:1:8000/drinks/1/
]
