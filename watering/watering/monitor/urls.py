from django.conf.urls import url
from monitor import views
from monitor.views import Monitor


urlpatterns=[
    url('',Monitor.as_view()),
    url('/',Monitor.as_view()),
]

