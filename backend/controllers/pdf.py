from flask import Response, request, send_file
from database.models import Pdf, StaticPdfBody
import services.pdf_service
import json
from flask_restful import Resource
from flask_pydantic import validate


class PdfsApi(Resource):
    @validate(body=StaticPdfBody)
    def post(self):
        try:
            pdf_from_database = Pdf.objects.get(redfin_src=request.body_params.url, deleted=False)
            return send_file(json.loads(pdf_from_database.to_json()).get('pdf_src'))
        except Exception as e:
            print(f'File does not exist, except and creating a new one. Error: {e}')
        pdf_src = services.pdf_service.convert_to_pdf(request.body_params)
        pdf = Pdf(redfin_src=request.body_params.url, pdf_src=pdf_src, deleted=False).save()
        return send_file(pdf_src, as_attachment=True)


class PdfApi(Resource):
    def get(self):
        url = request.args.get('url')
        pdf = Pdf.objects.get(redfin_src=url).to_json()
        return Response(pdf, mimetype='application/json', status=200)

    def delete(self):
        url = request.args.get('url')
        Pdf.objects.get(redfin_src=url).update(deleted=True)
        pdf = Pdf.objects.get(redfin_src=url).to_json()
        return Response(pdf, mimetype='application/json', status=200)
