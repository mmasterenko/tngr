from django.conf.urls import include, url
from django.contrib import admin
from tengApp import views

urlpatterns = [
    url(r'^teyladmin/', include(admin.site.urls)),

    url(r'^media/(?P<path>images/.+(?:\.jpeg|\.jpg|\.png))$', views.media, name='media'),
    url(r'^media/(?P<path>files/.+(?:\.pdf|\.doc|\.docx|\.txt))$', views.media, name='media'),

    url(r'^$', 'tengApp.views.home', name='home'),
    url(r'^projects/', 'tengApp.views.project', name='project'),
    url(r'^about/', 'tengApp.views.about', name='about'),
    url(r'^business-group/', 'tengApp.views.business_group', name='business_group'),
    url(r'^news/p/(?P<page_id>[0-9]+)', views.news, name='news'),
    url(r'^news/', views.news, name='news'),
    url(r'^(?P<page_url>[^/]+)/$', views.simple_page, name='simple_page'),
]
