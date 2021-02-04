from . import views
from django.urls import path

app_name = "myprofile"

urlpatterns = {
    path("", views.top, name ="top"),
    path("resume/", views.resume, name ="resume"),
}
