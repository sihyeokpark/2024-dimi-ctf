const jwt = require('jsonwebtoken')
const express = require('express')
const alasql = require('alasql')
const { v1 } = require('uuid')

const router = express.Router()

const { adminId } = require('../index.js')
const JWTKEY = require('fs').readFileSync('/app/src/jwt.key', 'utf8')

router.use((req, res, next) => {
  const { key } = req.query
  try {
    const data = jwt.verify(key, JWTKEY)
    console.log(data)
    
    if (data.id === adminId) return next()
    else return res.send('Invalid token')
    
  } catch (e) {
    return res.send(e)
  }
})

router.get('/', (req, res) => {
  res.send('Hello admin!')
})

router.post('/adduser', (req, res) => {
  try {
    const { password, isAdmin } = req.body
    const id = v1()
    alasql(`INSERT INTO users VALUES ("${id}", "${password}", ${isAdmin});`)
    alasql(`INSERT INTO logs VALUES (NOW(), "[+] new account - [${isAdmin ? 'REDACTD' : id}]");`)
    res.send('User added')
  } catch (e) {
    res.send(e)
  }
})

module.exports = router