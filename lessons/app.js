const express = require("express");
const Lessons = require('./controllers/Lessons'); 
const GigaChatPromt = require('./controllers/GigaChatPromt'); 
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json()); 

app.post("/post/lessons", async function(request, response) {
    const userTelegramId = request.body.userTelegramId;

    if (!userTelegramId) {
        return response.status(400).send("userTelegramId is required");
    }

    try {
        const lessonsData = await Lessons(userTelegramId);
        if (lessonsData) {
            response.json(lessonsData);
        } else {
            response.status(404).send("No lessons found for the specified user.");
        }
    } catch (error) {
        console.error('Error fetching lessons:', error);
        response.status(500).send("Internal server error");
    }
});
app.post("/post/information", async function(request, response) {
    const promt = request.body.promt;

    if (!promt) {
        return response.status(400).send("promt is required");
    }

    try {
        const lessonsData = await GigaChatPromt(promt);
        if (lessonsData) {
            response.json(lessonsData);
        } else {
            response.status(404).send("No relevant content found for the specified prompt.");
        }
    } catch (error) {
        console.error('Error fetching lessons:', error);
        response.status(500).send("Internal server error");
    }
});


app.listen(3000, () => {
    console.log(`Server is running on port ${3000}`);
});
