from django.contrib import admin
from advertisements.models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    pass

admin.site.register(Advertisement, AdvertisementAdmin)

