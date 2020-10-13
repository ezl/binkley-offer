from django.contrib import admin

from .models import Pdf, UserProfile, Token

admin.site.register(Pdf)
admin.site.register(UserProfile)
admin.site.register(Token)
