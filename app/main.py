from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.runner import execute_script

app = FastAPI()

class ScriptInput(BaseModel):
    script: str

@app.post("/run-script")
async def run_script(input: ScriptInput):
    result = await execute_script(input.script)
    if result["success"]:
        return result
    raise HTTPException(status_code=500, detail=result["error"])
