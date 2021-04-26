from django.conf.urls import url
from .views import test
# from . import views

urlpatterns = [
    url(r'^', test),
    
]
