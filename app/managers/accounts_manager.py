from app import db


class AccountsManager(object):
    """"
    Contains methods to access or store data of the Accounts
    """

    def __init__(self):
        """
        Initializes AccountsManager instance setting a database session
        """
        self.__db_session = db

    def create_account(self, account_data):
        """"
        Creates an account
        """
        self.__db_session.accounts.insert_one(
            {
             "user_id": account_data.get("user_id"),
             "balance": account_data.get("pin"),
            }
        )

    def retrieve_account(self, filters):
        """"
        Retrieves an account
        :param filters: Dict, contains the information of the account to retrieve. Ie, {"user_id": "0984705245"}
        Ie, {"account_id": "account123", "user_id": {"$oid": "608f44818f5b713944790aac"}}
        :return: Dict, contains the account information
        """
        account = self.__db_session.accounts.find_one(filters)
        return account

    def update_account(self, filters, updated_account):
        """
        Updates the account
        :param filters: Dict, contains the information to filter the data that is going to be updated.
        Ie, {"_id": {"$oid": "08957485230945"}}
        :param updated_account: Dict, contains the updated account information.
        Ie, {"balance": 20000}
        :return:
        """
        self.__db_session.accounts.update_many(filters, updated_account)
        result = {'result': 'Account updated successfully'}
        return result
