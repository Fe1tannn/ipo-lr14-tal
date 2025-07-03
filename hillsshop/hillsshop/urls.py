from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/spec/', permanent=False)),  # Перенаправление с / на /spec/
    path('spec/', include('shop.urls')),  # Корректное подключение путей из shop.urls
    path('about/', include('shop.urls'), name='about'),  # Проверьте, нужно ли это
    path('store/', include('shop.urls'), name='store'),  # Проверьте, нужно ли это
]