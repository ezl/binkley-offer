from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import ParseError

from .serializers import PdfSerializer

class PdfViewSet(ViewSet):
    serializer_class = PdfSerializer 
    
    def create(self, request):
        serializer = PdfSerializer(data=request.data)
        
        if not serializer.is_valid():
            raise ParseError(detail=serializer.errors)

    def retrieve(self, request):
        pass

    def destroy(self, request):
        pass
