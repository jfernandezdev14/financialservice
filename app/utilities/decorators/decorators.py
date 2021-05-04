from functools import wraps

from flask import jsonify
from werkzeug.exceptions import InternalServerError, BadRequest, NotFound, Unauthorized


def api_resource_endpoint():
    """
    Wrapper function to handle API endpoint
    :param logger: DB logger to save a log record
    :param error_code: Int, Custom http error code. Ie, 500
    :param is_view: Bool, the endpoint is a view (lendingportal) or not ?. Ie, False
    :return decorator_function: the decorator itself
    """

    def wrapper_function(function):
        """
        Decorator used in API endpoints to handle the exceptions possibly raised
        :param function: function to be decorated. Function
        :return decorator_function: the decorator itself
        """

        @wraps(function)
        def decorator_function(*args, **kwargs):

            try:
                return function(*args, **kwargs)

            except Unauthorized as e:
                return jsonify(e)

            except NotFound as e:
                return jsonify(e)

            except BadRequest as e:
                return jsonify(e)

            except InternalServerError as e:
                return jsonify(e)

            except Exception as e:
                raise e

        return decorator_function

    return wrapper_function
