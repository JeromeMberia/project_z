from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_items),
    path('add/', views.create_item),
    path('<int:pk>/delete', views.delete_item),
    path('<int:pk>/update', views.update_item_detail),
    path('<int:pk>/', views.get_item_detail),
]