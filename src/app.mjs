import express from 'express';

const app = express();

const ip = 'localhost';
const port = 8000;

app.use(express.json());
app.set('json spaces', 2);

app.listen(port, ip, () => {
    console.log(`listening at ip: ${ip} and port: ${port}`);
});
