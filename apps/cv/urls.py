from django.urls import path
from . import views

app_name = 'cv'

urlpatterns = [
    path('', views.CVView.as_view(), name='cv'),
]
