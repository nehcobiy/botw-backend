from rest_framework import status
from rest_framework.exceptions import APIException

class BaseCustomException(APIException):
    detail = None
    status_code = None

    def __init__(self, detail, code):
        super().__init__(detail, code)
        self.detail = detail
        self.status_code = code
    
class NonexistentIdException(BaseCustomException):
    def __init__(self):
        self.detail = 'Nonexistent id'
        super().__init__(self.detail, status.HTTP_404_NOT_FOUND)

class InvalidIdException(BaseCustomException):
    def __init__(self):
        self.detail = 'Invalid id data type: id must be an integer'
        super().__init__(self.detail, status.HTTP_400_BAD_REQUEST)