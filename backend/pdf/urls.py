from django.urls import path

from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt import views as jwt_views

from .views import PdfViewSet, SearchView, RedfinView, UserAuth, UserLogin, UserPdfs

router = SimpleRouter()
router.register('pdf', PdfViewSet, basename='pdf_view_set')
# router.register('google-auth', GoogleAuthViewSet, basename="google_auth_view_set")
router.register('user-auth', UserAuth, basename='user_auth_view_set')
router.register('user-login', UserLogin, basename='user_login_view_set')

urlpatterns = [
    path('search/', SearchView.as_view()),
    path('scrapper/', RedfinView.as_view()),
    path('pdf-list/', UserPdfs.as_view()),
] + router.urls
