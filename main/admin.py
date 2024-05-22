from django.contrib import admin

from main.models import AboutModel


# Register your models here.
@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    exclude = ['id']
