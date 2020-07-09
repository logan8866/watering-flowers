from django.conf.urls import url
from datarecord import views
from datarecord.views import Datarecord

urlpatterns=[

    url(r'',Datarecord.as_view()),

]

