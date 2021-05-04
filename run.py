#!flask/bin/python
from flask_restful import Api

from app import app
from app.resources.accounts_resources import AccountsResource

financialservice_api = Api(app)

# List of Endpoints

financialservice_api.add_resource(
    AccountsResource,
    '/financialservice/api/v1.0/accounts'
)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8001)
