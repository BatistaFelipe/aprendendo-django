from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'mysite'
urlpatterns = [
    path('', views.index, name='index'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
