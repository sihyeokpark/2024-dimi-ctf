const express = require('express');
const app = express();
const path = require('path');
const sqlite3 = require('sqlite3').verbose();

const PORT = 3000;

let db = new sqlite3.Database('./users.db', (err) => {
    if (err) {
        console.error(err.message);
    } else {
        console.log('Connected to the SQLite database.');

        db.run("CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, pw TEXT NOT NULL, isAdmin INTEGER NOT NULL)", (err) => {
            if (err) {
                console.error(err.message);
            } else {
                console.log('Table created or already exists.');
                insertUsers();
            }
        });
    }
});

const insertUsers = () => {
    const insertQuery = `INSERT OR IGNORE INTO users (id, pw, isAdmin) VALUES (?, ?, ?)`;

    db.run(insertQuery, ['guest', 'guest', 0], (err) => {
        if (err) {
            return console.error(err.message);
        }
        console.log('GUEST 사용자 추가됨');
    });

    db.run(insertQuery, ['admin', 'N0w_y0u_kn0w_SQL_Injection', 1], (err) => {
        if (err) {
            return console.error(err.message);
        }
        console.log('ADMIN 사용자 추가됨');
    });
};

app.use(express.static(path.join(__dirname)));
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.post('/login', (req, res) => {
    const id = req.body.id;
    const pw = req.body.pw;

    const query = `SELECT * FROM users WHERE id = '${id}' AND pw = '${pw}';`
    db.get(query, (err, row) => {
        if (err) {
            res.send("오류 발생: " + err.message);
            return;
        }
        if (row) {
            if (row.isAdmin) {
                res.send("성공!\n" + "DIMI{N0w_y0u_kn0w_SQL_Injection}");
            } else {
                res.send("GUEST 로그인 성공!");
            }
        } else {
            res.send("실패!");
        }
    });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
