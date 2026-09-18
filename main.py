from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

app = FastAPI()

# السماح للاتصالات من موقعك على GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Server is running!", "message": "AZ Bot Server is active."}

@app.post("/start-bot")
def start_bot():
    options = webdriver.ChromeOptions()
    # تشغيل المتصفح بوضع المخفي (لأن السيرفر السحابي لا يحتوي على شاشة عرض حقيقية)
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        # 1. فتح موقع Kids A-Z
        driver.get("https://www.kidsa-z.com/ng/student-portal")
        wait = WebDriverWait(driver, 15)
        
        # 2. إدخال اسم المستخدم للمعلم
        teacher_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text'], input")))
        teacher_input.send_keys("iclass36")
        
        # زر التالي
        next_btn = driver.find_element(By.CSS_SELECTOR, "button, .next-btn")
        next_btn.click()
        
        # 3. اختيار الفصل 7B
        class_7b = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '7B')]")))
        class_7b.click()
        
        # 4. اختيار اسمك Salem
        salem_profile = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Salem')]")))
        salem_profile.click()
        
        # 5. إدخال كلمة السر
        pass_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password'], input")))
        pass_input.send_keys("5788")
        
        submit_btn = driver.find_element(By.CSS_SELECTOR, "button, .next-btn")
        submit_btn.click()
        
        time.sleep(5)
        
        driver.quit()
        return {"status": "success", "message": "تم تسجيل الدخول بنجاح من السيرفر!"}
        
    except Exception as e:
        driver.quit()
        return {"status": "error", "message": str(e)}
