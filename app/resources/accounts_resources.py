from flask import request, jsonify
from flask_restful import Resource

from app.controllers.accounts_controller import AccountsController
from app.utilities.decorators.decorators import api_resource_endpoint


class AccountsResource(Resource):
    """
    Contains the list of methods exposed of the UsersResource
    """
    @api_resource_endpoint()
    def get(self):
        """
        Retrieves the information of an user
        :return:
        """
        data = request.get_json(force=True)
        accounts_controller = AccountsController()
        account = accounts_controller.retrieve_account(filters=data)
        return jsonify(account)

    @api_resource_endpoint()
    def patch(self):
        """
        Retrieves the information of an user
        :return:
        """
        data = request.get_json(force=True)
        accounts_controller = AccountsController()
        account = accounts_controller.update_account(account_data=data)
        return jsonify(account)
