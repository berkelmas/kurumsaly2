from django.contrib import admin
from .models import Contact, Makaleler

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['iletisim_adsoyad', 'iletisim_tarihi']



@admin.register(Makaleler)
class MakaleAdmin(admin.ModelAdmin):
    exclude = ('makale_slug',)