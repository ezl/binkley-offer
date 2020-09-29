import os

from types import SimpleNamespace

from django.http import FileResponse

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.response import Response

from .serializers import CreatePdfSerializer, GetPdfSerializer, SearchSerializer
from .models import Pdf

from .services.search_service import search_redfin_autocomplete_api

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
