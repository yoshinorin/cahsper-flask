from werkzeug.exceptions import HTTPException

class UnauthorizedException(HTTPException):
    code = 401

class NotFoundException(HTTPException):
    code = 404

class InternalServerException(HTTPException):
    code = 500
