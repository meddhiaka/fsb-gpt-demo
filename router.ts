import { Router, Request, Response } from "express"
import { PythonShell, Options } from 'python-shell'

const r:Router = Router()

r.get("/", (req: Request, res: Response) => {
    res.send({msg:"you're inside nested route!"})
  })

r.post("/chat", (req: Request, res: Response) => {
  const {message} = req.body

  const options: Options = {
    mode: 'text',
    pythonPath: 'core/venv/bin/python',
    pythonOptions: ['-u'],
    scriptPath: 'core',
    args: [message]
  };

  PythonShell.run('main.py', options)
          .then(results => {
            res.json(results)
          })
          .catch(e => console.error(e))
})


export default r