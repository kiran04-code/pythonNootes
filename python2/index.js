const express = require('express');
const app = express();
const port = 3008;

app.get("/",(req,res)=>{
    return res.send("Hello World")
})
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
})