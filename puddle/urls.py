from django.contrib import admin
from django.urls import path
from core import views  # importa suas views do app

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.index, name='contact'),  # adiciona essa linha
    path('admin/', admin.site.urls),
]
