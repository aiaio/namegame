from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView, RedirectView
from rest_framework import routers

from names import views

router = routers.DefaultRouter()
router.register(r'names', views.NameViewSet)
#router.register(r'random', views.RandomNameViewSet.as_view()

urlpatterns = patterns('',
    url(r'^$', views.NameCreate.as_view(), name='home'),
    url(r'^play/$', views.NameDetail.as_view(), name='play'),
    url(r'^ready/$', views.Ready.as_view(), name='ready'),
    url(r'^api/', include(router.urls)),
    url(r'^api/(?P<pk>.*?)/', views.RandomNameView.as_view(), name='random'),
)
