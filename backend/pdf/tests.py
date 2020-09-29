from django.test import TestCase, Client

from .serializers import pdf_service


class TestPdfViewSet(TestCase):
    def setUp(self):
        self.client = Client()
        self.redfin_url = "https://www.redfin.com/IL/Chicago/1000-W-Washington-Blvd-60607/unit-238/home/12789078"

        self.test_contract = "files/test_contract.pdf"

        pdf_service.convert_to_pdf = self.mock_convert_to_pdf

    def mock_convert_to_pdf(self, data):
        return self.test_contract

    def get_pdf(self):
        return self.client.get(f"/api/pdf/", {"url": self.redfin_url})

    def create_pdf(self):
        return self.client.post("/api/pdf/", {"url": self.redfin_url})

    def delete_pdf(self, pk):
        return self.client.delete(f"/api/pdf/{pk}/")

    def test_create_pdf(self):
        response = self.create_pdf()
        self.assertEqual(response.status_code, 200)

        response = self.client.post("/api/pdf/", {"url-wrong": self.redfin_url})
        self.assertEqual(response.status_code, 400)

    def test_get_pdf(self):
        response = self.get_pdf()
        self.assertEqual(response.status_code, 404)

        self.create_pdf()
        response2 = self.get_pdf()
        self.assertEqual(response2.status_code, 200)

    def test_delete_pdf(self):
        self.create_pdf()
        pdf = self.get_pdf()
        self.assertEqual(pdf.status_code, 200)

        self.delete_pdf(pdf.json()["id"])
        self.assertEqual(self.get_pdf().status_code, 404)


class TestSearchView(TestCase):
    def setUp(self):
        self.client = Client()
        self.search_url = "https://www.redfin.com/stingray/do/location-autocomplete?location=824&count=10&v=2"

    def test_search_pdf(self):
        request = self.client.post("/api/search/", {"url": self.search_url})
        response = request.json()
        self.assertNotEqual(len(response["properties"]), 0)
