from django.contrib import admin

from .models import Pdf, UserProfile, PdfFields

admin.site.register(Pdf)
admin.site.register(UserProfile)
admin.site.register(PdfFields)
# admin.site.register(PersistentUserChoice)
