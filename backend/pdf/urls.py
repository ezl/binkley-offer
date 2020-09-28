from rest_framework.routers import SimpleRouter 
from .views import PdfViewSet

router = SimpleRouter()
router.register('', PdfViewSet, basename='pdf_view_set')

urlpatterns = router.urls
