from django.urls import path
from . import views     #  Located in the same file structure. This is a mass import
#  Base folder is app folder.  mysite is proj folder


urlpatterns = [
    path('', views.taskList, name='tasks')
]
