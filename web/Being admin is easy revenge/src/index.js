const express = require('express')

const FLAG = 'DIMI{EXONExonEXONEXONisbabo}'
const app = express()
const PORT = 3000

const users = {
  exon: {
    name: {
      firstName: '시혁',
      lastName: '박'
    },
    age: 18,
    position: 'webhacking',
    type: 'admin'
  },
}

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get('/create', (req, res) => {
  const { user, name, position } = req.query
  const [lastName, firstName] = name.split(' ')

  if (user === 'exon') return res.send('exon is ADMIN!!! you can\'t change it!')
  users[user] = {
    name: {
      firstName,
      lastName
    },
    age: 17,
    position,
  }
  return res.send(`Create Profile Success! ${JSON.stringify(users[user])}`)
})

app.get('/change', (req, res) => {
  const { user, property, position } = req.query
  const previous = users[user][property]
  if (property === 'type') return res.send('You can\'t change type!')
  users[user][property] = position
  res.send('Change Profile Success!')
  setTimeout(() => {
    users[user][property] = previous // rollback
  }, 10000)
})

app.get('/flag', (req, res) => {
  const { user } = req.query
  if (user === 'exon') return res.send('exon is not you!!')
  if (users[user].type === 'admin') {
    res.send(FLAG)
  } else {
    res.send('You are not admin!')
  }
})

app.listen(3000, () => {
  console.log(`listening on port ${PORT}`)
})