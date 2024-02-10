import { Router, Request, Response } from "express"

const r:Router = Router()

r.get("/", (req: Request, res: Response) => {
    res.send({msg:"you're inside nested route!"})
  })

r.post("/chat", (req: Request, res: Response) => {
//    const result = req.body;
//    res.json(result)
})


export default r