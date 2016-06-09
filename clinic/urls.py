from django.conf.urls import url
from . import views
app_name = 'clinic'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/patdetails/$', views.patdetails, name='patdetails'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^delete/$', views.deleted, name='deleted'),
    url(r'^add/$', views.add, name='add'),
]