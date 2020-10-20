from django.contrib import admin

from .models import Pdf, UserProfile, PersistentUserChoice

admin.site.register(Pdf)
admin.site.register(UserProfile)
admin.site.register(PersistentUserChoice)
