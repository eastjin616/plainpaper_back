from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "✅ plainpaper backend 정상 작동 중!"}