from django.conf.urls import include, url
from django.contrib import admin
from tengApp import views

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'tengApp.views.home', name='home'),
    url(r'^projects/', 'tengApp.views.project', name='project'),
    url(r'^about/', 'tengApp.views.about', name='about'),
    url(r'^business-group/', 'tengApp.views.business_group', name='business_group'),
    url(r'^news/', views.news, name='news'),


    url(r'^admin/', include(admin.site.urls)),
]
