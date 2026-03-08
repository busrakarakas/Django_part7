# ana_sayfa/forms.py
from django import forms
from .models import TeknoProje

class ProjeForm(forms.ModelForm):
    class Meta:
        model = TeknoProje
        fields = ['baslik', 'detay', 'durum'] # Hangi alanların görüneceğini seçiyoruz