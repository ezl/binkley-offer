import os

from types import SimpleNamespace
import json
from django.http import FileResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.response import Response

# from oauth2client import client
# from googleapiclient.discovery import build

from .exceptions.custom_exceptions import RedfinScrapperException, UnhandledException, InvalidPropertyType, \
    InvalidPassword
from .serializers import CreatePdfSerializer, GetPdfSerializer, SearchSerializer, RedfinScrapperSerializer, \
    GoogleAuthSerializer, CreateUserSerializer, ResponseUserSerializer, LoginUserSerializer, \
    SendEmailSerializer, PdfFieldsSerializer
from .models import Pdf, PdfFields
from .services.email_service import send_email
from .services.pdf_fields import build_pdf_fields

from .services.search_service import search_redfin_autocomplete_api
from .services.pdf_service import scraper_redfin
from .services.auth_service import *
from .services.utils import *
from rest_framework import status


class PdfViewSet(ViewSet):
    serializer_class = CreatePdfSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def create(self, request):

        serializer = CreatePdfSerializer(data=request.data)

        if not serializer.is_valid():
            raise ParseError(detail=serializer.errors)

        try:
            pdf = serializer.save()
            build_pdf_fields(SimpleNamespace(**request.data), pdf.id)
        except InvalidPropertyType as invalid_property_type:
            raise invalid_property_type

        pdf_src = pdf.pdf_src

        if not os.path.exists(pdf_src):
            raise NotFound(detail='PDF not found')

        if request.auth:
            user = User.objects.get(
                id=Token.objects.get(key=request.auth.key).user_id)
            pdf.user_email = user.username
            pdf.save()
        get_pdf_serializer = GetPdfSerializer(Pdf.objects.filter(id=pdf.id, deleted=False).first())
        return Response(get_pdf_serializer.data,)

    def list(self, request):
        pdf_id = request.GET.get('id')
        pdf = Pdf.objects.filter(id=pdf_id, deleted=False).first()

        if not pdf:
            raise NotFound(detail='PDF not found')

        serializer = GetPdfSerializer(pdf)

        return FileResponse(open(serializer.data['pdf_src'], 'rb'))

    def destroy(self, request, pk=None):
        pdf = Pdf.objects.filter(pk=pk, deleted=False).first()

        if not pdf:
            raise NotFound(detail='PDF not found')

        pdf.deleted = True
        pdf.save()

        serializer = GetPdfSerializer(pdf)

        return Response(serializer.data)


class EmailView(APIView):
    serializer_class = SendEmailSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = SendEmailSerializer(data=request.data)

        if not serializer.is_valid():
            raise ParseError(detail=serializer.errors)

        send_email(serializer.validated_data['send_to'], "Dummy Title", serializer.validated_data['pdf_id'])
        return Response({"status": "sent"})


class PdfFieldsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        pdf_id = request.GET.get("id")
        pdf_fields = PdfFields.objects.filter(pdf_id=int(pdf_id)).first()

        if not pdf_fields:
            raise NotFound(detail="PDF not found")

        serializer = PdfFieldsSerializer(pdf_fields)

        return Response(serializer.data)


class SearchView(APIView):
    serializer_class = SearchSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = SearchSerializer(data=request.data)

        if not serializer.is_valid():
            raise ParseError(detail=serializer.errors)

        url = serializer.validated_data['url']

        search = search_redfin_autocomplete_api(url)

        if search:
            return Response(search)
        return Response({'properties': []})


class RedfinView(APIView):
    serializer_class = RedfinScrapperSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RedfinScrapperSerializer(data=request.data)

        if not serializer.is_valid():
            raise ParseError(detail=serializer.errors)

        try:
            url = serializer.validated_data['url']
            scrapper_redfin_details = scraper_redfin(url)
            if scrapper_redfin_details:
                return Response(scrapper_redfin_details)
        except Exception:
            raise RedfinScrapperException()


# class GoogleAuthViewSet(ViewSet):
#     serializer_class = GoogleAuthSerializer
#
#     CLIENT_ID = '783671048395-hblgld7toqqnrciqi477gje5snggtjka.apps.googleusercontent.com'
#
#     CLIENT_SECRET = 'Aq0Lk6xzzKes__d_WLDUuT2z'
#
#     def create(self, request):
#         serializer = GoogleAuthSerializer(data=request.data)
#
#         if not serializer.is_valid():
#             raise ParseError(detail=serializer.errors)
#
#         credentials = client.credentials_from_code(self.CLIENT_ID, self.CLIENT_SECRET,
#                                                    scope=['https://www.googleapis.com/auth/gmail.labels',
#                                                           'https://www.googleapis.com/auth/gmail.readonly',
#                                                           'https://www.googleapis.com/auth/gmail.modify'],
#                                                    code=serializer.validated_data['code'],
#                                                    redirect_uri=serializer.validated_data['redirect_uri'])
#
#         service = build('gmail', 'v1', credentials=credentials)
#         print(service.users().labels().list(userId='me').execute())
#         return Response("a mers")


class UserAuth(ViewSet):
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = CreateUserSerializer(data=request.data)

        if not serializer.is_valid():
            raise ParseError(detail=serializer.errors)

        if not password_checker(serializer.validated_data['password']):
            raise InvalidPassword()
        try:
            serializer_response = ResponseUserSerializer(
                data=create_user(serializer.validated_data))
            serializer_response.is_valid()
            print(serializer_response.errors)
            if not serializer_response.is_valid():
                raise ParseError(detail=serializer_response.errors)

            return Response(serializer_response.data)
        except RedfinScrapperException as duplicate_error:
            raise duplicate_error
        except UnhandledException:
            raise UnhandledException(detail="Unhandled Exception", code=500)

    def list(self, request):
        user_uid = request.GET.get('user_uid')
        user = UserProfile.objects.filter(user_uid=user_uid).first()

        if not user:
            raise NotFound(detail='User not found')

        serializer = ResponseUserSerializer(user)

        return Response(serializer.data)


class UserLogin(ViewSet):
    serializer_class = LoginUserSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = LoginUserSerializer(data=request.data)

        if not serializer.is_valid():
            raise ParseError(detail=serializer.errors)
        try:
            serializer_response = ResponseUserSerializer(
                data=login_user(serializer.validated_data))
            if not serializer_response.is_valid():
                raise ParseError(detail=serializer_response.errors)

            return Response(serializer_response.data)
        except NotFound as not_found:
            raise not_found
        except UnhandledException:
            raise UnhandledException(detail="Unhandled Exception", code=500)


class UserPdfs(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        user = User.objects.get(
            id=Token.objects.get(key=request.auth.key).user_id)
        pdfs = Pdf.objects.filter(user_email=user.username)
        serializer_response = GetPdfSerializer(pdfs, many=True)
        return Response({'pdfs': serializer_response.data})

# class UserPreferences(ViewSet):
#     authentication_classes = (TokenAuthentication,)
#
#     def create(self, request):
#         serializer = UserPreferencesSerializer(data=request.data)
#
#         if not serializer.is_valid():
#             raise ParseError(detail=serializer.errors)
#         create_user_persistent_choices(serializer.validated_data, User.objects.get(
#             id=Token.objects.get(key=request.auth.key).user_id))
#
#         return Response(status=status.HTTP_201_CREATED)
#
#     def list(self, request):
#
#         user_preferences = PersistentUserChoice.objects.filter(user=User.objects.get(
#             id=Token.objects.get(key=request.auth.key).user_id)).first()
#
#         if not user_preferences:
#             raise NotFound(detail='User Preferences not found')
#
#         serializer = UserPreferencesSerializer(user_preferences)
#
#         return Response(serializer.data)
