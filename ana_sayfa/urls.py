from django.urls import path
from .views import ProjeListView, ProjeDetailView, ProjeCreateView

urlpatterns = [
    path('', ProjeListView.as_view(), name='anasayfa'),
    path('proje/<int:pk>/', ProjeDetailView.as_view(), name='proje_detay'),
    path('yeni/', ProjeCreateView.as_view(), name='proje_ekle'),
]