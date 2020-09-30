from rest_framework.exceptions import APIException


class RedfinScrapper(APIException):
    status_code = 409
    default_detail = "Scrapper Failed for Redfin "
    default_code = "fail_scrapper"
