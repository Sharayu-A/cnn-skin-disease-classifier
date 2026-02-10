from django.urls import path
from .views import home, single_upload, batch_upload

urlpatterns = [
    path("", home, name="home"),
    path("single/", single_upload, name="single"),
    path("batch/", batch_upload, name="batch"),
]
