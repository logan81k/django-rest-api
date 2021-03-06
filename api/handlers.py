import logging

from rest_framework.views import exception_handler

from api.base.exceptions import ServiceException

logger = logging.getLogger(__name__)

'''
{
    "status": 401,
    "code": 2500,
    "message": "error message",
    "more_info": "http://www.bitberry.app/docs/errors/2500"
}
'''


def api_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    print(f"response: {response}, {type(exc)}, {exc}")
    if response:
        if isinstance(exc, ServiceException):
            response.data["code"] = exc.code
            response.data["detail"] = exc.detail
            response.data["more_info"] = exc.more_info

        response.data['status'] = response.status_code

    return response
