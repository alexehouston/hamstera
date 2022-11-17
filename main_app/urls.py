from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('hamsters/', views.hamster_index, name='index'),
  path('hamsters/<int:hamster_id>/', views.hamsters_detail, name='detail'),
  path('hamsters/create/', views.HamsterCreate.as_view(), name='hamsters_create'),
  path('hamsters/<int:pk>/update/', views.HamsterUpdate.as_view(), name='hamsters_update'),
  path('hamsters/<int:pk>/delete/', views.HamsterDelete.as_view(), name='hamsters_delete'),
  path('cats/<int:hamster_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]