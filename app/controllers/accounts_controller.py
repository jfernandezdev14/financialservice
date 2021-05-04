from bson import ObjectId

from app.utilities.exceptions.accounts_exceptions import AccountNotFound
from app.managers.accounts_manager import AccountsManager


class AccountsController(object):
    """
    Contains the logic related to the users functionalities
    """

    @staticmethod
    def retrieve_account(filters):
        """
        Retrieves the account information
        :param filters: Dict, contains the information of the account to retrieve. Ie, {"user_id": "0984705245"}
        :return: Object, Returns the account information
        """

        accounts_manager = AccountsManager()
        account_retrieved = accounts_manager.retrieve_account(filters)
        if not account_retrieved:
            raise AccountNotFound(message="Account not found, please confirm if the values are correct")
        account = {'user_id': account_retrieved['user_id'], 'balance': account_retrieved['balance']}
        return account

    @staticmethod
    def update_account(account_data):
        """
        Updates the account information
        :param account_data: Dict, Contains the account information. Ie, {"balance": 1000}
        :return: Object, Returns the account updated
        """

        accounts_manager = AccountsManager()
        filters = account_data.pop('filters', {})
        data_updated = account_data.pop('data_updated', {})
        account_updated = {'$set': data_updated}
        result = accounts_manager.update_account(filters, account_updated)
        return result
