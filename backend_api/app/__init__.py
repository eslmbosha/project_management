# Backend API - Project Management

هذا هو الخادم الخلفي لتطبيق إدارة المشاريع باستخدام **FastAPI** و **Python**.

## 🚀 التشغيل

### 1. إنشاء البيئة الافتراضية
\\\ash
python -m venv venv
venv\Scripts\activate  # في Windows
# source venv/bin/activate  # في Mac/Linux
\\\

### 2. تثبيت الحزم
\\\ash
pip install -r requirements.txt
\\\

### 3. تشغيل الخادم
\\\ash
uvicorn app.main:app --reload
\\\

### 4. فتح التوثيق التفاعلي
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📁 هيكل المشروع

\\\
backend_api/
├── app/
│   ├── api/           # Routes و Dependencies
│   ├── core/          # الإعدادات الأساسية
│   ├── models/        # نماذج قاعدة البيانات
│   ├── schemas/       # هياكل البيانات (Pydantic)
│   ├── services/      # منطق الأعمال
│   ├── utils/         # أدوات مساعدة
│   ├── db/            # اتصال قاعدة البيانات
│   ├── main.py        # نقطة البداية
│   └── __init__.py
├── tests/             # اختبارات الوحدة
├── requirements.txt   # الحزم المطلوبة
└── .env              # متغيرات البيئة
\\\
"@ | Out-File -FilePath backend_api\README.md -Encoding utf8
@"
# ملف تعريف الحزمة
