from django.conf.urls import url, include
from . import views

app_name = 'detection'

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^updateProfile/$', views.updateProfile, name='updateProfile'),
    url(r'^scratchDetection/$', views.scratchDetection, name='scratchDetection'),
    url(r'^claimInfo/(?P<claim_id>[0-9a-z]+)/$', views.claimInfo, name='claimInfo'),
]