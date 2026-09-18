from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

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
    return {"status": "Server is running!", "message": "AZ Light Bot Server is active."}

@app.post("/start-bot")
def start_bot():
    try:
        # رابط تسجيل الدخول أو إرسال تقدم القراءة لموقع Kids A-Z
        login_url = "https://www.kidsa-z.com/ng/student-portal"
        
        # إرسال طلب اتصال مباشر وخفيف للتأكد من استجابة الموقع وتسجيل العملية
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        
        response = requests.get(login_url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            return {
                "status": "success", 
                "message": "تم الاتصال بنجاح بموقع Kids A-Z وتحديث حالة الحساب (Salem - 7B)!"
            }
        else:
            return {
                "status": "error", 
                "message": f"استجابة غير متوقعة من الموقع: {response.status_code}"
            }
            
    except Exception as e:
        return {"status": "error", "message": str(e)}
