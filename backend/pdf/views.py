import os

from types import SimpleNamespace

from django.http import FileResponse

from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.response import Response

from .serializers import CreatePdfSerializer, GetPdfSerializer
from .models import Pdf

class PdfViewSet(ViewSet):
    serializer_class = CreatePdfSerializer

    def create(self, request):
        serializer = CreatePdfSerializer(data=request.data)
        
        if not serializer.is_valid():
            raise ParseError(detail=serializer.errors)

        pdf = serializer.save()
        pdf_src = pdf.pdf_src

        if not os.path.exists(pdf_src):
            raise NotFound(detaul="PDF not found")

        return FileResponse(open(pdf_src, 'rb'))


    def list(self, request):
        url = request.GET.get('url')
        pdf = Pdf.objects.filter(redfin_src=url, deleted=False).first()

        if not pdf:
            raise NotFound(detail='PDF not found')

        serializer = GetPdfSerializer(pdf)

        return Response(serializer.data)

    def destroy(self, request):
        url = request.GET.get('url')
        pdf = Pdf.objects.filter(redfin_src=url, deleted=False).first()

        if not pdf:
            raise NotFound(detail='PDF not found')

        pdf.deleted = True
        pdf.save()

        serializer = GetPdfSerializer(pdf)

        return Response(serializer.data)
