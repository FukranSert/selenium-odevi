from django.urls import path
from . import views
app_name = 'ilkapp'
urlpatterns = [
               path("home",views.home,name="home")
               
               
               ]