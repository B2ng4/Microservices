const express = require("express")

const app = express()

app.get("/get/lessons", function(request, response){
    response.send("")
})

app.listen(3000);