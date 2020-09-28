from django.db import models

class Pdf(models.Model):
    redfin_src = models.TextField(unique=True)
    pdf_src = models.TextField()
    deleted = models.BooleanField(default=False)
