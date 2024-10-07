import express from 'express'
import { getNotes } from './database.js';
import cors from 'cors';


 const app = express()

 app.use(cors());

app.get("/notes",async(req, res)=> {

    const notes = await getNotes()
    res.send(notes)
})

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});