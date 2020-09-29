from .pdf import PdfsApi, PdfApi
from .search import SearchApi


def initialize_routes(api):
    api.add_resource(PdfsApi, '/api/pdfs')
    api.add_resource(PdfApi, '/api/pdf')
    api.add_resource(SearchApi, '/api/search')
