# اختيار صورة أساسية تعتمدها حاويتك
FROM python:3.9

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملفات مشروعك من مجلد المشروع إلى مجلد العمل داخل الحاوية
COPY . /app

# تثبيت المكتبات اللازمة باستخدام pip
RUN pip install -r requirements.txt

# تثبيت برنامج screen
RUN apt-get update && apt-get install -y screen

# تحديد المنفذ الذي سيعمل عليه التطبيق
EXPOSE 5000

# تشغيل التطبيق عند بدء تشغيل الحاوية واستدعاء برنامج "screen"
CMD ["screen", "-S", "users.py", "python3", "main.py"]
