from django.contrib import admin
# Burada 'Proje' yerine senin modelinin gerçek adı olan 'TeknoProje' yazmalı
from .models import TeknoProje 

@admin.register(TeknoProje)
class TeknoProjeAdmin(admin.ModelAdmin):
    # Tablo sütunlarını senin modelindeki alanlara göre ayarladım
    list_display = ('baslik', 'eklenme_tarihi', 'durum') 
    
    # Sağ taraftaki filtre paneli
    list_filter = ('durum', 'eklenme_tarihi')
    
    # Arama çubuğu
    search_fields = ('baslik',)

# Admin panel başlıkları
admin.site.site_header = "Büşra'nın Yönetim Paneli"
admin.site.index_title = "Büşra'nın Web Projesi Yönetim Merkezi"