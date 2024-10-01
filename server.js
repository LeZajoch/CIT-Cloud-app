const express = require('express');
const mongoose = require('mongoose');
const app = express();

// Připojení k MongoDB
mongoose.connect('mongodb://localhost/cit-cloud', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

// Definice schématu pro příspěvek
const postSchema = new mongoose.Schema({
    title: String,
    content: String
});

const Post = mongoose.model('Post', postSchema);

// Middleware pro obsluhu statických souborů (CSS, JS)
app.use(express.static('public'));

// Endpoint pro získání příspěvků
app.get('/posts', async (req, res) => {
    const posts = await Post.find();
    res.json(posts);
});

// Spuštění serveru
app.listen(3000, () => {
    console.log('Server běží na http://localhost:3000');
});
