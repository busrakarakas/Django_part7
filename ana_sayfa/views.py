from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import TeknoProje
from .forms import ProjeForm

# Listeleme
class ProjeListView(ListView):
    model = TeknoProje
    template_name = 'anasayfa.html'
    context_object_name = 'projeler'

# Detay
class ProjeDetailView(DetailView):
    model = TeknoProje
    template_name = 'proje_detay.html'
    context_object_name = 'proje'

# Proje Ekleme (Yeni)
class ProjeCreateView(CreateView):
    model = TeknoProje
    form_class = ProjeForm
    template_name = 'proje_ekle.html'
    success_url = reverse_lazy('anasayfa') # Başarılı olursa ana sayfaya dön