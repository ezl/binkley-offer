from rest_framework.exceptions import APIException


class UnhandledException(APIException):
    status_code = 500
    default_detail = "Unhandled Exception"
    default_code = "unhandled_exception"


class RedfinScrapperException(APIException):
    status_code = 409
    default_detail = "Scrapper Failed for Redfin "
    default_code = "fail_scrapper"


class InvalidPropertyType(APIException):
    status_code = 401
    default_detail = "Invalid Property Type only <<attached>> and <<detached>> are available and required"
    default_code = "invalid_property_type"


class DuplicateEntityException(APIException):
    status_code = 409
    default_code = "duplicate_entity"

    def __init__(self, class_name):
        if class_name:
            detail = f"Duplicate Entity for {class_name}"
        else:
            detail = f"Duplicate Entity <<debugger>>"
        super().__init__(detail)
