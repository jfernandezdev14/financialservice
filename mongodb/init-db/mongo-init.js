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
db.createCollection('accounts', { capped : true, size : 5242880, max : 5000 } );
db.createCollection('transactions', { capped : true, size : 5242880, max : 5000 } );
print('END #################################################################');
