from fastapi import FastAPI, UploadFile, File
import random

app = FastAPI(title="VoiceGuardAI Inference API")

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    result = random.choice(["REAL", "FAKE"])
    confidence = round(random.uniform(0.75, 0.99), 2)

    return {
        "filename": file.filename,
        "prediction": result,
        "confidence": confidence
    }