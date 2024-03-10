const express = require('express')
const alasql = require('alasql')
const crypto = require("crypto")
const { v1 } = require('uuid')

const PORT = 3001

const adminRoutes = require('./routes/admin.js')
const appRoutes = require('./routes/app.js')

const app = express()
app.use(express.json())

alasql('CREATE TABLE users (id string, password string, isAdmin boolean);')
alasql('CREATE TABLE logs (time string, message string);')
alasql('INSERT INTO logs VALUES (NOW(), "[+] Server started");')
const adminId = v1()
const guestId = v1()
alasql(`INSERT INTO users VALUES ("${adminId}", "${crypto.randomBytes(20).toString('hex')}", true);`)
alasql(`INSERT INTO logs VALUES (NOW(), "[+] new account - [REDACTED]");`)
alasql(`INSERT INTO users VALUES ("${guestId}", "guest", false);`)
alasql(`INSERT INTO logs VALUES (NOW(), "[+] new account - [${guestId}]");`)
alasql('INSERT INTO logs VALUES (NOW(), "[+] Server started");')

console.log(alasql('SELECT * FROM logs'))
console.log(alasql('SELECT * FROM users'))

app.listen(PORT, () => {
  console.log(`[+] App is running at http://localhost:${PORT}`)
})

app.use('/', appRoutes)
app.use('/admin', adminRoutes)