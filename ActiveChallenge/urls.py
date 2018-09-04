from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    #url(r'^$', 'ActiveChallenge.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.Home),
    url(r'^Home/$', views.Home),
    url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('accounts.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
