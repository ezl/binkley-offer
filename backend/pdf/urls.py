from django.urls import path

from rest_framework.routers import SimpleRouter 

from .views import PdfViewSet, SearchView, RedfinView

router = SimpleRouter()
router.register('pdf', PdfViewSet, basename='pdf_view_set')

urlpatterns = [
    path('search/', SearchView.as_view()),
    path('scrapper/', RedfinView.as_view())
] + router.urls
