from django.urls import path

from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt import views as jwt_views

from .views import PdfViewSet, SearchView, RedfinView, GoogleAuthViewSet, UserAuth, UserLogin, Test

router = SimpleRouter()
router.register('pdf', PdfViewSet, basename='pdf_view_set')
router.register('google-auth', GoogleAuthViewSet, basename="google_auth_view_set")
router.register('user-auth', UserAuth, basename='user_auth_view_set')
router.register('user-login', UserLogin, basename='user_login_view_set')

urlpatterns = [
    path('search/', SearchView.as_view()),
    path('scrapper/', RedfinView.as_view()),
    path('hello/', Test.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
] + router.urls
