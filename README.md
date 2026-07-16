# 📱 Project Management App

تطبيق إدارة مشاريع مدمج مع Flutter (Frontend) و Python (Backend)

## 🏗️ الهيكل

\\\
project_management/
├── mobile_app/          # تطبيق Flutter
│   ├── lib/
│   │   ├── core/        # الأدوات العامة
│   │   ├── models/      # نماذج البيانات
│   │   ├── services/    # خدمات API
│   │   ├── providers/   # إدارة الحالة
│   │   ├── screens/     # الشاشات
│   │   └── widgets/     # عناصر UI
│   └── assets/          # الصور والخطوط
└── backend_api/         # API باستخدام Python
\\\

## 🚀 التشغيل

\\\ash
# Flutter
cd mobile_app
flutter pub get
flutter run

# Python
cd backend_api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
\\\

## 📦 التقنيات المستخدمة

- **Flutter** - واجهة المستخدم
- **Python (FastAPI/Django)** - الخادم الخلفي
- **Git & GitHub** - التحكم في الإصدارات
