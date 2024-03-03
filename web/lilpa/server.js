const express = require('express');
const cookieParser = require('cookie-parser');
const app = express();
const path = require('path');
const PORT = 3001;

app.use(express.static(path.join(__dirname)));
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

function checkAllMembersYes(req) {
    var members = ["GOSEGU", "INE", "JINGBURGER", "JURURU", "VIICHAN"];
    return members.every(member => req.cookies[member] === "yes");
}

app.post('/get-flag', (req, res) => {
    if (checkAllMembersYes(req)) {
        res.status(200).send("성공!\nDIMI{Every_G0t_Yummy_C00kie!}");
    } else {
        res.status(400).send("Not all members have set their cookie to 'yes'");
    }
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
