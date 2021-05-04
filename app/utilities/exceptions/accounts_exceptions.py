from app.utilities.exceptions.exceptions import HttpNotFound


class AccountNotFound(HttpNotFound):
    def __init__(self, message=''):
        HttpNotFound.__init__(self, message)


class FiltersNotFound(HttpNotFound):
    def __init__(self, message=''):
        HttpNotFound.__init__(self, message)

