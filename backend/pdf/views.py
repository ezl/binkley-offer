import os

from types import SimpleNamespace

from django.http import FileResponse

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.response import Response

from oauth2client import client
from googleapiclient.discovery import build

from .exceptions.custom_exceptions import RedfinScrapper
from .serializers import CreatePdfSerializer, GetPdfSerializer, SearchSerializer, RedfinScrapperSerializer, \
    GoogleAuthSerializer
from .models import Pdf

from .services.search_service import search_redfin_autocomplete_api
from .services.pdf_service import scraper_redfin


class PdfViewSet(ViewSet):
    serializer_class = CreatePdfSerializer

    def create(self, request):

        serializer = CreatePdfSerializer(data=request.data)

        if not serializer.is_valid():
            raise ParseError(detail=serializer.errors)

        pdf = serializer.save()
        pdf_src = pdf.pdf_src

        if not os.path.exists(pdf_src):
            raise NotFound(detail='PDF not found')

        return FileResponse(open(pdf_src, 'rb'))

    def list(self, request):
        url = request.GET.get('url')
        pdf = Pdf.objects.filter(redfin_src=url, deleted=False).first()

        if not pdf:
            raise NotFound(detail='PDF not found')

        serializer = GetPdfSerializer(pdf)

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        pdf = Pdf.objects.filter(pk=pk, deleted=False).first()

        if not pdf:
            raise NotFound(detail='PDF not found')

        pdf.deleted = True
        pdf.save()

        serializer = GetPdfSerializer(pdf)

        return Response(serializer.data)


class SearchView(APIView):
    serializer_class = SearchSerializer

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
            raise RedfinScrapper()


class GoogleAuthViewSet(ViewSet):
    serializer_class = GoogleAuthSerializer

    CLIENT_ID = '783671048395-hblgld7toqqnrciqi477gje5snggtjka.apps.googleusercontent.com'

    CLIENT_SECRET = 'Aq0Lk6xzzKes__d_WLDUuT2z'

    def create(self, request):
        serializer = GoogleAuthSerializer(data=request.data)

        if not serializer.is_valid():
            raise ParseError(detail=serializer.errors)

        credentials = client.credentials_from_code(self.CLIENT_ID, self.CLIENT_SECRET,
                                                   scope=['https://www.googleapis.com/auth/gmail.labels', 'https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.modify'],
                                                   code=serializer.validated_data['code'],
                                                   redirect_uri=serializer.validated_data['redirect_uri'])

        service = build('gmail', 'v1', credentials=credentials)
        print(service.users().labels().list(userId='me').execute())
        return Response("a mers")
