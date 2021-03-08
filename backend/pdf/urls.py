from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import PdfViewSet, SearchView, RedfinView, UserAuth, UserLogin, UserPdfs, EmailView, PdfFieldsView

router = SimpleRouter()
router.register('pdf', PdfViewSet, basename='pdf_view_set')
router.register('user-auth', UserAuth, basename='user_auth_view_set')
router.register('user-login', UserLogin, basename='user_login_view_set')

urlpatterns = [
    path('search/', SearchView.as_view()),
    path('scrapper/', RedfinView.as_view()),
    path('pdf-list/', UserPdfs.as_view()),
    path('email/', EmailView.as_view()),
    path('fields/', PdfFieldsView.as_view())
] + router.urls
