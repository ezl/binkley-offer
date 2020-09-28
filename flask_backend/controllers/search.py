from flask import request
from flask_restful import Resource

import services.search_service


class SearchApi(Resource):
    def post(self):
        redfin_search_autocomplete_url = request.get_json().get('url')
        return services.search_service.search_redfin_autocomplete_api(redfin_search_autocomplete_url), 200
