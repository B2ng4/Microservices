const express = require("express");
const searchBooks = require('./controllers/apiReq');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());

app.get("/", function(req, res) {
    res.send("Сервис Литература");
});

app.get("/get/books/:nameBook", async function(req, res) {
    const nameBook = req.params.nameBook;

    if (!nameBook) {
        return res.status(400).send("Никаких параметров не передано");
    }

    try {
        const lessonsData = await searchBooks(nameBook); 
        if (lessonsData && lessonsData.length > 0) {
            res.json(lessonsData); 
        } else {
            res.status(404).send("No books found for the specified name.");
        }
    } catch (error) {
        console.error('Error fetching books:', error);
        res.status(500).send("Internal server error");
    }
});

app.listen(3000, () => {
    console.log(`Server is running on port ${3000}`);
});