from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
async def root():
    return {
        "status": "ok",
        "service": "Vocard",
        "bot": "running"
    }

@app.get("/health")
async def health():
    return {"healthy": True}

def run():
    import uvicorn
    port = int(os.getenv("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
