from django.urls import path

from AppGrupo5 import views

urlpatterns = [
    
    path('instrumentos',views.instrumentos),
    path('pedal', views.pedal),
    path('disco',views.disco),
    path('', views.inicio, name="inicio"),
]

