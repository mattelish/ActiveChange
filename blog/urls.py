from django.conf.urls import url 
from . import views

app_name = 'blog'

urlpatterns = [
   url(r'^$', views.blog_list, name="list"),
   url(r'^create/$', views.blog_create, name="create"),
   url(r'^(?P<slug>[\w-]+)/$', views.blog_detail, name="detail"),
]