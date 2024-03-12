const jwt = require('jsonwebtoken')
const express = require('express')
const alasql = require('alasql')
const ip = require('ip')
const { get } = require('axios')

const JWTKEY = require('fs').readFileSync('/app/src/jwt.key', 'utf8')

const router = express.Router()

router.get('/', (req, res) => {
  res.send('hello')
})

router.get('/login', (req, res) => {
  const { id, password } = req.query
  const users = alasql(`SELECT * FROM users`)
  users.forEach((user) => {
    if (user.id === id && user.password === password) {
      const token = jwt.sign({
        id: user.id,
        isAdmin: user.isAdmin
      }, JWTKEY, { expiresIn: '1h', algorithm: 'HS256' })
      alasql(`INSERT INTO logs VALUES (NOW(), "[+] ${user.id} login");`)
      return res.send({ token })
    }
  })
  res.send('Login failed')
})

router.get('/log', (req, res) => {
  let reqIp = req.ip
  if (reqIp.startsWith('::ffff:')) reqIp = reqIp.slice(7)
  if (reqIp !== '127.0.0.1' && reqIp !== '::1') {
    const logs = alasql('SELECT * FROM logs')
    res.send(logs)
  } else {
    res.send(JWTKEY)
  }
})

router.post('/log', async (req, res) => {
  const url = new URL(`http://${req.body.url}`)
  if (ip.isPublic(url.hostname) && parseInt(url.hostname) !== NaN) {
    try {
      const { data } = await get(`http://${req.body.url}`)
      console.log(data)
      return res.send(data)
    } catch(e) {
      return res.send(e.message)
    }
  } else {
    return res.send('Invalid URL')
  }
})

module.exports = router