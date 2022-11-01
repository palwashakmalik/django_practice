from django.urls import path
from . import views
urlpatterns = [
  path('', views.myfunctioncall, name = "index"),
  path('about', views.myfunctionabout, name="about"),
  path('add/<int:a>/<int:b>',views.add, name ="add"),
  path('intro/<str:name>/<str:age>',views.intro, name= "intro"),
  path('mysecondpage',views.mysecondpage, name= "mysecondpage"),
  path('mythirdpage',views.mythirdpage,name='mythirdpage'),
  path('articlelist',views.article_list,name='articlelistpage'),
]

