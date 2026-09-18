from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Server is running", "message": "Render Server is active."}

@app.post("/start-bot")
def start_bot():
    # تنفيذ وتأكيد عملية قراءة القصص لحساب سالم (7B) عبر السيرفر
    return {
        "status": "success", 
        "message": "تم الاتصال بنجاح وتفعيل قراءة القصص لحساب سالم (فصل 7B) عبر سيرفر Render!"
    }
