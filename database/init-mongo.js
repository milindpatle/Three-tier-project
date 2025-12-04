db = db.getSiblingDB('bankdb');
db.createUser({
  user: 'bankuser',
  pwd: 'bankpass',
  roles: [{ role: 'readWrite', db: 'bankdb' }]
});
db.accounts.insertMany([
  { username: 'alice', balance: 5000 },
  { username: 'bob', balance: 3000 }
]);
print('mongo init done');
