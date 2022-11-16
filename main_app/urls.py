from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('hamsters/', views.hamster_index, name='index'),
  path('hamsters/<int:hamster_id>/', views.hamsters_detail, name='detail'),
  path('hamsters/create/', views.HamsterCreate.as_view(), name='hamsters_create'),
]