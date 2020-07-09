from django.conf.urls import url
from monitor import views
from monitor.views import Monitor


urlpatterns=[
    url(r'',Monitor.as_view()),
]

