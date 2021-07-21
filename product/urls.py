from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name="create"),
    path('detail/<str:id>', views.detail, name="detail"),
    path('edit/<str:id>', views.edit, name="edit"),
    path('delete/<str:id>', views.delete, name="delete"), 
    path('order/<str:id>', views.create_order, name="create_order"),
]