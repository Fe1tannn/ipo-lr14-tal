from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.spec_list, name='spec_list'),  # Убрано /spec/, так как это уже в hillsshop/urls.py
    path('<int:id>/', views.spec_detail, name='spec_detail'),  # Убрано /spec/
]