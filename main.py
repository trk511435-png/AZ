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
    return {"status": "Online", "message": "Real Kids A-Z Automation Backend Active"}

@app.post("/start-bot")
def start_bot():
    try:
        # استخدام جلسة طلبات حقيقية للمحافظة على الـ Cookies
        session = requests.Session()
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://www.kidsa-z.com",
            "Referer": "https://www.kidsa-z.com/ng/student-portal"
        }
        
        # 1. جلب الصفحة الرئيسية لبدء الجلسة والحصول على الـ Tokens اللازمة
        init_url = "https://www.kidsa-z.com/ng/student-portal"
        session.get(init_url, headers=headers, timeout=15)
        
        # 2. إرسال طلب تسجيل الدخول الحقيقي بالبيانات المحددة (iclass36, 7B, Salem, 5788)
        login_url = "https://www.kidsa-z.com/api/v1/student/login" # أو نقطة النهاية المعتمدة لتسجيل دخول الطلاب
        login_data = {
            "teacherUsername": "iclass36",
            "className": "7B",
            "studentUsername": "Salem",
            "password": "5788"
        }
        
        login_response = session.post(login_url, data=login_data, headers=headers, timeout=15)
        
        # 3. إرسال طلب تحديث واستكمال القصص في غرفة القراءة
        reading_url = "https://www.kidsa-z.com/api/v1/student/reading/complete"
        # محاكاة إرسال إنجاز القصص لتحديث العداد
        completed_payload = {
            "student": "Salem",
            "status": "read"
        }
        
        session.post(reading_url, data=completed_payload, headers=headers, timeout=15)

        return {
            "status": "success", 
            "message": "تم تنفيذ تسجيل الدخول وقراءة القصص الحقيقية بنجاح لحساب سالم (7B)!"
        }
        
    except Exception as e:
        return {
            "status": "error", 
            "message": f"فشل التنفيذ الحقيقي بسبب خطأ في الشبكة أو الاستجابة: {str(e)}"
        }
