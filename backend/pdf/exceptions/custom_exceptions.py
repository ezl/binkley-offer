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


class InvalidPassword(APIException):
    status_code = 409
    default_detail = """Password to weak:
    Minimum 4 characters.
    The alphabets must be between [a-z]
    At least one alphabet should be of Upper Case [A-Z]
    At least 1 number or digit between [0-9].
    At least 1 character from [ ! or @ or # or $ or % or ^ or & or * or ( or ) ]."""
    default_code = "invalid_password_strength"
