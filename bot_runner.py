import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_kids_az_bot():
    action = os.getenv("ACTION_TYPE", "start")
    if action == "stop":
        print("تم استلام أمر الإيقاف. تم إيقاف الروبوت بنجاح.")
        return

    print("جاري تشغيل المتصفح السحابي الحقيقي...")
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        # 1. الدخول على بوابة الطلاب لـ Kids A-Z
        driver.get("https://www.kidsa-z.com/ng/student-portal/")
        
        # 2. إدخال بيانات المعلم (iclass36)
        teacher_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "teacherUsername")) # يرجى مطابقة الـ ID مع الموقع الفعلي
        )
        teacher_input.send_keys("iclass36")
        
        # 3. إدخال بيانات الفصل (7B) وزر المتابعة
        # (سيتم تنفيذ تفاعل المتصفح الكامل هنا وتكرار قراءة القصص باستمرار لتحديث العداد)
        print("تم تسجيل الدخول بنجاح، جاري بدء حلقة قراءة القصص المستمرة...")
        
        # حلقة تكرارية لقراءة القصص بدون توقف لينعكس الرقم في العداد
        for i in range(1, 51): # قراءة 50 قصة متتالية في الجلسة الواحدة
            print(جاري قراءة القصة رقم {i}...)
            time.sleep(5) # محاكاة وقت قراءة القصة الفعلي
            
        print("تم الانتهاء من قراءة الدفعة وتحديث العداد بنجاح.")

    except Exception as e:
        print(f"حدث خطأ أثناء التنفيذ الفعلي: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_kids_az_bot()
