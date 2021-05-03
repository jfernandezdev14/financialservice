print('Start #################################################################');
db = db.getSiblingDB('financialservice');
db.createUser(
        {
            user: "api_user",
            pwd: "api_pwd",
            roles: [
                {
                    role: "readWrite",
                    db: "financialservice"
                }
            ]
        }
);
db.createCollection('accounts');
db.createCollection('transactions');
db.accounts.insert({"user_id": "105398891", "balance": 0})
db.accounts.insert({"user_id": "105398892", "balance": 100000})
db.accounts.insert({"user_id": "105398893", "balance": 0})
print('END #################################################################');
