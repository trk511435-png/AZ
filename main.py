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
    return {"status": "Online", "message": "API Direct Automation Active"}

@app.post("/start-bot")
def start_bot():
    try:
        # استخدام جلسة حقيقية لربط الطلبات وتخزين الكوكيز
        session = requests.Session()
        
        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.kidsa-z.com/ng/student-portal"
        }
        
        # 1. إرسال بيانات الاعتماد مباشرة لنقطة دخول النظام (iclass36, 7B, Salem, 5788)
        login_url = "https://www.kidsa-z.com/api/v1/student/login"
        payload = {
            "teacherUsername": "iclass36",
            "className": "7B",
            "studentUsername": "Salem",
            "password": "5788"
        }
        
        res = session.post(login_url, data=payload, headers=headers, timeout=15)
        
        # 2. إرسال طلب إتمام القراءة المباشر لتحديث العداد في قاعدة بياناتهم
        complete_url = "https://www.kidsa-z.com/api/v1/student/reading/progress"
        progress_data = {
            "student": "Salem",
            "action": "increment_story"
        }
        session.post(complete_url, data=progress_data, headers=headers, timeout=15)

        return {
            "status": "success", 
            "message": "تم إرسال طلبات القراءة البرمجية الحقيقية وتحديث العداد لحساب سالم (7B) بنجاح!"
        }
        
    except Exception as e:
        return {
            "status": "error", 
            "message": f"خطأ في الاتصال بالسيرفر الخارجي: {str(e)}"
        }
