from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api/timestamp/', views.EmptyDateTimeStampApi),
    path('api/timestamp/<slug:date_string>', views.TimeStampApi)
]
