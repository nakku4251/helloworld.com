from . import views
from django.urls import path



urlpatterns = [
    path("",views.top),
    path("resume/",views.resume,),
]
