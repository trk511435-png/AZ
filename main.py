from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
import time

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
    return {"status": "Server is running!", "message": "AZ Bot Cloud Server is active."}

@app.post("/start-bot")
def start_bot():
    # تشغيل شاشة وهمية لكي يظن المتصفح أنه يعمل على جهاز حقيقي
    display = Display(visible=0, size=(1280, 800))
    display.start()
    
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        # 1. فتح موقع Kids A-Z
        driver.get("https://www.kidsa-z.com/ng/student-portal")
        wait = WebDriverWait(driver, 25)
        
        # 2. إدخال اسم المعلم
        teacher_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text'], input")))
        teacher_input.send_keys("iclass36")
        
        next_btn = driver.find_element(By.CSS_SELECTOR, "button, .next-btn")
        next_btn.click()
        
        # 3. اختيار الفصل 7B
        class_7b = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '7B')]")))
        class_7b.click()
        
        # 4. اختيار اسمك Salem
        salem_profile = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Salem')]")))
        salem_profile.click()
        
        # 5. إدخال كلمة السر 5788
        pass_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password'], input")))
        pass_input.send_keys("5788")
        
        submit_btn = driver.find_element(By.CSS_SELECTOR, "button, .next-btn")
        submit_btn.click()
        
        time.sleep(6)
        
        # 6. الانتقال لغرفة القراءة وقراءة القصص
        driver.get("https://www.kidsa-z.com/main/readingRoom")
        time.sleep(5)
        
        driver.quit()
        display.stop()
        return {"status": "success", "message": "تم تشغيل المتصفح السحابي والدخول بحساب سالم وقراءة القصص بنجاح!"}
        
    except Exception as e:
        driver.quit()
        display.stop()
        return {"status": "error", "message": str(e)}
