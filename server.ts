import cors from "cors"
import express, { Express, Request, Response } from "express"
import dotenv from "dotenv"

import r from "./router"

import bodyParser from "body-parser"

dotenv.config()

const app: Express = express()
const port = process.env.PORT

app.use(cors())
app.use(bodyParser.json())

app.get("/", (req: Request, res: Response) => {
  res.send({ msg: "chatbot serverside root API :)" })
})

app.use("/api", r)

app.listen(port, () => {
  console.log(`server is running at http://localhost:${port}`)
})