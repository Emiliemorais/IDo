"""ido URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import notifications.urls
import django_blog.urls
from django_blog import views as django_blog_views

from blog import views as blog_views
from manager import views as manager_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^$', blog_views.home, name='home'),
    url(r'^about/$', blog_views.about, name='about'),
    url(r'^address/$', blog_views.address, name='address'),
        
    url(r'^manager/', include('manager.urls')),
    url(r'^blog/', include('blog.urls')),

    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    url('^django_blog/', include(django_blog.urls, namespace='dp_blog')),
    url(r'^post/$', django_blog_views.PostView.as_view(), {'template_name': 'new_post.html'}, name='post'),
]
