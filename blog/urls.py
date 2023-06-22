
from django.urls import path               
from . import views                          # for views of app

app_name= 'blog'
urlpatterns = [
    
    path('',views.all_blogs,name='all_blogs'),
    path('<int:blog_id>/',views.detail,name='detail'),              #get the blog id for detail displaying n single page
    
]