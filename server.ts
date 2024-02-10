import express, { Express, Request, Response } from "express"
import dotenv from "dotenv"

dotenv.config()

const app: Express = express()
const port = process.env.PORT

app.get("/", (req: Request, res: Response) => {
  res.send({msg:"chatbot serverside root API :)"})
})

app.listen(port, () => {
  console.log(`server is running at http://localhost:${port}`)
})